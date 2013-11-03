import pkg_resources
import sys

from _nilsimsa import compare_hexdigests


version_file = pkg_resources.resource_filename(__name__, 'VERSION')
with open(version_file) as vf:
    __version__ = vf.read()
del version_file


__all__ = ['compare_hexdigests', '__version__']
