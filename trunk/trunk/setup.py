from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

import deblib

setup(name="DebLib",
      version=deblib.__version__,
      author = "Adelux",
      author_email = "contact+deblib@adelux.fr",
      download_url = "http://www.adelux.fr/projects/dsadeb/download",
      license = "GPL",
      keywords = "debian deb linux",
      description = "A small package",
      long_description = """
This is a really cool package...
blah blah blah, to complete.""",

      url = "http://www.adelux.fr/projects/dsadeb/deblib.html",
      zip_safe = False,
      #install_requires=['Paper>=1.0', 'UPSCode'],
      packages = find_packages(exclude=['tests','ez_setup']),
      package_data = {
        # Include all that is in data/
        'deblib' : ['data/*.txt'],
      },

      classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],

      test_suite = "nose.collector",
      )
