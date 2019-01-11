# SystemdServiceGenerator
Systemd simple service generator

To run, use:
`python3 main.py`

Available args:
```
-h, --help     Show the help message amd exit
--name NAME    Name of the service
--type TYPE    Type of the service
--desc DESCRIPTION    Description of the service
--start START  Start cmd of the service
--stop STOP    Stop cmd of the service
```

Example run command:
 `python3 main.py --name SITE --desc webserver --type simple --start /etc/init.d/apache2 start --stop /etc/init.d/apache2 stop`
