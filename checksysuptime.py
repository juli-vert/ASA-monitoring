'''Check System Uptime
Usage command [argv1]
argv1 = snmp host'''

#!/usr/bin/python3
import os,sys,re

hostip = sys.argv[1]

comm = '{0} {1} {2}'.format("snmpwalk -c private -v2c",hostip,"-s0 1.3.6.1.2.1.1.3.0")
aux = os.popen(comm,'r')
peer = aux.readline().rstrip('\n')
ind = re.search('\((.+?)\)',peer).group(1)
print (ind)
print (str(int(int(ind)/8640000)))

