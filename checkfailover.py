'''Check failover
Usage command [argv1]
argv1 = snmp host'''

#!/usr/bin/python3
import os,sys

hostip = sys.argv[1]

comm = '{0} {1} {2}'.format("snmpwalk -c private -v2c",hostip,"-s0 1.3.6.1.4.1.9.9.147.1.2.1.1.1.2 | grep \"this device\"")
aux = os.popen(comm,'r')
peer = aux.readline().rstrip('\n')
ind = peer.rstrip(" = ").lstrip("iso.3.6.1.4.1.9.9.147").lstrip("2.1.1.1.2")
if "Primary" in peer:
    status = "primary"
elif "Secondary" in peer:
    status = "secondary"
comm = '{0} {1} {2}{3}'.format("snmpwalk -c private -v2c",hostip,"-s0 1.3.6.1.4.1.9.9.147.1.2.1.1.1.4.",ind)
aux = os.popen(comm,'r')
peer = aux.readline().rstrip('\n')
if (status == "primary" and "Active" not in peer) or (status == "secondary" and "Standby" not in peer):
    print(0)
else:
    print(1)
