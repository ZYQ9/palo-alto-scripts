# Script to create CLI commands from text files

txtfile = input('Enter the file you would like to send output to: ')

with open(txtfile, 'w') as output:
    with open('redacted', 'r') as input:
        output.write('======================= ZOOM ======================\n\n')
        for line in input:
            output.write('set address ' + 'ZN-' + line.replace('/','-').strip() + ' ' + 'ip-netmask ' + line)
        output.write('\n')

    with open('redacted', 'r') as input:
        output.write('======================= MS-TEAMS ======================\n\n')
        for line in input:
            output.write('set address ' + 'TN-' + line.replace('/','-').strip() + ' ' + 'ip-netmask ' + line)
        output.write('\n')

    with open('redacted', 'r') as input:
        output.write('======================= RING CENTRAL ======================\n\n')
        for line in input:
            output.write('set address ' + 'RCN-' + line.replace('/','-').strip() + ' ' + 'ip-netmask ' + line)
        output.write('\n')

    with open('redacted', 'r') as input:
        output.write('======================= CISCO WEBEX ======================\n\n')
        for line in input:
            output.write('set address ' + 'CWN-' + line.replace('/','-').strip() + ' ' + 'ip-netmask ' + line)
        output.write('\n')
        output.close()
