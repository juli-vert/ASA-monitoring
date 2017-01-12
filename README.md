# ASA-monitoring
It's a (Zabbix) custom template for an old Cisco ASA 5520 with some scripting

Some macros are needed:
{$SNMPHOST} = I know you can use {HOST.CONN} but I preferred to create my own "variable"
{$SNMP_COMMUNITY} = As usual
{$PEERIP} = Peer IP of one IPSec Tunnel (if you have more than one just clone the monitor)

I've called my per-interface monitors with the correct interface name, you can get yours with the MIB ifDescr
OID: 1.3.6.1.2.1.2.2.1.2
