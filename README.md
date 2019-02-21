# hello-workbench

Example Workbench module for new developers.

# Getting Started

* Set up a
  [Workbench development environment](https://github.com/CJWorkbench/cjworkbench/wiki/Setting-up-a-development-environment)
* Clone this repository into a _sibling_ directory. For example, if Workbench
  is in `~/src/cjworkbench/cjworkbench`, clone this repository into
  `~/src/cjworkbench/hello-workbench`
* Start Workbench in the Workbench directory: `bin/dev start`
* Watch this module from the Workbench directory:
  `bin/dev develop-module hello-workbench`. Every time files change, this will
  re-import your module.
* Browse to your local Workbench at
  [http://localhost:8000](http://localhost:8000) to try out your module.
* Edit this module. Refresh in Workbench to see your edits.

# Developing

1. Add tests to ``test_module.py``
2. Run ``python3 test_module.py`` to find errors
3. Edit code in ``module.py``
4. Push to GitHub

For lots more information, see the
[module development documentation](https://github.com/CJWorkbench/cjworkbench/wiki/Creating-A-Module).
