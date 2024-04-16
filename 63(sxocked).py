import socket
from view63 import index, blog


class Web:
    URL = {"/": index, "/blog": blog}  # index,blog  == HTML Templates
    ip_address = '127.0.0.1'
    port = 5000

    def __init__(self):
        pass

    def main(self):
        server_socked = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET вказує на Сімейство Адрес IPv4.
        # Константа SOCK_STREAM представляє надійний, двосторонній, з'єднаний канал зв'язку, який зазвичай
        # використовується разом із протоколом керування передачею даних (TCP - Transmission Control Protocol).
        print(server_socked)
        bind = server_socked.bind((self.ip_address, self.port))
        listen = server_socked.listen()  # Сервер в режимі прийому з'єднання
        # print(bind)
        # print(listen)
        while True:
            client_socket, address = server_socked.accept()
            request = client_socket.recv(1024)
            print(address, request)
            response = self.generate(request.decode())
            client_socket.sendall(response)
            client_socket.close()

    def generate(self, request):
        method, url = self.reques_parse(request)
        headers, code = self.generate_headers(method, url)
        body = self.generate_content(code, url)
        return (headers + body).encode()

    def reques_parse(self, request):
        pars = request.split()
        method = pars[0]
        url = pars[1]
        return method, url

    def generate_headers(self, method, url):
        if method != "GET":
            return "HTTP/1.1 405 method not Allowed\n\n", 405
        if url not in self.URL:
            return 'HTTP/1.1 405 Method not found\n\n', 404
        return 'HTTP/1.1 200 OK!\n\n', 200

    def generate_content(self, code, url):
        if code == 404:
            return '<h1>404</h1><h3>Not Found</h3>'
        elif code == 405:
            return '<h1>404</h1><h3>Method not allowed</h3>'
        return self.URL[url]()


web = Web()

web.main()
