import jinja2

catalog = [
    {"id": 1, 'item': 'pen', 'price': 1.25},
    {"id": 2, 'item': 'cap', 'price': 4},
    {"id": 3, 'item': 'table', 'price': 25},
    {"id": 4, 'item': 'chair', 'price': 10},
    {"id": 5, 'item': 'plate', 'price': 2}
]

text = "There is interior items: {% for i in m %} {{i['item']}} {% endfor %}. THere is amount" \
       "of money : {{ m | sum(attribute = 'price') }}." \
       "there are cost that more(and) than 10 USD : {% for i in m %} " \
       "{% if i['price'] >= 10 %} " \
       "{{i['price']}}" \
       "{%endif%}" \
       "{%endfor%}"

tm = jinja2.Template(text)
msg = tm.render(m=catalog)
print(msg)
