Git / Python version extraction
===============================

.. contents::

This package replaces manual versioning by extracting Git information via ``git describe``, store it in a Python source file and have it read wherever you need the version info.

 The idea is to *first* tag your code in Git, and once everything is checked in, run this script. The script will create/update store the version modify a file that your application will need once deployed. That file should normally not be versioned itself (ie it should be *gitignored*), but be produced by build scripts that will call this script at packaging time.

The generated version file looks something similar to this:

.. code-block:: python

    # source: https://packaging.python.org/guides/single-sourcing-package-version/
    # WARNING: this file is generated from script

    __version__ = "0.4.3"
    __branch__ = "alex/git-version"

Creating/updating the version file
----------------------------------

To create or rewrite the file, run ``update_version_info <file>``

.. code-block:: bash

    update_version_info myproject/version.py


Use
---

To use the version info, include (rather than import) that file:

.. code-block:: python

    exec(open("myproject/version.py").read())
    # ...
    print('version='+__version__)


Installation
------------

.. code-block:: bash

    pip install git+https://github.com/axd1967/pygit-version.git#egg=pygitversion
