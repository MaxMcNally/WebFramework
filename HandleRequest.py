
def HandleRequest(routes,path):
    if path.endswith('/') and len(path.rstrip('/')) > 0:
        path = path.rstrip('/')[0]
    wildcardPath = path.replace(path.split('/')[-1],'*')
    #check static routes
    if path in routes:
        print("Matched Path")
        f = routes[path]
        print(f().Route)
        return f().Route()
    #check dynamic routes
    if wildcardPath in routes:
        print("Matched Wildcard Path")
        wildcard = path.split('/')[-1]
        f = routes[wildcardPath]
        print(f().Route,wildcard)
        return f().Route(wildcard)
