#!/usr/bin/env python3

import importlib
import unittest

try:
    from mainutils import module_parent, disable_requests_warnings
except ImportError:
    from .mainutils import module_parent, disable_requests_warnings



class MainutilsTest(unittest.TestCase):
    def test_module_import(self):
        global __package__
        __package__ = module_parent()
        importlib.import_module(__package__)

    def test_disable_requests_warnings(self):
        disable_requests_warnings()


if __name__ == '__main__':
    unittest.main()
