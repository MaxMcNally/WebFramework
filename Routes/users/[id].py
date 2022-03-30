from BaseClasses.Route import Route
TemplateFile = 'users/Index.html'

class UserIndex(Route):
    def __init__(self):
        self.TemplateFile = TemplateFile
        super().__init__()

    def Route(self):
        print("Running User Index")
        data = {
            'user' : 'Bar'
        }
        return {
            'data' : data,
            'output' : self.Template(data)   
        }
