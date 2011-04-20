#!/usr/bin/env python
"""
pybedtools utility scripts:

"""
import sys

def import_module(name):
    __import__("%s" % (name,), globals(), locals(), [], -1)
    return sys.modules[name]

def script_names(module):
    return [script for script in  module.__all__ if not script[:2] == "__"]


if __name__ == "__main__":

    m = import_module("pybedtools.scripts")
    scripts = script_names(m)
    mods = [import_module("pybedtools.scripts.%s" % s) for s in scripts]

    if (len(sys.argv) != 1 and not sys.argv[1] in scripts) or len(sys.argv) == 1:

        print __doc__.strip() + "\n"
        for name, mod in zip(scripts, mods):
            print " %-12s: %s\n" % (name, mod.main.__doc__.strip())
    else:
         mname = sys.argv.pop(1)
         i = scripts.index(mname)
         module = mods[i]
         module.main()
