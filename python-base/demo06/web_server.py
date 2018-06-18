
# coding:utf-8
#tcp socket 服务端
import socket

from multiprocessing import Process
# from socket import socket,AF_INET

"""
    HTTP1.1 200 OK\r\n
    \r\n
    hello world
"""
"""
    HTTP1.1 404 Not Found\r\n
    \r\n
    not found
"""

HTML_ROOT_DIR = "./html"

def handle_client(client_socket):
    #处理客户度请求
    request_data = client_socket.recv(1024)
    response_start_line = "HTTP/1.1 200 OK\r\n\r\nhello world"
    response_headers = "Server: My Server\r\n"
    response_body = "hello world lyon"


    try:
        file = open(HTML_ROOT_DIR + "index.html")
    except IOError:
        print("error")
    pass
if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", "8000"))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        handler_client_process = Process(target = handle_client, args=(client_socket,))
        handler_client_process.start
        client_socket.close()
