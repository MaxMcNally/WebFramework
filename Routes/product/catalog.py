from BaseClasses.Route import Route
TemplateFile = 'product/Catalog.html'

class ProductCatalog(Route):
    def __init__(self):
        self.TemplateFile = TemplateFile
        super().__init__(self)

    def Route(self):
        print("Running Product Catalog")
        data = {
            'blog' : 'Foo'
        }
        return {
            'data' : data,
            'output' : self.Template(data)   
        }

