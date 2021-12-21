from docutils import nodes
from docutils.parsers.rst.directives.body import Compound
from docutils.parsers.rst.directives import flag
from docutils.statemachine import StringList
from sphinx.util.nodes import set_source_info
from functools import reduce
import os
import json
import operator
import logging


debug = False

tab = '   '

def convert_default_value(s):
    v = str(s)
    if v.lower() == 'true':
        return 'Yes'
    elif v.lower() == 'false':
        return 'No'
    else:
        return v

metadata_to_document = [('_default' , 'Default value'   ,convert_default_value),
                        ('_choices' , 'Options'         ,lambda s: str(s).replace("'","")),
                        ('_unit'    , 'Unit'            ,lambda s: str(s)),
                        ('_unique'  , 'Recurring'       ,lambda s: str(not s)),
                        ('_gui_name', 'GUI name'        ,lambda s: str(s).rstrip(':')),
                        ('_comment' , 'Description'     ,lambda s: str(s))]

kf_def_metadata_to_document = [('_type'             , 'Type'            ,lambda s: str(s)),
                               ('_comment'          , 'Description'     ,lambda s: str(s)),
                               ('_unit'             , 'Unit'            ,lambda s: str(s)),
                               ('_possible_values'  , 'Possible values' ,lambda s: str(s)),
                               ('_values_range'     , 'Values range'    ,lambda s: str(s).replace("//","")),
                               ('_shape'            , 'Shape'           ,lambda s: str(s).replace("'",""))]


# This will contain the list of keys to be referenced from scmautodocindex:
list_of_scmautodoc = []
n_ref_per_key = {}


def setup(app):
    app.add_node(scmautodoc)
    app.add_directive('scmautodoc', SCMAutoDoc)
    app.add_directive('scmautodocindex', SCMAutoDocIndex)
    app.add_directive('scmautodoclist', SCMAutoDocList)
    app.add_directive('scmautodockf', SCMAutoDocKF)
    app.connect('doctree-read', collect_list_of_scmautodoc)
    app.connect('doctree-resolved', process_scmautodoc_nodes)
    return {'parallel_read_safe':False}


class scmautodoc(nodes.Element):
    pass


class scmautodocindex(nodes.General, nodes.Element):
    pass


class scmautodoclist(nodes.Element):
    pass


class scmautodockf(nodes.Element):
    pass


