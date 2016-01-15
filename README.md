# MetaData Collector #
Conjunto de scripts en python que permiten recuperar metadatos a partir de la información obtenida en etapas anteriores 
del proceso de monitoreo activo. Además contiene scripts de normalización de datos de versiones anteriores del Grabber.

Modo de uso:
```
usage: main.py [-h] -i INPUT [-o OUTPUT] [--port PORT] [--date DATE] [--whois]
               [--dns_reverse] [--http] [--https] [--ssh] [--normalize_http]
               [--normalize_cert] [--validate_cert] [--clean_errors]
               [--zmap_log] [--juniper]

Recollect IP data

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file name
  -o OUTPUT, --output OUTPUT
                        Output file name
  --port PORT           Set the scanned port
  --date DATE           Add the date of scan (input format dd/mm/yyyy)
  --whois               Set whois ip response
  --dns_reverse         Set the machine name
  --http                Parse http info
  --https               Parse https info
  --ssh                 Parse ssh info
  --normalize_http      Normalize old http scans fields
  --normalize_cert      Normalize old certificate scans fields
  --validate_cert       Validate server certificate
  --clean_errors        Clean the lines with only error an ip fields
  --zmap_log            Parse Zmap log
  --juniper             Filter the machine with juniper backdoor
```

## Avisos
La ejecución de los siguientes procedimietos demora varios minutos:
    * whois
    * reverse_dns
    * validate_cert
    
## Documentación
La documentación de cada paquete se encuentra en su interior en formato de un readme
