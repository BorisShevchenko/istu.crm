# Example package with a console entry point
from __future__ import print_function

from pyramid.config import Configurator
from pyramid.response import Response
from wsgiref.simple_server import make_server
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

# имя -> Значение
# A=[1,2,3,None,5,None,7,None,None,None,11,13,17]; A[0] == 1
# D={"881236":"Иванов", "555555":"Петров"}....


def hello_world(request):
    today = datetime.today()
    today = today.strftime("%d %B %Y, %A")
    return {"title": "Рекомендательная система рынка недвижимости г. Иркутска", "today": today}


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

    config.include('pyramid_chameleon')
    config.include('pyramid_debugtoolbar')

    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello',
                    renderer="istu.crm:templates/index.pt")

    config.add_route('hi', '/hi')
    config.add_view(hi_body, route_name='hi',
                    renderer="istu.crm:templates/index.pt")

    config.add_route('ask', '/ask')
    config.add_view(ask, route_name='ask',
                    renderer="istu.crm:templates/index.pt")

    config.add_static_view(name='layout', path='istu.crm:templates/layout')

    return config.make_wsgi_app()

NET = '0.0.0.0'
PORT = 6543


def run():
    app = main(None)
    print("http://127.0.0.1:{}".format(PORT))
    server = make_server(NET, PORT, app)
    server.serve_forever()

if __name__ == "__main__":
    run()
