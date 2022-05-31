# ----------------------------------------------------------------------------------------------
# The purpose of this script will be to read in a txt file with objects from an ASA
# and parse through that file to create a CSV file that can be loaded into an FMC for
# bulk importation of objects. This is required because the FMC conversion tool is hot garbage.
# ---------------------------------------------------------------------------------------------

import netaddr
import csv

# Header required by the FMC to import objects
header = ['NAME', 'DESCRIPTION', 'TYPE', 'VALUE', 'LOOKUP']
output = []

# Get the files from the user
txtfile = input(r"Please enter the name of the text file you would like to convert:")
csvfile = input(r"Please enter the name of the csv file you like to receive:")

# Open txt file that will be used to add data to CSV
with open(txtfile, 'r') as f:
    ol = f.readlines()
    nl = []
    prefix = 'object'

    # Removes new line character from list objects
    for i in ol:
        nl.append(i.replace("\n", ""))

    # Combines objects to make easier to work with
    for item in nl:
        if item.startswith(prefix) or not output:
            output.append(item)
        else:
            output[-1] += item

    # Splits each object into it's own list
    testlist = []
    for x in output:
        y = x.split(" ")
        testlist.append(y)

print(testlist)
with open(csvfile, 'w') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()

    x = ['', '', '', '', ''] # List which will rearrange values

    for i in testlist:
        x[0] = i[2]

        # Check if object is subnet and convert type to network and netmask to CIDR
        if i[3] == 'subnet':
            string = i[4] + '/' + str(netaddr.IPAddress(i[5]).netmask_bits())
            i[3] = 'network'
            x[3] = string
            x[2] = i[3]

        # Check if object is host
        if i[3] == 'host':
            x[3] = i[4]
            x[2] = i[3]

        if i[3] == 'fqdn':
            x[3] = i[4]
            x[2] = i[3]

        for y in i:
            if y == 'description':
                x[1] = ' '.join(i[i.index('description')+1:])
        print(x)

        for item in x:
            f.write(item + ',')
        f.write('\n')
        x[1] = ''







