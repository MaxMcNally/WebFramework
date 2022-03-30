from BaseClasses.Route import Route

class ProductPage(Route):
    def __init__(self):
        self.TemplateFile = 'product/Page.html'
        super().__init__()
            
    def Route(self,id):
        print("Running Product ID: " + id)
        data = {
            'productID' : id
        }
        output = self.Template(data)   
        return {
            'data' : data,
            'output' : output
        }

