import os
import sys
import argparse

def prompt_sudo():
    try:
        os.mkdir('/test')
        os.rmdir('/test')
    except PermissionError:
        print('You need root permission to generate the service!')
        sys.exit(1)

prompt_sudo()

parser = argparse.ArgumentParser()

parser.add_argument("--name", help="Name of the service")
parser.add_argument("--type", help="Type of the service")
parser.add_argument("--desc", help="Description of the service")
parser.add_argument("--start", help="Start cmd of the service")
parser.add_argument("--stop", help="Stop cmd of the service")

args = parser.parse_args(sys.argv[1:])

name = args.name or input('Enter name for service: ')
type = args.type or input('Enter type for service (Press Enter for default): ')
description = args.desc or input('Enter description for service: ')
startOperation = args.start or input('Enter service start command: ')
stopOperation = args.stop or input('Enter service stop command (Press Enter for none): ')


if type is '' or None:
    type = 'simple'


if stopOperation:
    stopOperation = 'ExecStop=%s' % stopOperation


with open(f'/etc/systemd/system/{name}.service', 'w') as f:
    try:
        f.write("""
        [Unit]
        Description=%s
        After=multi-user.target

        [Service]
        Type=%s
        ExecStart=%s
        %s

        [Install]
        WantedBy=multi-user.target
        """ % (description, type, startOperation, stopOperation))
    
    except IOError as err:
        print(f'An Input/Output error happened!\n{err}')

cmd = f'sudo systemctl enable {name}'
print(f'To enable the service, type: {cmd}')
