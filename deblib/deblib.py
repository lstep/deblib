# -*- coding: latin-1 -*-
"""
Copyright (C) 2006 Adelux <contact@adelux.fr>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
import sys,os.path,re, operator

def check_debian_version():
    """ Tests if we are on a debian, and if yes, returns the release name """
    table = {'3.1': 'sarge', '3.0': 'woody', '2.2':'potato'}
    try:
        value = file('/etc/debian_version').read().strip()
        return table.get(value, None)
    except IOError:
        return False

class DebPackages:
    def __init__(self, status_file=None):
        self.path_to_status = status_file or '/var/lib/dpkg/status'
        self.packages = {}
        self.debianVersion = check_debian_version()
        if not self.debianVersion:
            raise 'Exception', 'Not on a Debian System'
        self.rebuild_package_list()

    def rebuild_package_list(self):
        """ """
        fd = open(self.path_to_status,'r')
        data = fd.read()
        fd.close()
        self._parse_debian_packages(data)

    def _parse_debian_packages(self, data):
        regexp = re.compile(r"""^Package: (?P<name>[a-zA-Z0-9+.\-_]+)\nStatus: (?P<status>[^\n]+).*?Version: (?P<version>[^\n]+).*?Description:(?P<description>[^\n]+)""", re.MULTILINE+re.DOTALL)
        packages = regexp.finditer(data)
        for package in packages:
            # Only get the installed ones
            status = package.group('status').split()
            if 'installed' in status:
                self.packages[package.group('name')] = {'name':package.group('name'),
                                                        'version': package.group('version'),
                                                        'status': status,
                                                        'description': package.group('description'),
                                                        }

    ####################
    def is_installed(self, package):
        """ Utiliser re.sub / regexp si on veut extraire differemment <=, >= """
        tbl = {'<': operator.lt, '>': operator.gt, '=': operator.eq, }
        op = tbl.get(package[0], None)
        if op:
           package = package[1:]
           package,version = package.split('_',1)

        pac = self.packages.get(package, None)
        if pac:
           if op:
              # We need to test the version too
              # Cleanup the version
              v = pac['version']
              if ':' in v:
                  v = v.split(':')[-1]
              return op(v, version)
           return True
        return False

    def find_package(self, package):
        """ Finds package """
        if self.packages.has_key(package):
            return self.packages[package]['version']
        else:
            return False

    def find_package_like(self, package_substring):
        """ Finds package approximately """
        for package in self.packages.keys():
            if package_substring in package:
                yield (package,self.packages[package]['version'])


if __name__ == '__main__':
    s = DebPackages()
    for p in s.find_package_like('util'):
        print p
