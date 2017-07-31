#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import start_stop_ec2


class ReadFileTestsCase(unittest.TestCase):
    def testReadFile():
        with open('/Users/bodo/credentials.txt', 'r') as f:
            credentials = [line.strip() for line in f]


if __name__ == "__main__":
    unittest.main()
