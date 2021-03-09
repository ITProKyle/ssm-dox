#######
ssm-dox
#######

CLI tool for building and publishing SSM Documents.


************
What Is Dox?
************

**Dox** is a directory containing the source code of an SSM document.
Named for it's corresponding SSM Document, the directory contains the following:

- ``template.yaml`` or ``template.yml`` file **[REQUIRED]**
- ``README.md`` file describing the SSM Document
- external files to be included in the SSM Document (e.g. shell or PowerShell scripts)


************
Why Use Dox?
************

Using **Dox** to write an SSM Document allows for scripts and other items to be linted and tested outside of the SSM Document.
This enables CI/CD pipelines to easily validate the code before it gets deployed to AWS.


.. toctree::
  :caption: Dox
  :maxdepth: 2
  :glob:
  :hidden:

  dox/*


.. toctree::
  :caption: CLI
  :maxdepth: 2
  :glob:
  :hidden:

  cli/*


.. toctree::
  :caption: Developers Guide
  :maxdepth: 2
  :glob:
  :hidden:

  developers/*