class SCMAutoDoc(Compound):
    """
        Document a key (and possibly all sub-keys/sub-blocks) by reading the info from the json definitions file.
        Simple usage example: ".. scmautodoc:: band Basis"
        This will document the Basis key/block (and recursively all sub-keys/sub-blocks) from the file band.json.
        It will also create a label for cross-reference named key-Basis.
        One can also explicitly specify a list of sub-keys, e.g.: ".. scmautodoc:: band Basis Type Core"
    """

    has_content               = False
    required_arguments        = 2
    optional_arguments        = 1
    final_argument_whitespace = True

    option_spec = {'notrecursive'                 : flag,    # do not recursively document sub-keys/sub-blocks
                   'nosummary'                    : flag,    # do not create the key summary
                   'onlysummary'                  : flag,    # only create the key summary
                   'skipblockdescription'         : flag,    # do not print the description of the top level block
                   'noref'                        : flag,    # do not create a label for cross-reference (if a key is documented multiple times, you should include it in all but one instances)
                   'collapselongchoicesinsummary' : flag}    # When creating the summary: if there are many 'choices' (>10), show "[...]" instead of the long list of choices

    def run(self):
        node = scmautodoc()
        node.document = self.state.document
        set_source_info(self, node)

        json_filename = self.arguments[0]
        key           = self.arguments[1]
        sub_keys      = self.arguments[2] if len(self.arguments)>2 else None

        if debug: print("\n\nIn SCMAutoDoc run")
        if debug: print("Arguments  : ", self.arguments)
        if debug: print("Options    : ", self.options)

        recursive                        = not('notrecursive' in self.options)
        summary                          = not('nosummary' in self.options)
        make_ref                         = not('noref' in self.options)
        skip_block_description           = 'skipblockdescription' in self.options
        only_suymmary                    = 'onlysummary' in self.options
        collapse_long_choices_in_summary = 'collapselongchoicesinsummary' in self.options
        document_keys = not only_suymmary

        node['key'] = (json_filename,key)
        node['make_ref'] = make_ref


        self.content = StringList(generate_doc(json_filename, key, sub_keys, recursive, document_keys, summary, make_ref, skip_block_description, collapse_long_choices_in_summary))

        if debug:
            print("=== Generated rst content from SCMAutoDoc ===\n")
            for line in self.content: print(line)

        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class SCMAutoDocIndex(Compound):
    """
        Create a list with links to all documented keywords.
    """

    has_content               = False
    required_arguments        = 0
    optional_arguments        = 0
    final_argument_whitespace = False

    option_spec = {}

    def run(self):
        node = scmautodocindex()
        node.document = self.state.document
        set_source_info(self, node)

        content = []

        # which json files have been documented?
        json_files = set([json_filename for json_filename, key in list_of_scmautodoc])

        # check that all keys have been referenced at least once
        for key, n_refs in n_ref_per_key.items():
            if n_refs == 0:
                logging.warn(f'SCMAutoDoc: key "{key}" is included, but no reference/label was created (the :noref: was used every time this key was included). Remove the :noref: from one of the scmautodoc directives, otherwise this key will not end up in the index.')


        for j_header in sorted(json_files):

            content.append(f"**{j_header.replace('.json','')}:**")
            content.append("")

            content.append('.. hlist::')
            content.append(tab+':columns: 2')
            content.append(tab)

            for json_filename, key in sorted(list_of_scmautodoc):
                if j_header==json_filename:
                    content.append(tab+'* :ref:`'+key.replace('%', ' > ') +' <'+link_name(json_filename,key)+'>`')

            content.append("")


        self.content = StringList(content)

        if debug:
            print("=== Generated rst content from SCMAutoDocIndex ===\n")
            for line in self.content: print(line)

        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class SCMAutoDocList(Compound):
    """
        Document all non-hidden keywords for the specified json file.
        Usage example: ".. scmautodoclist:: band"
    """

    has_content               = False
    required_arguments        = 1
    optional_arguments        = 0
    final_argument_whitespace = False

    option_spec = {}

    def run(self):
        node = scmautodoclist()
        node.document = self.state.document
        set_source_info(self, node)

        json_filename = self.arguments[0]

        defs = load_json_def('input_def', json_filename)

        content = []

        for key in sorted(defs, key=str.lower):
            # label for cross referencing:
            content.append(f".. _scmautodoclist-{json_filename.replace('.json','')}-{key}:")
            content.append("")
            content += generate_doc(json_filename, key, sub_keys=None, recursive=True, document_keys=True, summary=False, make_ref=False, skip_block_description=False, collapse_long_choices_in_summary=False)
            content.append("")

        self.content = StringList(content)

        if debug:
            print("=== Generated rst content from SCMAutoDocList ===\n")
            for line in self.content: print(line)

        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def process_scmautodoc_nodes(app, doctree, docname):
    ns = dict((k, app.config[k]) for k in app.config.values)
    ns.update(app.config.__dict__.copy())
    ns['builder'] = app.builder.name

    for node in doctree.traverse(scmautodoc):
        node.replace_self(node.children)

    for node in doctree.traverse(scmautodocindex):
        node.replace_self(node.children)

    for node in doctree.traverse(scmautodoclist):
        node.replace_self(node.children)


