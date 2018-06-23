
# coding:utf-8
import socket

from multiprocessing import Process
# from socket import socket,AF_INET

HTML_ROOT_DIR = ""


def handle_client(client_socket):

    # 处理客户度请求
    request_data = client_socket.recv(1024)
    print("request data:", request_data)

    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My Server\r\n"
    response_body = "hello world lyon"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response:", response)

    # 向客户端响应数据
    client_socket.send(bytes(response, "utf-8"))
    client_socket.close()

    # try:
    #     file = open(HTML_ROOT_DIR + "index.html")
    # except IOError:
    #     print("error")


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        # print("[%s, %s]用户连接上了" % (client_address[0],client_address[1]))
        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
