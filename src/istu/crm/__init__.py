# Example package with a console entry point
from __future__ import print_function

from pyramid.config import Configurator
from pyramid.response import Response
from wsgiref.simple_server import make_server


def hello_world(request):
    return Response('<body><h1>Hello, World!</h1></body>')


def hi_body(request):
    print(request.GET)
    name = request.GET.get("name", "Unknown person")
    return Response('Hi, {}!'.format(name))


def ask(request):
    q = request.POST.get("q", '').strip()
    if q == '':
        return Response("""
        <form action="ask" method="POST">
           <input name="q" placeholder="Делай запрос, чувак!"> </br>
           <input name="submit" type="submit" value="Ok">
        </form>
        """)
    else:
        return Response("""
        <h1>Hi, {q}!</h1>
        <p>Привет, {q}!<p>
        <p>Еще тект для понтов</p>
        """.format(q=q))


def main(global_config, **settings):
    config = Configurator(settings=settings)

    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')

    config.add_route('hi', '/hi')
    config.add_view(hi_body, route_name='hi')

    config.add_route('ask', '/ask')
    config.add_view(ask, route_name='ask')

    return config.make_wsgi_app()

NET = '0.0.0.0'
PORT = 6543

def run():
    app = main(None)
    print("http://127.0.0.1:{}".format(PORT))
    server = make_server(NET, PORT, app)
    server.serve_forever()

if __name__=="__main__":
    run()
