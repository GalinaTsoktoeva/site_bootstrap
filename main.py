import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def __get_index(self):
        return """
<!-- CSS -->
<style>
    @media (min-width: 768px) {
        .navbar-container {
            position: sticky;
            top: 0;
            overflow-y: auto;
            height: 100vh;
        }

        .navbar-container .navbar {
            align-items: flex-start;
            justify-content: flex-start;
            flex-wrap: nowrap;
            flex-direction: column;
            height: 100%;
        }

        .navbar-container .navbar-collapse {
            align-items: flex-start;
        }

        .navbar-container .nav {
            flex-direction: column;
            flex-wrap: nowrap;
        }

        .navbar-container .navbar-nav {
            flex-direction: column !important;
        }
    }
</style>

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Главная</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>
<body>

<div class="container-fluid">
    <div class="row">
        <div class="col-md-4 col-lg-3 navbar-container bg-dark">
            <!-- Вертикальное меню -->
            <nav class="navbar navbar-expand-md bg-dark"data-bs-theme="dark">
              <a class="navbar-brand" href="#">
                <img src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Logo" width="30" height="24"
                     class="d-inline-block align-text-top">
                Меню
              </a>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar"
                      aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbar">
                    <!-- Пункты вертикального меню -->
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="#link-1">Главная</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#link-2">Категории</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#link-3">Заказы</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#link-4">Контакты</a>
                        </li>
                        <li class="nav-item dropdown fixed-bottom">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                               aria-expanded="false">
                                Пользователи</a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="#">Профиль</a></li>
                                <li><a class="dropdown-item" href="#">Выход</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
        <div class="col-md-8 col-lg-9 content-container" >
            <h2 class="text-center mt-5">Контакты</h2>
            <div class="container">
                <div class="row mt-5 justify-content-center">
                    <div class="col-6 md-5">
                        <form class="border border-light rounded-3">
                            <div class="mb-3">
                                <label for="exampleInputEmail1" class="form-label">Имя</label>
                                <input name="name" type="text" class="form-control" id="exampleInputEmail1"
                                       aria-describedby="emailHelp">
                            </div>
                            <label for="exampleInputEmail1" class="form-label">Почта</label>
                            <div class="input-group mb-3">
                                <span class="input-group-text" id="basic-addon1">@</span>
                                <input name="email" type="email" class="form-control" aria-label="Username"
                                       aria-describedby="basic-addon1">
                            </div>
                            <div class="mb-3">
                                <label for="exampleFormControlTextarea1" class="form-label">Сообщение</label>
                                <textarea name="message" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                            </div>

                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                    </div>
                    <div class="col-6">
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title">Наши контакты</h5>
                                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum., </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>"""

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")