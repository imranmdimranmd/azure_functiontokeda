import sys
from pathlib import Path
import ruamel.yaml

file_name = Path('input.yaml')

record_to_add = dict(name='Lisa', email='lisa@test.com', numbers=['000-111-2222', '000-111-2223'])

yaml = ruamel.yaml.YAML()
yaml.explicit_start = True
data = yaml.load(file_name)
data['002'] = record_to_add
yaml.dump(data, sys.stdout)
