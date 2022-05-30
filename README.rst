=========
 mavconn
=========

An asynchronous MAVLink connection library with separate send/receive threads.

|ci| |wheels| |release| |badge|

|cov| |pylint|

|tag| |license| |python|



.. note:: This project uses versioningit_ to generate and maintain the
          version file, which only gets included in the sdist/wheel
          packages. In a fresh clone, running any of the tox_ commands
          should generate the current version file.

.. _versioningit: https://github.com/jwodder/versioningit
.. _tox: https://github.com/tox-dev/tox


Dev tools
=========

Local tool dependencies to aid in development; install for maximum enjoyment.

Tox
---

As long as you have git and at least Python 3.6, then you can install
and use `tox`_.  After cloning the repository, you can run the repo
checks with the ``tox`` command.  It will build a virtual python
environment for each installed version of python with all the python
dependencies and run the specified commands, eg:

::

  $ git clone https://github.com/VCTLabs/mavconn
  $ cd mavconn/
  $ tox -e py

The above will run the default test commands using the (local) default
Python version.  To specify the Python version and host OS type, run
something like::

  $ tox -e py39-linux

To build and check the Python package, run::

  $ tox -e deploy,check

Full list of additional ``tox`` commands:

* ``tox -e deploy`` will build the python packages and run package checks
* ``tox -e check`` will install the wheel package from above
* ``tox -e lint`` will run ``pylint`` (somewhat less permissive than PEP8/flake8 checks)
* ``tox -e mypy`` will run mypy import and type checking
* ``tox -e style`` will run flake8 style checks

To build/lint the api docs, use the following tox commands:

* ``tox -e docs`` will build the documentation using sphinx and the api-doc plugin
* ``tox -e docs-lint`` will the sphinx link checking


.. |ci| image:: https://github.com/VCTLabs/mavconn/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/VCTLabs/mavconn/actions/workflows/ci.yml
    :alt: CI Status

.. |wheels| image:: https://github.com/VCTLabs/mavconn/actions/workflows/wheels.yml/badge.svg
    :target: https://github.com/VCTLabs/mavconn/actions/workflows/wheels.yml
    :alt: Wheel Status

.. |badge| image:: https://github.com/VCTLabs/mavconn/actions/workflows/pylint.yml/badge.svg
    :target: https://github.com/VCTLabs/mavconn/actions/workflows/pylint.yml
    :alt: Pylint Status

.. |release| image:: https://github.com/VCTLabs/mavconn/actions/workflows/release.yml/badge.svg
    :target: https://github.com/VCTLabs/mavconn/actions/workflows/release.yml
    :alt: Release Status

.. |cov| image:: https://raw.githubusercontent.com/VCTLabs/mavconn/badges/master/test-coverage.svg
    :target: https://github.com/VCTLabs/mavconn/
    :alt: Test coverage

.. |pylint| image:: https://raw.githubusercontent.com/VCTLabs/mavconn/badges/master/pylint-score.svg
    :target: https://github.com/VCTLabs/mavconn/actions/workflows/pylint.yml
    :alt: Pylint score

.. |license| image:: https://img.shields.io/github/license/VCTLabs/mavconn
    :target: https://github.com/VCTLabs/mavconn/blob/master/LICENSE
    :alt: License

.. |tag| image:: https://img.shields.io/github/v/tag/VCTLabs/mavconn?color=green&include_prereleases&label=latest%20release
    :target: https://github.com/VCTLabs/mavconn/releases
    :alt: GitHub tag

.. |python| image:: https://img.shields.io/badge/python-3.6+-blue.svg
    :target: https://www.python.org/downloads/
    :alt: Python
