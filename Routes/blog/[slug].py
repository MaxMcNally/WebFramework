from BaseClasses.Route import Route

class BlogEntry(Route):
    def __init__(self):
        self.TemplateFile = 'blog/Entry.html'
        super().__init__()

    def Route(self,id):
        print("Running Slug with ID: " + id)
        data = {
            'slug' : id
        }
        return {
            'data' : data,
            'output' : self.Template(data)   
        }