def generate_doc(json_filename, key, sub_keys, recursive, document_keys, summary, make_ref, skip_block_description, collapse_long_choices_in_summary):
    """
        Return the documentation of a key as a list of lines in 'rst' (restructured text) format
    """

    lines = []

    defs = load_json_def('input_def', json_filename)

    names, nodes, depths = collect_keys_to_document(defs, key, sub_keys, recursive)

    if len(names)==0: return lines

    if debug: print(names)
    if debug: print(depths)

    if make_ref:
        lines.append('.. _'+link_name(json_filename, key)+":")
        lines.append('')

    if summary:
        lines += make_summary(names, nodes, depths, collapse_long_choices_in_summary)

    if document_keys:
        for name, node, depth in zip(names, nodes, depths):
            lines += document_key(name, node, depth, depth==0 and skip_block_description)

    return lines


def collect_keys_to_document(defs, key, sub_keys, recursive, depth=0):
    """
        Return the list of the key names that should be documented, alongside with the
        corresponding node in the definitions-dictionary and the hierarchical depth WRT 'key'
    """

    names, nodes, depths = [], [], []

    key_path = key.split('%')
    key_name = key_path[-1]
    node = reduce(operator.getitem, key_path, defs)

    # do not document hidden keys:
    if '_hidden' in node and node['_hidden'] == True:
        return [], [], []

    # do not document hidden choices:
    if '_choices' in node and '_hiddenchoices' in node:
        hidden_choices = set(node['_hiddenchoices'])
        node['_choices'] = [x for x in node['_choices'] if x not in hidden_choices]

    names.append(key_name)
    nodes.append(node)
    depths.append(depth)

    if sub_keys:
        for sub_key in sub_keys.split():
            sub_names, sub_nodes, sub_depths = collect_keys_to_document(node, sub_key, None,
                                                                        recursive, depth=len(sub_key.split('%')))
            names  += sub_names
            nodes  += sub_nodes
            depths += sub_depths
    elif recursive:
        for k in sorted(node):
            if not k.startswith('_'):
                sub_names, sub_nodes, sub_depths = collect_keys_to_document(node, k, None, True, depth=depth+1)
                names  += sub_names
                nodes  += sub_nodes
                depths += sub_depths

    return names, nodes, depths


def make_summary(names, nodes, depths, collapse_long_choices_in_summary):
    """
        Make a mock input (in an rst code-block) that serves as a summary for the block/key.
    """

    lines = []

    n_items = len(names)

    if n_items==0:
        return lines

    lines.append('.. code-block:: none')
    lines.append('')

    for name, node, depth, i in zip(names, nodes, depths, range(n_items)):

        indented_name = (depth+1)*tab + name

        if node['_category'] == 'block':
            extra = ''
            if '_header' in node and node['_header']: extra += ' header'
            if node['_type'] == 'free': extra += ' # Non-standard block. See details.'
            lines.append(indented_name + extra)

            if node['_type'] == 'free':
                lines.append((depth+2)*tab + "...")
                lines.append((depth+1)*tab+'End')

        elif node['_category'] == 'key':
            if node['_type'] == 'multiple_choice':
                if collapse_long_choices_in_summary and len(node['_choices']) > 10:
                    lines.append(f"{indented_name} [...]")
                else:
                    for line in _summary_for_multiple_choices(indented_name, node['_choices']):
                        lines.append(line)

            elif node['_type'] == 'bool':
                lines.append(indented_name + ' Yes/No')
            else:
                lines.append(indented_name + ' ' + node['_type'])

        # Add End of blocks:
        if i<n_items-1: # not the last element
            for i in range(depth,depths[i+1],-1):
                lines.append((i)*tab+'End')

    # Close all remaining blocks:
    if len(depths)>0:
        for i in range(depths[-1],0,-1):
            lines.append((i)*tab+'End')

    # Special case: if all there is to document is a single empty block, close it here:
    if n_items==1 and nodes[0]['_category']=='block' and nodes[0]['_type']=='fixed':
        lines.append(tab+'End')

    lines.append('')
    return lines



