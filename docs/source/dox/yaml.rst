#########
YAML Tags
#########

ssm-dox uses a custom YAML loader when handling Dox.
This custom loader implements tags that can be used to simplify writing Dox or perform utility functions such as including the contents of an external file.


*************
IncludeScript
*************

This tag accepts the path (absolute or relative) to a file as an argument.
The file is then read and converted into a by splitting at each line break.
The resulting data structure can be passed to ``input.runCommand`` of an *aws:runPowerShellScript* or *aws:runShellScript* mainStep.


.. rubric:: Usage
.. code-block:: yaml

  runCommand: !IncludeScript ./example.sh

.. rubric:: Example
.. code-block:: yaml

  mainSteps:
    - action: aws:runShellScript
      name: Example
      inputs:
        runCommand: !IncludeScript ./example.sh
      ...


----


*********
LinuxOnly
*********

Shorthand for a precondition that restricts to mainStep to only run on Linux systems.

.. rubric:: Usage
.. code-block:: yaml

  precondition: !LinuxOnly

.. rubric:: Example
.. code-block:: yaml

  mainSteps:
    - action: aws:runShellScript
      name: Example
      precondition: !LinuxOnly
      ...


----


***********
WindowsOnly
***********

Shorthand for a precondition that restricts to mainStep to only run on Windows systems.

.. rubric:: Usage
.. code-block:: yaml

  precondition: !WindowsOnly

.. rubric:: Example
.. code-block:: yaml

  mainSteps:
    - action: aws:runShellScript
      name: Example
      precondition: !WindowsOnly
      ...
