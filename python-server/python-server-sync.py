import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([ (r"/", MainHandler), ])  # URL Mapping

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)    # Port Number
    tornado.ioloop.IOLoop.current().start()