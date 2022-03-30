from BaseClasses.Route import Route
TemplateFile = 'users/Create.html'

class CreateUser(Route):
    def __init__(self):
        self.TemplateFile = TemplateFile
        super().__init__(self)

    def Route(self):
        print("Running Blog Index")
        data = {
            'blog' : 'Foo'
        }
        return {
            'data' : data,
            'output' : self.Template(data)   
        }