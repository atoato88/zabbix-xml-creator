
def parse_command():
  from optparse import OptionParser, OptionValueError
  usage = "usage: %prog [options]"
  parser = OptionParser(usage)

  parser.add_option(
        "-t", "--target",
        action="store",
        type="string",
        dest="hosts_file",
        help="target file(csv format) path for zabbix hosts.",
        default="resource/hosts.csv")
  
  parser.add_option(
        "-b", "--base",
        action="store",
        type="string",
        dest="base_template_file",
        help="base xml template file for zabbix import.",
        default="resource/base_zabbix_jinja2.xml")

  (options, args) = parser.parse_args()
  return (options, args)

def load_hosts(path='resource/hosts.csv'):
    def _create_hash(cols, values):
        result={}
        for i, c in enumerate(cols):
            result[c.strip()]=values[i].decode('utf-8').strip()
        return result
    import csv
    results = []
    columns = []
    try:
        reader = csv.reader(open(path, 'r'))
    except BaseException as e:
        print e
        return results
    header = reader.next()
    for r in reader:
        print r
        results.append(_create_hash(header, r))
    return results

def replace_xml(path='resource/base_zabbix_jinja2.xml', hosts=[]):
    from jinja2 import Environment
    from jinja2.loaders import FileSystemLoader
    import os.path

    dirname = os.path.dirname(path)
    filename = os.path.basename(path)

    env = Environment(loader=FileSystemLoader(dirname))
    tmpl = env.get_template(filename)
    return tmpl.render(hosts=hosts)

def main():
  (options, args) = parse_command()
  hosts = load_hosts(path=options.hosts_file) if not \
        options.hosts_file else load_hosts()
  output = replace_xml(path=options.base_template_file, hosts=hosts) if not \
        options.base_template_file else replace_xml(hosts=hosts)
  print output

if __name__ == '__main__':
    main()

