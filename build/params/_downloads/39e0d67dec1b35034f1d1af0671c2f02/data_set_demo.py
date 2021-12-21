#!/usr/bin/env amspython
# coding: utf-8

# ### Add an entry

from scm.params import *
import numpy as np
data_set = DataSet()
data_set.add_entry("angle('H2O', 0, 1, 2)", weight=0.333)


# To **access the last added element**, use ``data_set[-1]``

print("String representation of data_set[-1]")
print(data_set[-1])
print("Type: {}".format(type(data_set[-1])))


# You can also **change it after you've added it**:

data_set[-1].sigma = 3.0
print(data_set[-1])


# We recommend to always specify the *reference value*, the *unit*, and the *sigma* value when adding an entry, and also to specify any meaningful *metadata* about the data set entry.

data_set.add_entry("energy('H2O')-0.5*energy('O2')-energy('H2')", 
                  weight=2.0, 
                  reference=-241.8, 
                  unit=('kJ/mol', 2625.15), 
                  sigma=10.0,
                  metadata={
                      'Source': 'NIST Chemistry WebBook',
                      'Description': 'Hydrogen combustion (gasphase) per mol H2'
                  })
print(data_set[-1])


# All *expressions* in a single DataSet **must be unique**:

try:
    data_set.add_entry("energy('H2O')-0.5*energy('O2')-energy('H2')", weight=2.0)
except Exception as e:
    print("Caught the following exception: {}".format(e))


# The **reference values can also be numpy arrays**, for example when extracting forces or charges:

forces = np.array([[ 0.0614444 , -0.11830478,  0.03707212],
                  [-0.05000567,  0.09744271, -0.03291899],
                  [-0.01143873,  0.02086207, -0.00415313]])
data_set.add_entry("forces('distorted_H2O')",
                  weight=1.0,
                  reference=forces,
                  metadata={'Source': 'Calculated_with_DFT'})
print(data_set[-1])


# ### DataSetEntry attributes

# A DataSetEntry has the following attributes:
# 
# * **expression** : str
# * **weight** : float or numpy array
# * **unit** : 2-tuple (str, float)
# * **reference** : float or numpy array
# * **sigma** : float
# * **jobids** : set of str (read-only). The job ids that appear in the expression.
# * **extractors** : set of str (read-only). The extractors that appear in the expression.

print(data_set[-2].expression)
print(data_set[-2].weight)
print(data_set[-2].unit)
print(data_set[-2].reference)
print(data_set[-2].sigma)


print(data_set[-2].jobids)


print(data_set[-2].extractors)


# ### Accessing the DataSet entries

# Above, `data_set[-1]` was used to access the last added element, and `data_set[-2]` to access the second to last added element. More generally, the DataSet can be **indexed either as a** `list` **or as a** `dict`:

print(data_set[0].expression)
print(data_set[1].expression)
print(data_set[1].reference)
print(data_set["energy('H2O')-0.5*energy('O2')-energy('H2')"].reference)


# **Get the number of entries** in the DataSet with ``len()``:

print(len(data_set))


print(data_set.get('expression'))
print(data_set.keys())


print(data_set.get('weight'))
print(data_set.get('extractors'))


# **Loop over DataSet entries**:

for ds_entry in data_set:
    print(ds_entry.expression)


for expr in data_set.get('expression'):
    print(expr)


# Use the **DataSet.index()** method to get the index of a DataSetEntry:

ds_entry = data_set["energy('H2O')-0.5*energy('O2')-energy('H2')"]
print(data_set.index(ds_entry))


print(data_set[1].expression)


# ### Delete a DataSet entry 
# 
# **Remove** an entry with ``del``:

data_set.add_entry("energy('some_job')", weight=1.0)
print(len(data_set))
print(data_set[-1].expression)
del data_set[-1] # or del data_set["energy('some_job')"]
print(len(data_set))
print(data_set[-1].expression)


# ``del`` can also be used to delete multiple entries at once, as in ``del data_set[0,2]`` to remove the first and third entries.

# ### Split a DataSet into subsets

# **Subset from a list of given expressions**

subset = data_set.from_expressions(["angle('H2O', 0, 1, 2)", 
                                   "energy('H2O')-0.5*energy('O2')-energy('H2')"])
print(subset.keys())


expression = "angle('H2O', 0, 1, 2)"
original_sigma = data_set[expression].sigma
print("For expression {} the original sigma value is: {}".format(expression, original_sigma))

subset[expression].sigma = 1234 # this modifies the entry in the original data_set
print(data_set[expression].sigma)
print(subset[expression].sigma)

# restore the original value, this modifies the subset!
data_set[expression].sigma = original_sigma 
print(data_set[expression].sigma)
print(subset[expression].sigma)


# **To modify a subset without modifying the original DataSet**, you must create a `copy`:

new_subset = subset.copy()
new_subset[expression].sigma = 2345
print(new_subset[expression].sigma)
print(subset[expression].sigma)
print(data_set[expression].sigma)


# **Subset from a list of job ids**

subset = data_set.from_jobids(['H2O', 'O2', 'H2'])
print(subset.keys())


# **Subset from metadata key-value pairs**

subset = data_set.from_metadata('Source', 'NIST Chemistry WebBook')
print(subset)


# You can also match using **regular expressions**:

subset = data_set.from_metadata('Source', '^N[iI]ST\s+Che\w', regex=True)
print(subset.keys())


# **Subset from extractors**

subset = data_set.from_extractors('forces')
print(subset.get('expression'))


# A subset from multiple extractors can be generated by passing a list:

subset = data_set.from_extractors(['angle','forces'])
print(subset.get('expression'))


# **Random subset with N entries**

subset = data_set.random(2, seed=314)
print(subset.keys())


# **Split the data_set into random nonoverlapping subsets**

subset_list = data_set.split(2/3.0, 1/3.0, seed=314)
print(subset_list[0].keys())
print(subset_list[1].keys())


# ### DataSet header
# The header can be used to store comments about a data_set. When storing as a .yaml file, the header is printed as a separate YAML entry at the top of the file.

data_set.header = {'Comment': 'An example data_set', 'Date': '21-May-2001'}
print(data_set)


# ### Save the data set

data_set.store('data_set.yaml')

