from istu.crm import main
from wsgiref.simple_server import make_server

NET = '0.0.0.0'
PORT = 6543

if __name__ == '__main__':
    app = main(None)
    print("http://127.0.0.1:{}".format(PORT))
    server = make_server(NET, PORT, app)
    server.serve_forever()
