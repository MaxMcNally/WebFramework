from DB.Connection import MySQLConnection


from LoadRoutes import LoadRoutes
from HandleRequest import HandleRequest
#connect to db
db = MySQLConnection()
routes = LoadRoutes('Routes/', {})
print(routes)
def App(environ, start_response):
    path = environ['PATH_INFO']
    pageData = HandleRequest(routes,path)
    if pageData == None:
        data = b"Sorry, that page could not be found\n"
        start_response("404", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])

    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(pageData['output'])))
    ])
    return iter([pageData['output'].encode('UTF-8')])