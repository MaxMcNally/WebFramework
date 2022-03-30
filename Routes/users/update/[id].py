from BaseClasses.Route import Route
TemplateFile = 'users/Update.html'

class UpdateUser(Route):
    def __init__(self):
        self.TemplateFile = TemplateFile
        super().__init__()

    def Route(self):
        print("Running Update User Index")
        data = {
            'blog' : 'Foo'
        }
        return {
            'data' : data,
            'output' : self.Template(data)   
        }
