from BaseClasses.Route import Route
TemplateFile = 'blog/Index.html'

class BlogIndex(Route):
    def __init__(self):
        self.TemplateFile = TemplateFile
        super().__init__()

    def Route(self):
        print("Running Blog Index")
        data = {
            'blog' : 'Foo'
        }
        return {
            'data' : data,
            'output' : self.Template(data)   
        }
