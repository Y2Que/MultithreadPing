import os

ping_timeout_ms = "1000"
server_ip = "192.168.1.83"

# ping IP and suppress default output
rep = os.system("ping -w " + ping_timeout_ms +  " " + server_ip + " > nul")

if rep == 0:
    print "\n" + server_ip + " is UP"
else:
    print "\n" + server_ip + " is DOWN"