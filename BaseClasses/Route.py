import DB
from jinja2 import Environment, PackageLoader, select_autoescape
from datetime import date
globals = {
    'date' : date.today()
}
env = Environment(
    loader = PackageLoader("App"),
    autoescape = select_autoescape()
)

class Route:
    def __init__(self):
        print("Making Base Class")
        print(self)
        self.env = env
        self.DB = DB
        self.globals = globals
        self.TemplateFile = self.TemplateFile

    def Template(self,data):
        data['globals'] = globals
        print("Rendering Template with")
        print(data)
        template = self.env.get_template(self.TemplateFile)
        return template.render(data)    