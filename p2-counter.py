'''Phase 2 counter
Usage command [argv1 argv2]
argv1 = snmp host
argv2 = peer ip'''

#!/usr/bin/python3
import os,sys

hostip = sys.argv[1]
tunnelip = sys.argv[2]

comm = '{0} {1} {2} {3}'.format("snmpwalk -c private -v2c",hostip,"-s0 1.3.6.1.4.1.9.9.171.1.2.3.1.7 | grep",tunnelip)
aux = os.popen(comm,'r')
peer = aux.readline().rstrip('\n')
comm = '{0} {1} {2}'.format("echo",peer,"| awk -F \"3.1.7.\" '{print $2}' | awk -F \" = \" '{print $1}'")
aux = os.popen(comm,"r")
peerid = aux.readline().rstrip('\n')
comm = '{0} {1} {2} {3} {4}'.format("snmpwalk -c private -v2c",hostip,"-s0 1.3.6.1.4.1.9.9.171.1.3.2.1.2 | grep",peerid,"| wc -l")
aux = os.popen(comm,"r")
nump2 = aux.readline().rstrip('\n')
print (nump2)