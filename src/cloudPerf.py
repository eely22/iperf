import socket
from subprocess import call
from time import sleep

host = '0.0.0.0'
port = 9017
addr = (host, port)
buf = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)

while 1:
    (data,clientAddr) = sock.recvfrom(buf)
    if not data:
        print "Client has exited!"
        break
    else:
	print "\nOn address: " + str(clientAddr[0]) + ":" + str(clientAddr[1])
        print "\nReceived messag: " + data
	sock.sendto(str(clientAddr[1]) + "\r\n", clientAddr)
	sock.close()
	sleep(2)
	#call("./iperf -c " + str(clientAddr[0]) + " -p " + str(clientAddr[1]) + " -t 5 -b 1m", shell=True)
	call("./iperf -c " + str(clientAddr[0]) + " -p " + str(clientAddr[1]) + " -B 172.31.10.105 -E " + str(port) + " -t 45 -b 30m", shell=True)

	abort

# Close socket
sock.close()

