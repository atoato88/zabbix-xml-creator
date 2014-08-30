from xml.etree.ElementTree import *
from os import path

output_tree = None
hosts_tag = None

def get_root_from_file(file_name):
    root = parse( path.join( path.dirname( __file__ ), '..', 'resource', file_name) ) 
    return root.getroot()

def insert_sub_into_base_root(base_root, sub_root):
    global output_tree
    global hosts_tag

    #find 'hosts' tag

    if hosts_tag is None:
        hosts_tag = base_root.find('.//hosts')

    hosts_tag.insert(0, sub_root)

    set_output_tree(ElementTree(base_root))

def get_output_tree():
    global output_tree
    return output_tree

def set_output_tree(tree):
    global output_tree
    output_tree = tree

def write_output_xml(file_name='generated_zabbix_import.xml'):
    output_tree.write(file_name)

def main():
  print 'zabbix-xml-creator: start process'
  sub_root = get_root_from_file('sub_host_define.xml')
  base_root = get_root_from_file('base_zabbix_xml.xml')
  #load host define info

  #replace template with real value in sub host define.

  #insert sub host define into base zabbix xml.
  insert_sub_into_base_root(base_root, sub_root)

  #write xml file.
  write_output_xml()
  print 'zabbix-xml-creator: finish process'

if __name__ == '__main__':
    main()

