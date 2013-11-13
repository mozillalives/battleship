#!/usr/bin/python
import optparse
import sys
try:
    import unittest as unittest2
except ImportError:
    print "You're missing the unittest2 module"
    print "on a linux system, this should be just"
    print "`sudo apt-get install python-setuptools`"
    print "`sudo easy_install unittest2`"
    sys.exit(1)

USAGE = """%prog SDK_PATH TEST_PATH
Run unit tests for App Engine apps.

SDK_PATH    Path to the sdk installation
TEST_PATH   Path to the package containing test modules"""

def main(sdk_path, test_path):
    sys.path.insert(0, sdk_path)
    import dev_appserver
    dev_appserver.fix_sys_path()
    suite = unittest2.loader.TestLoader().discover(test_path)
    unittest2.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    if len(args) != 2:
        print "Error: exactly 2 arguments required"
        parser.print_help()
        sys.exit(1)

    main(args[0], args[1])
