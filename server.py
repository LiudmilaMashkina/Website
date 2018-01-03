#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer

class Resource:
    def __init__(self, content_type, file_name):
      self.content_type = content_type
      self.file_name = file_name


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
    # GET
    def do_GET(self):
        print(self.path)

        resourceMap = {
            '/index.html' : Resource('text/html','index.html'),
            '/contacts.html' : Resource('text/html', 'contacts.html'),
            '/myCV.html' : Resource('text/html', 'myCV.html'),
            '/' : Resource('text/html','index.html'),
            '/main_pic.jpg' : Resource('image/jpeg','main_pic.jpg'),
            '/main_photo_left.jpg' : Resource('image/jpeg','main_photo_left.jpg'),
            '/main_photo_right.jpg' : Resource('image/jpeg','main_photo_right.jpg'),
            '/download_small.png' : Resource('image/png','download_small.png'),
            '/mashkina.png' : Resource('image/png','mashkina.png'),
            '/instagram_button.png' : Resource('image/png','instagram_button.png'),
            '/facebook_button.png' : Resource('image/png', 'facebook_button.png'),
            '/linkedin_button.png' : Resource('image/png', 'linkedin_button.png'),
            '/beer_vert.png' : Resource('image/png', 'beer_vert.png'),
            '/beer_hor.png' : Resource('image/png', 'beer_hor.png'),
            '/christmas_tree.png' : Resource('image/png', 'christmas_tree.png'),
            '/olympic_bibs.png' : Resource('image/png', 'olympic_bibs.png'),
            '/binary.png' : Resource('image/png', 'binary.png'),
            '/lens.png' : Resource('image/png', 'lens.png'),
            '/lm_favicon.png' : Resource('image/png', 'lm_favicon.png'),
            '/style.css' : Resource('text/css','style.css'),
            '/mashkina_cv.pdf' : Resource('application/pdf', 'mashkina_cv.pdf')
        }
        
        resource = resourceMap.get(self.path, None)
        print(resource)
        # Send response status code
        if resource == None:
            self.send_response(404)
        else:   
            self.send_response(200)
            self.processRequest(resource)

    def processRequest(self, resource):
        self.send_header('Content-type',resource.content_type)
        self.end_headers()

        if resource.content_type.startswith('text/'):
            message = open(resource.file_name).read()
            self.wfile.write(bytes(message, "utf8"))
        else:
            message = open(resource.file_name, 'rb').read()
            self.wfile.write(message)

def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ("0.0.0.0", 8080)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()