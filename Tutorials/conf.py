# -*- coding: utf-8 -*-

from global_conf import *
project, htmlhelp_basename, latex_documents = set_project_specific_var ('Tutorials')
rst_prolog += init_gui_icons()

html_logo = 'Images/logo.png'

rst_prolog +="""
.. |adf-logo| image:: /Images/ModulesLogos/icon-adf-compact.svg
    :width: 100px
    :target: https://www.scm.com/product/adf/

.. |band-logo| image:: /Images/ModulesLogos/icon-band-compact.svg
    :width: 125px
    :target: https://www.scm.com/product/band/

.. |dftb-logo| image:: /Images/ModulesLogos/icon-dftb-compact.svg
    :width: 120px
    :target: https://www.scm.com/product/dftb/

.. |reaxff-logo| image:: /Images/ModulesLogos/icon-reaxff-compact.svg
    :width: 140px
    :target: https://www.scm.com/product/dftb/

.. |amsdriver-logo| image:: /Images/ModulesLogos/icon-ams-driver-compact.svg
    :width: 110px
    :target: https://www.scm.com/product/ams/

"""