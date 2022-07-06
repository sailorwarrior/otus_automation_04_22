import socket
from config import LOCALHOST, random_port
from http.client import responses

my_socket = socket.socket()
address_and_port = (LOCALHOST, random_port())

my_socket.bind(address_and_port)
print("Socket 1 binded on", address_and_port)

BACKLOG = 10
my_socket.listen(BACKLOG)

conn, addr = my_socket.accept()

data = conn.recv(1024)

answer = data.decode("utf-8")
get_status = answer.split('?status=')
get_method = answer.split('/')
split_for_headers = answer.split('\r\n')
splited_headers = split_for_headers[1:len(split_for_headers) - 1]
splited_headers_to_str = ','.join(splited_headers)
response_stat = get_status[1][0:3]
test = responses[int(response_stat)]
print(f'Got data:\n Request Method: {get_method[0]}\n Request Source: {address_and_port}\n '
      f'Response Status: {response_stat}: {test} \n HEADERS:{splited_headers_to_str}')
