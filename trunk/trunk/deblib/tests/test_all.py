import os
import unittest

from deblib import deblib

def mydebian_version():
    return 'sarge'


class MyFirstTestCase(unittest.TestCase):
    def setUp(self):
        # Cheat to make it believe we're on a Debian system
        deblib.check_debian_version = mydebian_version
        # If use of trial, instead of nose
        if "_trial_temp" in os.getcwd():
            status_file = '../deblib/tests/status'
        else:
            status_file='deblib/tests/status'
        self.p = deblib.DebPackages(status_file)

    def tearDown(self):
        del self.p

    def testNumPackages(self):
        """ Verifies that the init has read the packages list correctly """
        self.failUnless(len(self.p.packages) == 205)

    def testIsInstalled(self):
        """ Tests the method is_installed """
        result = self.p.is_installed('python')
        self.failUnless(result == True)

    def testIsInstalledOperators(self):
        """ Tests the <,>,= operators of is_installed """
        result = self.p.is_installed('>python_2.0.0')
        assert result is True
        result = self.p.is_installed('<python_3.0.0')
        assert result is True
        result = self.p.is_installed('=python_2.3.5')
        assert result is False
        result = self.p.is_installed('=python_2.3.5-2')
        assert result is True
        #result = self.p.is_installed('<=python_2.3.5')
        #assert result is False

    def testFindPackageLike(self):
        """ Tests the method find_package_like """
        result = self.p.find_package_like('util')
        result = list(result)
        assert len(result) == 10


def main():
    unittest.main()

if __name__ == '__main__':
    main()
