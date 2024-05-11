from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command, netmiko_send_config


def runMe(task):
    devices = ['10.10.1.1', '10.10.1.2', '10.10.1.6']
    commands = [
        [
        'router ospf 1',
        'router-id 1.1.1.1',
        'default-information originate',
        'network 10.10.1.0 0.0.0.3 area 0'
        ],
        [
            'router ospf 1',
            'router-id 2.2.2.2',
            'network 10.10.1.0 0.0.0.3 area 0',
            'network 10.10.1.4 0.0.0.3 area 0'
        ],
        [
            'router ospf 1',
            'router-id 3.3.3.3',
            'network 10.10.1.4 0.0.0.3 area 0'
        ]
    ]
    for device, command in zip(devices, commands):
        if device == task.host.hostname:
            task.run(task=netmiko_send_config, config_commands=command)

    
configFile = "C:\\Users\\pc\\Desktop\\python_programmability\\llpyAuto01\\autoPy05\\nornirTutorials\\config.yaml"
connect = InitNornir(config_file=configFile)
result = connect.run(task=runMe)
print_result(result)
