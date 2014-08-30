import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../zabbix_xml_creator'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import zabbix_xml_creator
import unittest

class TestZabbixXMLCreator(unittest.TestCase):

    def setUp(self):
        pass

    def test_exactly_true(self):
        self.assertEquals(True, True, "test pass")

    def test_xml_part_read(self):
        zabbix_xml_creator.get_root_from_file("sub_host_define.xml")

    def test_xml_base_read(self):
        zabbix_xml_creator.get_root_from_file("base_zabbix_xml.xml")

    def test_insert_sub_to_base(self):
        self.assertEqual(2, 2, 'shuould be count for host is 2')


if __name__ == '__main__':
    unittest.main()


