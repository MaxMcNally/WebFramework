from BaseClasses.Route import Route
TemplateFile = 'users/Update.html'

class UpdateUser(Route):
    def __init__(self):
        super().__init__(self)

    def Route(self):
        print("Running Update User Index")
        data = {
            'blog' : 'Foo'
        }
        return {
            'data' : data,
            'output' : self.Template(data)   
        }

    def Template(self,data):
        template = self.env.get_template(TemplateFile)
        return template.render(data)