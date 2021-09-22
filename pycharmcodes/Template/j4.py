from jinja2 import Environment, FileSystemLoader

persons = [
    {"name":"Prem","age":21},
    {"name":"Raj","age":23},
    {"name":"Shivba","age":28},
    {"name":"Sanju","age":22}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template("showperson.txt")

output = template.render(persons=persons)
print(output)