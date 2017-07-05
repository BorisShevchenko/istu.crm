# Example package with a console entry point
from __future__ import print_function

from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')


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