def _summary_for_multiple_choices(indented_name: str, choices: list) -> list:
    newline_threshold = 90

    lines = [indented_name + ' [']
    for i, choice in enumerate(choices):
        if i < len(choices)-1: 
            lines[-1] += f"{choice} | "
            if len(lines[-1]) > newline_threshold:
                lines.append(' '*(len(indented_name) + 2))
        else:
            lines[-1] += f"{choice}]"
            
    return lines



def document_key(key, node, depth, skipdescription=False):
    """
        Return a list of lines representing the documentation of a single key/block
    """

    lines = []

    lines.append(depth*tab + literal(key))

    if not(skipdescription):
        # Make a single-line description of the type of key (e.g. 'block' or 'integer list')
        if node['_category']=='block':
            if node['_type']=='free':
                key_type = 'Non-standard block'
            else:
                key_type = 'Block'
        elif node['_category']=='key':
            key_type = node['_type'].title().replace('_',' ')

        lines.append((depth+1)*tab + ':Type: ' + key_type)

        # Document optional metadata:
        for metadata, description, process_content in metadata_to_document:
            if metadata in node:
                # Get rid of new lines:
                text =  process_content(node[metadata])
                lines.append((depth+1)*tab + ':' + description + ': ' + text)
        lines.append('')

    # escape special characters:
    lines = [line.replace('*','\*') for line in lines]

    return lines


def literal(s):
    return '``'+s+'``'


def link_name(json_filename, key):
    return f"{json_filename.replace('.json','')}-key-{key}"


def collect_list_of_scmautodoc(app, doctree):
    for node in doctree.traverse(scmautodoc):
        key = node['key']

        if not key in n_ref_per_key:
            n_ref_per_key[key] = 0

        if node['make_ref']:
            if any(key==k for k in list_of_scmautodoc):
                logging.warn('SCMAutoDoc: key "{}". If a keyword is documented with scmautodoc multiple times, you should include the :noref: option in all but one instances. '.format(node['key']))
            list_of_scmautodoc.append(key)
            n_ref_per_key[key] += 1


def load_json_def(folder, json_filename):
    json_decoder = json.JSONDecoder()
    jsonFile = os.path.join('..','bin',folder,json_filename+'.json')

    with open(jsonFile) as def_file:
        file_contents = def_file.read()

    defs = json_decoder.decode(file_contents)

    return defs




class SCMAutoDocKF(Compound):
    """
        Document the content of the a kf file using the kf_def json files
        Usage example: ".. scmautodockf:: ams"
    """

    has_content               = False
    required_arguments        = 2
    optional_arguments        = 1
    final_argument_whitespace = False

    option_spec = {}

    def run(self):
        node = scmautodoclist()
        node.document = self.state.document
        set_source_info(self, node)

        json_filename = self.arguments[0]
        key           = self.arguments[1]

        all_definitions = load_json_def('kf_def', json_filename)

        defs = {key:all_definitions[key]}

        content = []

        def walk_recursively(d, stack):
            nonlocal content

            for key in sorted(d, key=str.lower):
                value = d[key]
        
                if isinstance(value, dict):

                    if '_hidden' in value and value['_hidden']:
                        continue

                    if len(stack)==0:
                        # Section
                        section_name = key

                        # If the name of the section starts with a '*' , escape it
                        if section_name.startswith('*'):
                            section_name = '\\'+section_name

                        content.append(section_name)
                        content.append(tab+'**Section content:** ' + value['_comment'])
                        content.append('')

                    else:
                        # Variables
                        
                        content.append(tab+literal('%'.join(stack+[key])))
                    
                        for metadata, description, process_content in kf_def_metadata_to_document:
                            if metadata in value:
                                text =  process_content(value[metadata])
                                content.append(2*tab + ':' + description + ': ' + text)
                    
                    stack.append(key)
                    walk_recursively(value, stack)
                    content.append('')
                    stack.pop()

        walk_recursively(defs, [])

        self.content = StringList(content)

        if debug:
            print("=== Generated rst content from SCMAutoDocKF ===\n")
            for line in self.content: print(line)

        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]
