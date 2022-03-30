from BaseClasses.Route import Route
TemplateFile = 'product/Catalog.html'

class ProductCatalog(Route):
    def __init__(self):
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

    def Template(self,data):
        template = self.env.get_template(TemplateFile)
        return template.render(data)