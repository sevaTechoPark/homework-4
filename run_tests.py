#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
from tests.example_test import Tests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(Tests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
