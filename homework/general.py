from jinja2 import FileSystemLoader,Environment

loader = FileSystemLoader('templates')
env = Environment(loader=loader)

tm = env.get_template('login.html')
res = tm.render(title='Homework')

print(res)


