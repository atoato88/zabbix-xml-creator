def load_hosts(path='resource/hosts.csv'):
    def _create_hash(cols, values):
        result={}
        for i, c in enumerate(cols):
            result[c.strip()]=values[i].strip()
        return result
    import csv
    reader = csv.reader(open(path, 'r'))
    results = []
    columns = []
    header = reader.next()
    for r in reader:
        results.append(_create_hash(header, r))
    print results
    return results

def replace_xml(path='resource', hosts=[] ):
    from jinja2 import Environment
    from jinja2.loaders import FileSystemLoader

    env = Environment(loader=FileSystemLoader(path))
    tmpl = env.get_template('base_zabbix_jinja2.xml')
    print tmpl.render(hosts=hosts)

def main():
  replace_xml(hosts=load_hosts())

if __name__ == '__main__':
    main()

