from BaseClasses.Route import Route
TemplateFile = 'users/Index.html'

class UserIndex(Route):
    def __init__(self):
        super().__init__(self)

    def Route(self):
        print("Running User Index")
        data = {
            'user' : 'Bar'
        }
        return {
            'data' : data,
            'output' : self.Template(data)   
        }

    def Template(self,data):
        template = self.env.get_template(TemplateFile)
        return template.render(data)