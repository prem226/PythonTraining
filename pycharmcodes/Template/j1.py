from jinja2 import Template

name = input("Enter name: ")
tm = Template("hello {{ name }}")
msg = tm.render(name=name)

print(msg)

name = 'john'
age = 21

tm = Template("my name is {{name}} and i am {{age}}")
msg = tm.render(name=name,age=age)
print(msg)