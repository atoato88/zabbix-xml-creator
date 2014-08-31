import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../zabbix_xml_creator'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import zabbix_xml_creator
import unittest
from xml.etree.ElementTree import *

class TestZabbixXMLCreator(unittest.TestCase):

    def setUp(self):
        pass

    def test_exactly_true(self):
        self.assertEquals(True, True)

if __name__ == '__main__':
    unittest.main()




