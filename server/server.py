from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
import os

def log(message):
    stamp = datetime.datetime.now()
    print('[' + str(stamp) + ']: ' + message)


RESOURCE_TYPES = {
    'html' : 'text/html',
    'css' : 'text/css',
    'js' : 'application/javascript',
    'png' : 'image/png',
    'jpg' : 'image/jpeg',
    'pdf' : 'application/pdf'
}


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.logRequest()

        if self.path == '/health':
            self.send_response(200)
            return

        filename = self.path.split('/')[-1]
        extension = filename.split('.')[-1]

        if not filename:
            filename = 'index_2.html'
            extension = 'html'
        
        if not extension in RESOURCE_TYPES:
            self.send_response(404)
            return

        resource_type = RESOURCE_TYPES[extension]

        if os.path.isfile(filename):
            self.send_response(200)
            self.send_header('Content-type', resource_type)
            self.end_headers()

            if resource_type.startswith('text/'):
                message = open(filename).read()
                self.wfile.write(bytes(message, "utf8"))
            else:
                message = open(filename, 'rb').read()
                self.wfile.write(message)

            return

        self.send_response(404)

    def logRequest(self):
        log(self.path)
        client_ip = 'Client ip: ' + self.client_address[0]
        log(client_ip)

        if 'User-Agent' in self.headers:
            log('User agent: ' + self.headers['User-Agent'])

def run():
  log('starting server...')
 
  server_address = ("0.0.0.0", 8080)
  httpd = HTTPServer(server_address, RequestHandler)
  log('running server...')
  httpd.serve_forever() 
 
run()