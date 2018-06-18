import socket

# 创建tcp套接字
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("tcpSocket created")

# 创建udp套接字
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("udpSocket created")

sendAddr = ("127.0.0.1", 8080)
sendData = input("please input something")
udpSocket.sendto(b"sendData", sendAddr)
udpSocket.close()
