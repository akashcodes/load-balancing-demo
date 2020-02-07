import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen
import time


class RequestHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine

    def handlePing(self):
        self.write("Sharath Madarchod!")
        self.finish()
    
    def get(self):
        self.handlePing()


application = tornado.web.Application([
        (r"/.*", MainHandler),
])


if __name__ == "__main__":
    
    http_server = tornado.httpserver.HTTPServer(application)
    port = 8000
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()