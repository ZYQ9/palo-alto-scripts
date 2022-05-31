import csv

with open('cli.txt', 'w') as output_file:
    with open('export_objects_services_05202022_103005edt.csv', 'r') as input_file:
        output_file.write('================== SERVICES =======================================\n')
        for row in csv.reader(input_file):
            output_file.write('set service ' + row[0] + ' ' + 'protocol ' + str(row[2]).lower() + ' ' + 'port ' + row[3] + ' ' + '\n')
        output_file.write('\n')
        output_file.close()

with open('app-group.txt', 'w') as app_output_file:
    with open('export_objects_application_groups_05202022_173139edt.csv', 'r') as app_input_file:
        app_output_file.write('================== APPLICATION GROUPS =======================================\n')
        for row in csv.reader(app_input_file):
            app_output_file.write('set application-group ' + row[0] + ' ' + 'members ' + '[ ' + str(row[3]).replace(';', ' ') + ' ]' + '\n')
        app_output_file.write('\n')

    with open ('export_objects_service_groups_05202022_180907edt.csv', 'r') as ser_input_file:
        app_output_file.write('================== SERVICE GROUPS =======================================\n')
        for row in csv.reader(ser_input_file):
            app_output_file.write('set service-group ' + row[0] + ' ' + 'members ' + '[ ' + str(row[3]).replace(';', ' ') + ' ]' + '\n')
        app_output_file.write('\n')
        app_output_file.close()

print('File created Successfully')