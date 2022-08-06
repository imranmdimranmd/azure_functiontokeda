from glob import glob
import os
import yaml
cwd = os.getcwd()
 
 
 
def yaml_update(job_name, host_name, path_name,yaml_name):
 
    prom_dict = dict_file ={'job_name': 'system', 'static_configs': [{'targets': ['localhost'], 'labels': {'job': 'varlogs', '__path__': '/var/log/*log', 'host': 'grafana'}}]}
 
    prom_dict['jobname'] = job_name
    prom_dict['static_configs'][0]['labels']['host'] = host_name
    prom_dict['static_configs'][0]['labels']['__path__'] = path_name
 
    with open(yaml_name,'r') as yamlfile:
        cur_yaml = yaml.safe_load(yamlfile) # Note the safe_load
        cur_yaml['scrape_configs'].update(prom_dict)
 
    if cur_yaml:
        with open(yaml_name,'w') as yamlfile:
            yaml.safe_dump(cur_yaml, yamlfile) # Also note the safe_dump
 
    print(prom_dict)
     
 
 
def listdirs(rootdir):
    yaml_name = cwd + '\promtail\promtail-local-config.yaml'
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
 
            #path mame
            path_name = d
 
            #hostname extract 
            pos = d.rfind("@")
            host_name= d[pos+1:]
            print(host_name)
             
            #job name extract
            pos = d.rfind("\\")
            job_name= d[pos+1:]
            print(job_name)
 
            #append yaml
            yaml_update(job_name, host_name, path_name,cp.yaml)
 
 
            #print(d)
            listdirs(d)
  
 
listdirs(cwd)
