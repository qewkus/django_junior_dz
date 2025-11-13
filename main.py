# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
from config import CONTACTS

#Настройки запуска
hostName = "localhost"  # Адрес
serverPort = 8080  # Порт


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов
        """
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()
        with open(CONTACTS, encoding='utf-8') as f:
            content = f.read()
        # Завершение формирования заголовков ответа
        self.wfile.write(bytes(content, "utf-8"))  # Тело ответа

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(post_data)

        response = f"Received POST data: {post_data.decode('utf-8')}"
        print(response)


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
