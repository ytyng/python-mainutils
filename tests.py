#!/usr/bin/env python3

import importlib


def test():
    from mainutils import module_parent
    global __package__
    __package__ = module_parent()
    importlib.import_module(__package__)

    from .mainutils import disable_requests_warnings
    disable_requests_warnings()


if __name__ == '__main__':
    test()
