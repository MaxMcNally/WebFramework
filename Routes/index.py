from BaseClasses.Route import Route
TemplateFile = 'Index.html'

class Index(Route):
    def __init__(self):
        self.TemplateFile = TemplateFile
        super().__init__()

    def Route(self):
        print("Running Users Index")
        data = {
            'users' : 'Foo'
        }
        return {
            'data' : data,
            'output' : self.Template(data)   
        }

   