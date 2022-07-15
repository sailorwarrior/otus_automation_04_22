import random
import socket
import string
import sys
import datetime

from config import LOCALHOST


def generate_random_string(string_size):
    answer_codes = {200: 'OK', 400: 'Bad request', 404: 'Not found', 500: 'Internal Server Error'}
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    random_answer = random.choice(list(answer_codes))
    random_method = random.choice(methods)
    letters = string.ascii_letters
    header = ''.join(random.choice(letters) for i in range(string_size))
    request = f"{random_method}/HTTP/1.0\n {LOCALHOST}/?status={random_answer}\r\n Content-Length: 100\r\n" \
              f" Date:{datetime.datetime.now()}\r\n Content-Type: text/html\r\n <h1>{header}</h1>"
    return request


message = generate_random_string(20)
my_socket = socket.socket()

address_and_port = (LOCALHOST, int(sys.argv[1]))

my_socket.connect(address_and_port)

data_amount = my_socket.send(bytes(message, 'utf-8'))
print("Send", data_amount, "bytes")
my_socket.recv(1024)

my_socket.close()
