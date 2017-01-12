# ASA-monitoring
It's a (Zabbix) custom template for an old Cisco ASA 5520 with some scripting

Some macros are needed:
{$SNMPHOST} = I know you can use {HOST.CONN} but I preferred to create my own "variable"
{$SNMP_COMMUNITY} = As usual
{$PEERIP} = Peer IP of one IPSec Tunnel (if you have more than one just clone the monitor)

I've called my per-interface monitors with the correct interface name, you can get yours with the MIB ifDescr
OID: 1.3.6.1.2.1.2.2.1.2

The OIDs used are:

Uptime: 1.3.6.1.2.1.1.3.0 sysUpTime 
Interface Operational status: 1.3.6.1.2.1.2.2.1.8. ifOperStatus
Interface In traffic: 1.3.6.1.2.1.2.2.1.10. ifInOctets
Interface Out traffic: 1.3.6.1.2.1.2.2.1.16. ifOutOctets
Memory used: 1.3.6.1.4.1.9.9.48.1.1.1.5.1 ciscoMemoryPoolUsed
CPU used last minute: 1.3.6.1.4.1.9.9.109.1.1.1.1.4.1 cpmCPUTotal1min
Number of connections currently in use: 1.3.6.1.4.1.9.9.147.1.2.2.2.1.5.40.6 cfwConnectionStatValue 
Tunnels up: 1.3.6.1.4.1.9.9.171.1.2.1.1 cikeGlobalActiveTunnels
VPN Traffic IN: 1.3.6.1.4.1.9.9.171.1.2.1.3 cikeGlobalInOctets
VPN Traffic OUT: 1.3.6.1.4.1.9.9.171.1.2.1.11 cikeGlobalOutOctets
-- Script-based monitors --
Failover: 1.3.6.1.4.1.9.9.147.1.2.1.1.1.2 + 1.3.6.1.4.1.9.9.147.1.2.1.1.1.4 cfwHardwareInformation 
**To check some information about tunnels we need to get the indexes first using:
1.3.6.1.4.1.9.9.171.1.2.3.1.7 cikeTunRemoteValue **

Number of P2 on each IPSec tunnel: 1.3.6.1.4.1.9.9.171.1.3.2.1.2 cipSecTunIkeTunnelIndex

Some other monitors are still missing:
VPN active time: 1.3.6.1.4.1.9.9.171.1.2.3.1.16 cikeTunActiveTime
Per tunnel traffic IN: 1.3.6.1.4.1.9.9.171.1.2.3.1.19 cikeTunInOctets
Per tunnel traffic OUT: 1.3.6.1.4.1.9.9.171.1.2.3.1.27 cikeTunOutOctets
Tunnel status: 1.3.6.1.4.1.9.9.171.1.2.3.1.35 cikeTunStatus
Interface InDiscards: 1.3.6.1.2.1.2.2.1.13. ifInDiscards
Interface InErrors: 1.3.6.1.2.1.2.2.1.14. ifInErrors
Interface OutOctets: 1.3.6.1.2.1.2.2.1.16. ifOutOctets
Interface OutDiscards: 1.3.6.1.2.1.2.2.1.19. ifOutDiscards
