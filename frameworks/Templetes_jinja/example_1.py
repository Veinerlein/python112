from jinja2 import Template

name = 'Ihor'
age = 28

# tm = Template("Hello {{ n }}. I am {{age}}")  # виведеться власне значення червоного name
# msg = tm.render(n=name, age=age)  # імя попаде у обєет Темплейта рендер

per = {"name": 'Ihor', "age": 28}
tm = Template("HELLO {{ p.name }}, I am {{ p['age'] }}.")  # можна через словник к:з
msg = tm.render(p=per)
print(msg)


# {{ }} - вираз для вставлення конструкції Пайтон у шаблон
# {% %} - специфікатор шаблону
# {# #} - коментар
# # # - рядковий коментар

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


pers = Person("Vlad", 38)

# tm = Template('I am {{p.age}}, Hello {{p.name}}') # Можна через класи
tm = Template('I am {{p.get_age()}}, Hello {{p.name}}')  # можна через геттери

msg = tm.render(p=pers)
print(msg)

data = """
Modul Jinja2 instead of {{name}} painted the value
"""
tm = Template(data)
msg = tm.render(name='Vasil')
print(msg)

# {%raw%}...{%endraw%} - видасть сирий рядок без підстановки


# щоб вивести посилання в сирому вигляді у браузері
link = '<a href="#">link</a>'
tm = Template('{{link | e}}')  # e - ecranion екранування символів
msg = tm.render(link=link)
print(msg)

# щоб вивести список значень на сайті

# {% for вислів.. %}
# <блок що повторюється>
# {% endfor %}

cities = [
    {'id': 1, 'city': 'Kiyv'},
    {'id': 2, 'city': 'Zhitomyr'},
    {'id': 3, 'city': 'Ternopil'},
    {'id': 4, 'city': 'Zaporizhzhya'},
    {'id': 5, 'city': 'Rivne'},
    {'id': 6, 'city': 'Lutsk'}
]

links = '''<select name = 'cities'>
{% for city in cities -%}
    {% if city.id > 3 -%}
        <option value="{{city['id']}}">{{city['city']}}</option>
    {%elif city.city == 'Kiyv'%}
        <option>{{city['city']}}</option>
    {% else -%}
        {{ city['city']}}
    {% endif -%}
{% endfor -%}
</select>
'''
tm = Template(links)
print(tm.render(cities=cities))

# select = випадаючий список
# -   - мінус у кінці перед процентом у форі прибирає абзацні відступи (видаляє усі переноси і пробіли після блоку фор)

# {% if <умова> %}
# <Фрагмент умови>
# {% endif %}


menu = [
    {'link': 'index', 'name': 'Main'},
    {'link': 'news', 'name': 'News'},
    {'link': 'about', 'name': 'About a company'},
    {'link': 'shop', 'name': 'Shop'},
    {'link': 'contacts', 'name': 'Contacts'}
]
classname = {'class': "active"}

datas = """
<ul>
{% for elem in m -%}
{% if elem == m[0] -%}
<li><a href = "/{{elem['link']}}" class = {{c['class']}}>{{elem['name']}}</a><Li>
{%else-%}
<li><a href = "/{{elem['link']}}">{{elem['name']}}</a><Li>
{% endif -%}
{%endfor-%}
</ul>
"""

temp = Template(datas)
msg = temp.render(m=menu, c=classname)
print(msg)

cars = [
    {"model": "Audi", 'price': 23000},
    {"model": "Subaru", 'price': 17000},
    {"model": 'Renault', 'price': 44000},
    {"model": 'Wolksvagen', 'price': 21000},
    {"model": 'BMW', 'price': 34000}
]

sum = "Summ of all cars: {{c | sum(attribute = 'price')}}"


tm = Template(sum)
mesg = tm.render(c=cars)
print(mesg)










