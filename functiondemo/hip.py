import hiyapyco

yaml1 = """resources:
  server_group_1:
    type: OS::Nova::ServerGroup
    properties:
      name: { get_param: [server_groups, 5] }
      policies: [ { get_param: [server_group_types, 5] } ]

  server_group_2:
    type: OS::Nova::ServerGroup
    properties:
      name: { get_param: [server_groups, 8] }
      policies: [ { get_param: [server_group_types, 8] } ]
output:
  check_1:
    description: Name of the instance
    value: { get_attr: [check_1, vname] }"""

yaml2 = """resources:
  server_group_4:
    type: OS::Nova::ServerGroup
    properties:
      name: { get_param: [server_groups, 4] }
      policies: [ { get_param: [server_group_types, 4] } ]

  server_group_9:
    type: OS::Nova::ServerGroup
    properties:
      name: { get_param: [server_groups, 7] }
      policies: [ { get_param: [server_group_types, 7] } ]
output:
  check_6:
    description: Name of the instance
    value: { get_attr: [check_6, vname] }"""

merged_yaml = hiyapyco.load([yaml1, yaml2], method=hiyapyco.METHOD_MERGE)
print(hiyapyco.dump(merged_yaml))

