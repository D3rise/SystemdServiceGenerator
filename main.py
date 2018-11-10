import os, sys

def prompt_sudo():
    try:
        os.mkdir('/test')
        os.rmdir('/test')
    except PermissionError as err:
        print('You need root permission to generate the service!')
        sys.exit(1)

prompt_sudo()

name = input('Enter name for service: ')
type = input('Enter type for service (Press Enter for default): ')
description = input('Enter description for service: ')
startOperation = input('Enter service start command: ')
stopOperation = input('Enter service stop command (Press Enter for none): ')


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
