bind="0.0.0.0:8080"
pythonpath="/home/box/web"
def app(environ, start_response):
        status = '200 OK'
	headers = [
		('Content-type', 'text/plain')
	]
	body = [environ['QUERY_STRING'].replace('&', '\n')]
#	body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
        start_response(status, headers)
        return body
