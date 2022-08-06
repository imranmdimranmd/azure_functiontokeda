import ruamel.yaml
yaml = ruamel.yaml.YAML()
#Load the yaml files
with open('test1.yaml') as fp:
    data = yaml.load(fp)
with open('test2.yaml') as fp:
    data1 = yaml.load(fp)
#Add the resources from test2.yaml to test1.yaml resources
for i in data1['resources']:
    print (i,data1['resources'][i])
    data['resources'].update({i:data1['resources'][i]})
#create a new file with merged yaml
yaml.dump(data,file('/tmp/lal.yaml', 'w'))
