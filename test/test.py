import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../zabbix_xml_creator'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import zabbix_xml_creator
import tempfile
import unittest

class TestZabbixXMLCreator(unittest.TestCase):

    def setUp(self):
        pass

    def test_exactly_true(self):
        self.assertEquals(True, True)

    def test_load_hosts_no_such_file(self):
        r = zabbix_xml_creator.load_hosts('/no_such_file')
        self.assertEquals([], r)

    def test_load_hosts_default_file(self):
        r = zabbix_xml_creator.load_hosts()
        self.assertNotEqual([], r)

    def test_load_hosts_tmp_file(self):
        e = [{'a':'1','b':'2','c':'3','d':'4','e':'5'}]
        t = tempfile.NamedTemporaryFile('w')
        t.write("""a,b,c,d,e
            1,2,3,4,5""")
        t.flush()
        r = zabbix_xml_creator.load_hosts(t.name)
        t.close()
        self.assertEqual(e, r)

    def test_load_hosts_tmp_file2(self):
        e = [{'a':'1','b':'2','c':'3','d':'4','e':'5'},{'a':'11','b':'22','c':'33','d':'44','e':'55'}]
        t = tempfile.NamedTemporaryFile('w')
        t.write("""a,b,c,d,e
            1,2,3,4,5
            11,22,33,44,55""")
        t.flush()
        r = zabbix_xml_creator.load_hosts(t.name)
        t.close()
        self.assertEqual(e, r)

    def test_replace_xml_no_hosts(self):
        e = \
"""<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
  <version>2.0</version>
  <date>2014-04-19T14:20:50Z</date>
  <groups>
    <group>
      <name>STD_nova-compute</name>
    </group>
  </groups>
  <hosts>
  </hosts>
</zabbix_export>"""
        r = zabbix_xml_creator.replace_xml(hosts=[])
        self.assertEquals(e, r)

    def test_replace_xml_one_hosts(self):
        e = \
"""<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
  <version>2.0</version>
  <date>2014-04-19T14:20:50Z</date>
  <groups>
    <group>
      <name>STD_nova-compute</name>
    </group>
  </groups>
  <hosts>
    <host>
      <host>first</host>
      <name>fist-machine</name>
      <proxy />
      <status>0</status>
      <ipmi_authtype>-1</ipmi_authtype>
      <ipmi_privilege>2</ipmi_privilege>
      <ipmi_username />
      <ipmi_password />
      <templates>
        <template>
          <name>STD_Linux_General</name>
        </template>
        <template>
          <name>STD_nova-compute</name>
        </template>
      </templates>
      <groups>
        <group>
          <name>STD_nova-compute</name>
        </group>
      </groups>
      <interfaces>
        <interface>
          <default>1</default>
          <type>2</type>
          <useip>1</useip>
          <ip>172.16.0.1</ip>
          <dns />
          <port>7777</port>
          <interface_ref>if2</interface_ref>
        </interface>
        <interface>
          <default>1</default>
          <type>1</type>
          <useip>1</useip>
          <ip>192.168.1.1</ip>
          <dns />
          <port>10051</port>
          <interface_ref>if1</interface_ref>
        </interface>
      </interfaces>
      <applications />
      <items />
      <discovery_rules />
      <macros />
      <inventory />
    </host>
  </hosts>
</zabbix_export>"""
        r = zabbix_xml_creator.replace_xml(hosts=[{'display_name': 'fist-machine', 'name': 'first', \
            'ip2': '172.16.0.1', 'ip1': '192.168.1.1', 'port2': '7777', 'port1': '10051'}])
        self.assertEquals(e, r)

if __name__ == '__main__':
    unittest.main()




