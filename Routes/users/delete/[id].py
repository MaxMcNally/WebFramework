from BaseClasses.Route import Route
TemplateFile = 'users/Delete.html'

class DeleteUser(Route):
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

    def Template(self,data):
        template = self.env.get_template(TemplateFile)
        return template.render(data)