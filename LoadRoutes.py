import os
import re
from importlib import import_module
import inspect
#load models
#Starting from a base directory,
#recursively search for files, building the route as you go
#ex. Routes/ -> Routes/product -> Routes/product/images -> Routes/product/images/[id]
def LoadRoutes(dir, routes = {}):
    for object in os.listdir(dir):
        if os.path.isdir(dir + object):
            if (dir + object).find('__pycache__') == -1:
                routes = LoadRoutes(dir + object + '/', routes)
        elif os.path.isfile(dir + object):
            if object != '__init__.py':
                route = dir + object.rsplit('.py')[0].rsplit('index')[0]
                route = re.sub(r"\[[^()]*\]", "*", route)
                import_path = ( dir + object).replace('/','.').rsplit('.py')[0]
                module = import_module(import_path)
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if name != 'Route': 
                        className = name
                moduleFunction = getattr(module, className)
                routes['/' + route.replace("Routes/","")] = moduleFunction
    return routes