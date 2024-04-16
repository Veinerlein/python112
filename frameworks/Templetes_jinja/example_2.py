from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

# {%  filter | назва фільтру %}
# <фрагмент для задіювання фільтру>
# {%endfilter%}

# макро визначення  {% macro <назва(атрибути)> %} <шаблон рядка>  {% endmacro %} <теги та значення змінних> - функція в
# jinja2

html = """
{%- macro input(name,value='', type='text',size = '20') -%}
    <input type="{{type}}" name = '{{name}}' value = '{{ value }}' {{size}}>
{%-endmacro%}
<p>{{ input('username', "Enter the name") }}</p>
<p>{{ input('email', 'Enter the email') }}</p>
<p>{{ input('password') }}</p>
"""

tm = Template(html)
msg = tm.render()
print(msg)

persons = [
    {"name": 'Alex', 'year': 18, "weight": 78.5},
    {"name": 'Nick', 'year': 28, "weight": 82},
    {"name": 'Valdis', 'year': 33, "weight": 94}
]

tpl = """
{%- for u in users -%}
   {# {% filter upper -%}
        {{u.name}}
    {%-endfilter%} #}
    {%- filter string %} {{ u.year }} - {{ u.weight }} {% endfilter %}
{%endfor-%}
"""
# синтаксис коментаря {##}
tm = Template(tpl)
msg = tm.render(users=persons)
print(msg)

html = """
{%- macro input(n,p, t="text") -%}
<input type = {{t}} name={{n}} placeholder={{p}}>
{%- endmacro -%}
<p><{{ input('firstname','Name') }}></p>
<p><{{ input('lastname',"Lastname") }}></p>
<p><{{ input('address','Address') }}></p>
<p><{{ input("phone","Phone number", t='tel') }}></p>
<p><{{ input("email","Post", t = 'email') }}></p>
"""
tm = Template(html)
res = tm.render()
print(res)




html2 = """
{% macro list_users(lst) %}
<ul>
{% for u in users -%}
    <li>{{u.name}}
        <ul>
            <li>"year" = {{u.year}}</li>
            <li>"weight" = {{u.weight}}</li>
        </ul>
    </li>
{%endfor-%}
</ul>
{%-endmacro-%}

{{ list_users(users) }}
"""

# {% call[(параметри)] <macro> %} шаблон {% endcall %}

html = """
{% macro list_users(lst) %}
<ul>
{% for u in users -%}
    <li>{{u.name}} {{caller(u)}}
    </li>
{%endfor-%}
</ul>
{%-endmacro-%}

{% call(user) list_users(users) %}
    <ul>
        <li>age:{{user.year}}</li>
        <li>weight:{{user.weight}}</li>
    </ul>
{% endcall %}
"""

persons = [
    {"name": 'Alex', 'year': 18, "weight": 78.5},
    {"name": 'Nick', 'year': 28, "weight": 82},
    {"name": 'Valdis', 'year': 33, "weight": 94}
]

tmp = Template(html)
msg2 = tmp.render(users=persons)
print(msg2)

"""
<ul>
<li>Alex
        <ul>
            <li>"year" = 18</li>
            <li>"weight" = 78.5</li>
        </ul>
    </li>
<li>Nick
        <ul>
            <li>"year" = 28</li>
            <li>"weight" = 82</li>
        </ul>
    </li>
<li>Valdis
        <ul>
            <li>"year" = 33</li>
            <li>"weight" = 94</li>
        </ul>
    </li> 
</ul>"""

# робота із шаблонами


subs = ['Culture', 'Science', "Politic", 'Sport']
file_loader = FileSystemLoader('Templates')  # передав папку шаблонів
env = Environment(loader=file_loader)  # загрузка оточення

tm = env.get_template('about.html')  # файл шаблонів
# msg = tm.render(title='About Jinja2')
msg = tm.render(list_table=subs)
print(msg)

# {% include <шлях до шаблону> %} - підключення
# {% import <шлях до файлу шаблону> as <allies> %}

# розширення шаблону
# {% block назва блоку %} {% endblock %}


cars = [{'name': 'volvo', 'price': 2000}, {'name': 'marcedes', 'price': 4000}]
text = "this is car and price:" \
       "{% for i in c %} " \
       "{{(i.name | upper )}} {{i.price}}" \
       "{% filter upper %}{{i.name}}{% endfilter %}" \
       "{%endfor%}" \

t = Template(text)
m = t.render(c=cars)
print(m)

data = [
    {'name': 'firstname', 'plc': 'Name'},
    {'name': 'lastname', 'plc': 'Lastname'},
    {'name': 'address', 'plc': 'Address'},
    {'name': 'phone', 'plc': ' Phone'},
    {'name': 'email', 'plc': 'Post'}
]
t = """
{% macro input(n,plch,t='type') -%}
<p><input type = {{t}} name = {{n}} placeholder={{plch}}></p>
{%- endmacro %}
{% for d in data -%}
{%- if d.name=='phone' %}
{{input(d.name,d.plc,t="tel")}}
{%- elif d.name == 'email' %}
{{input(d.name,d.plc,'email')}}
{%- else %}
{{input(d.name,d.plc)}}
{%- endif %}
{%- endfor %}

"""
macro = Template(t)
res = macro.render(data=data)
print(res)

# знизу ідентичний результат із іншим кодом через підхід передавання в макрос аргументом цілий список

t = """
{%-macro input(data) -%}
<p>{%- for d in data %}
{%- if d.name == 'phone' %}
<input type = 'tel' name = {{d.name}} placeholder={{d.plc}}>
{%- elif d.name == 'email' %}
<input type = 'email' name = {{d.name}} placeholder={{d.plc}}>
{% else %}
<input type = 'text' name = {{d.name}} placeholder={{d.plc}}>
{%- endif %}
{%- endfor %}
</p>
{% endmacro %}
{{input(data)}}
"""

macro = Template(t)
res = macro.render(data=data)
print(res)





"""FLASK"""
# pip install Flask
