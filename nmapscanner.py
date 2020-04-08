import nmap
import sys
import pprint

pp = pprint.PrettyPrinter()

target = sys.argv[1]
#ports = "21,22,80,138,443,993,8080"
ports  = '21'
nm     = nmap.PortScanner()

print("Scanning target",target,"\nPorts: ",ports)
nm.scan(target, ports=ports)
#pp.pprint(nm.all_hosts())

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        for port, state in nm[host][proto].items():
            print('port : %s\tstate : %s' % (port,state['state']))