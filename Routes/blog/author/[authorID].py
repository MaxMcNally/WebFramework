from BaseClasses.Route import Route
TemplateFile = 'blog/Author.html'

class BlogAuthor(Route):
    def __init__(self):
        self.TemplateFile = TemplateFile
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
