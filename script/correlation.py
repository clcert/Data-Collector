import csv

zmap_files = [('port 22', 'port-22.csv'), ('port 25', 'port-25.csv'), ('port 80', 'port-80.csv'),
              ('port 110', 'port-110.csv'), ('port 143', 'port-143.csv'), ('port 443', 'port-443.csv'),
              ('port 465', 'port-465.csv'), ('port 993', 'port-993.csv'), ('port 995', 'port-995.csv'),
              ('port 1080', 'port-1080.csv'), ('port 2745', 'port-2745.csv'), ('port 3127', 'port-3127.csv'),
              ('port 4444', 'port-4444.csv'), ('port 5500', 'port-5500.csv'), ('port 5554', 'port-5554.csv'),
              ('port 5800', 'port-5800.csv'), ('port 5900', 'port-5900.csv'), ('port 8000', 'port-8000.csv'),
              ('port 8080', 'port-8080.csv'), ('port 8866', 'port-8866.csv'), ('port 9898', 'port-9898.csv'),
              ('port 9988', 'port-9988.csv'), ('port 12345', 'port-12345.csv'), ('port 27374', 'port-27374.csv'),
              ('port 31337', 'port-31337.csv')]

dict_fields = ['port 22', 'port 25', 'port 80', 'port 110', 'port 143', 'port 443', 'port 465', 'port 993', 'port 995',
               'port 1080', 'port 2745', 'port 3127', 'port 4444', 'port 5500', 'port 5554', 'port 5800', 'port 5900',
               'port 8000', 'port 8080', 'port 8866', 'port 9898', 'port 9988', 'port 12345', 'port 27374',
               'port 31337']

output = open('correlation.csv', 'wb')
data = dict()

for prop, file_name in zmap_files:
    input = open('data/' + file_name, 'r')

    for line in input:
        if line not in data:
            data[line] = dict.fromkeys(dict_fields, 0)

        data[line][prop] = 1

writer = csv.DictWriter(output, dict_fields)
writer.writeheader()

for i in data.keys():
    writer.writerow(data[i])
