# https://docs.python.org/3/library/http.server.html

import os
import http.server as server

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):

    def __reply(self, message):
        self.wfile.write(message.encode('utf-8'))
        self.end_headers()
    
    def __response(self, code, message):
        self.send_response(code, message)
        self.end_headers()

    def do_PUT(self):
        filename = os.path.basename(self.path)
        print(f"filename: {filename}")
        print(f"self.path: {self.path}")

        file_length = int(self.headers['Content-Length'])
        print(f"file_length: {file_length}")
        
        with open(filename, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))
        
        self.__response(201, 'Created')
        self.__reply(f'Saved {filename}')
        
    def do_GETCONTENT(self):
        self.__response(201, 'Sending back content')
        self.__reply(f'Replying back with content info')
    
if __name__ == '__main__':
    server.test(HandlerClass=HTTPRequestHandler)

"""
Noteworthy http.server function docs:

end_headers()
    Adds a blank line (indicating the end of the HTTP headers in
    the response) to the headers buffer and calls flush_headers().

send_response()
    Adds a response header to the headers buffer and logs the
    accepted request. The HTTP response line is written to the
    internal buffer, followed by Server and Date headers.
    The values for these two headers are picked up from the
    version_string() and date_time_string() methods, respectively.
    If the server does not intend to send any other headers using
    the send_header() method, then send_response() should be
    followed by an end_headers() call.
"""