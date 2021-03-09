.. _dev-getting-started:

###############
Getting Started
###############

Before getting started, `fork this repo`_ and `clone your fork`_.

.. _fork this repo: https://help.github.com/en/github/getting-started-with-github/fork-a-repo
.. _clone your fork: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository


***********************
Development Environment
***********************

This project uses ``poetry`` to create Python virtual environment.
This must be installed on your system before setting up your dev environment.

With poetry installed, run ``make setup`` to setup your development environment and ``pre-commit``


pre-commit
==========

`pre-commit <https://pre-commit.com/>`__ is configured for this project to help developers follow the coding style.
If you used ``make setup`` to setup your environment, it is already setup for you.
If not, you can run ``make setup-pre-commit`` to to install the pre-commit hooks.

You can also run ``make run-pre-commit`` at any time to manually trigger these hooks.


pyright Type Checking
=====================

This project uses pyright to perform type checking.
To run type checking locally, install pyright (``npm install``) then run ``make lint`` or ``make lint-pyright``.
