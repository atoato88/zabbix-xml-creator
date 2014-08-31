zabbix-xml-creator
==================

## requires

### Jinja2

- git clone with command
<pre>
git clone https://github.com/mitsuhiko/jinja2.git
</pre>
- install module with command
<pre>
sudo -i
python setup.py install
</pre>

## prerequisite

### resource/hosts.csv file format

It assumes that created by Microsoft Excel in csv-format.  
If value has comma','  it is covered with double-quote.  
> 1,"some,thing",2,3,4,.....  

And, it has no space' ' at between value and value.  

- bad-pattern    
> 1, 2, 3, 4, .....  
- good-pattern  
> 1,2,3,4,.....  
  
First line in this file is used at column header.  


