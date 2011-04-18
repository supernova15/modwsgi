"""

>>> import _testfuncs
>>> connection = _testfuncs.connection()
>>> messages = _testfuncs.messages()
>>> connection.putrequest('GET', '/start_response-1g.wsgi')
>>> connection.endheaders()
>>> response = connection.getresponse()
>>> response.status
500
>>> messages.output(-1)
'[error] ValueError: status code is not a 3 digit integer'

"""

def application(environ, start_response):
    status = 'XYZ OK' 
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
