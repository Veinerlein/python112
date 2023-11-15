"""WEB SOCKET"""
WEB_SOCKET = {
    "Model OSI": [
        "7 Application layer",
        "6 Presentation layer",
        "5 Session layer",
        "4 Transport layer",
        '3 Network layer',
        "2 Datalink layer",
        '1 Physical layer'
    ],
    "Model TCP/IP": [
        "Application",
        "Transport",
        "Internet",
        "Link"
    ]
}
OSI = "Open Systems Interconnection model (OSI model) is a conceptual model from the " \
      "International Organization for Standardization (ISO) that 'provides a common basis" \
      " for the coordination of standards development for the purpose of systems" \
      " interconnection.' In the OSI reference model, the communications between " \
      "systems are split into seven different abstraction layers: Physical, Data Link," \
      " Network, Transport, Session, Presentation, and Application."

TCP = [' TCP/IP, is a framework for organizing the set of communication protocols used in the Internet and similar ' \
       'computer networks according to functional criteria']
UDP = ["User datagramm protocol", 'speed']
"""
Transmission control protocol
"""
"""
Domain name system
"""
socket = "IP address + port"  # є клієнтський та серверний

import socket
from view63 import index, blog

URLS = {
    '/': index,
    "/blog": blog  # запуск як функцію у коді generate_content
}


def reques_parse(request): # попаде requests.decode()
    parsed = request.split(' ')  # розділити по пробілам бінарний ретюрн
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_headers(method, url):
    if method != "GET":
        return 'HTTP/1.1 405 Method not allowed\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Method not found\n\n', 404
    return 'HTTP/1.1 200 OK!\n\n', 200  # headers and code


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><h3>Not Found</h3>'
    elif code == 405:
        return '<h1>405</h1><h3>Method not allowed</h3>'
    return URLS[url]()


def generate_response(request):
    method, url = reques_parse(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()


ip_address = '127.0.0.1'
port = 5000


# adres_port = 127.0.0.1:5000

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # установлене зєднання на основі протоколі ITCP
    # додаток і отримує і відправляє дані
    server_socket.bind((ip_address, port))  # прив'язує сокет до адреси та порту
    server_socket.listen()  # запуск режиму прийому з'єднання, після цього можна викликати сервер за айпі та портом
    # разом
    while True:
        client_socket, address = server_socket.accept()  # Приймає з'єднання і блокує очіківання від повідомлення від
        # клієнта,  в результаті повертає кортеж
        requests = client_socket.recv(1024)  # читає та повертає набір байтів із сокета
        print(f"Client: {address} => \n {requests.decode('utf-8')}\n")
        print(client_socket)

        response = generate_response(requests.decode())
        client_socket.sendall(response) # відправляє данні у сокет
        client_socket.close()


if __name__ == '__main__':
    while True:
        run()

"""view.py"""


