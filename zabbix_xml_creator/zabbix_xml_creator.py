#TODO implement command line option display

def load_hosts(path='resource/hosts.csv'):
    def _create_hash(cols, values):
        result={}
        for i, c in enumerate(cols):
            result[c.strip()]=values[i].strip()
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
        results.append(_create_hash(header, r))
    print results
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
  print replace_xml(hosts=load_hosts())

if __name__ == '__main__':
    main()

