from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

import deblib

setup(name="DebLib",
      version=deblib.__version__,
      author = "Adelux",
      author_email = "luc stepniewski at adelux.fr",
      download_url = "http://code.google.com/p/deblib",
      license = "GPL",
      keywords = "debian deb python packages dpkg",
      description = "Module to easily access/search Debian packages",
      long_description = """
deblib is a simple module for Python that allows you to look at the debian packages database.
For example, it allows you to ask if a specific version of a package exist on the tested system.
deblib has been created to facilitate the development of the dsacheck project.""",

      url = "http://code.google.com/p/deblib",
      zip_safe = True,
      packages = find_packages(exclude=['tests','ez_setup']),
      package_data = {
        # Include all that is in data/
        'deblib' : ['data/*.txt'],
      },

      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],

      test_suite = "nose.collector",
      )
