Git / Python version extraction
===============================

This package replaces manual versioning by extracting Git information via ``git describe`` and storing it in a Python source file. The idea is to *first* tag your code in Git, and once everthing is checked in, run this script. It will modify a file that your application will need once deployed. That file should normally not be versioned itself, but be produced by build scripts.

It looks something similar to this:

.. code-block:: python

    # source: https://packaging.python.org/guides/single-sourcing-package-version/
    # WARNING: this file is generated from script

    __version__ = "0.4.3"
    __branch__ = "alex/git-version"

Then you can use it where needed by including (rather than importing) that file as following

.. code-block:: python

    exec(open("premieaanvragen/version.py").read())
    # ...
    print('version='+__version__)


To create or rewrite the file, run ``update_version_info <file>``

.. code-block:: bash

    cd premieaanvragen
    update_version_info premieaanvragen/version.py
