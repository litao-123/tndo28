import tornado.options
from tornado.options import define, options

from handlers.main import IndexHandler,ExploreHandler,PostHandler
from handlers.account import RegisterHandler
from util import ui_modules, ui_methods

define('port',default='8000',type=int,help='Linstening port')
define('debug',default='True',type=bool,help='debug mode')


class Application(tornado.web.Application):
    def __init__(self,debug=False):
        handlers = [
            (r"/", IndexHandler),
            (r"/explore", ExploreHandler),
            (r"/post/(?P<post_id>[0-9]+)", PostHandler),
            (r"/signup)", RegisterHandler),
        ]
        settings = dict(
            debug=debug,
            static_path='static',
            # static_url_prefix='/photo/',
            template_path='templates',
            # autoescape=None,
            ui_methods=ui_methods,
            ui_modules=ui_modules,
            cookie_secret='12345612',
            # login_url='/temp',
            # xsrf_cookies = True,
            pycket={
                'engine': 'redis',
                'storage': {
                    'host': 'localhost',
                    'port': 6379,
                    'db_sessions': 5,
                    'max_connections': 2 ** 10,
                },
                'cookies': {
                    'expires_days': 7
                }
            }
        )
        super().__init__(handlers,**settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application(debug=options.debug)
    app.listen(options.port)
    print("Server start on port {}".format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()