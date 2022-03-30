from BaseClasses.Route import Route
TemplateFile = 'blog/Author.html'

class BlogAuthor(Route):
    def __init__(self):
        super().__init__(self)

    def Route(self,id):
        print("Running Slug with ID: " + id)
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