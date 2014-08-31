def load_hosts(path='resource/hosts.csv'):
    pass

def replace_xml(path='resource', hosts=[{'name':'hogehoge'},{'name':'hogehoge2'}] ):
    from jinja2 import Environment
    from jinja2.loaders import FileSystemLoader

    env = Environment(loader=FileSystemLoader(path))
    tmpl = env.get_template('base_zabbix_jinja2.xml')
    print tmpl.render(hosts=hosts)

def main():
  replace_xml()

if __name__ == '__main__':
    main()

