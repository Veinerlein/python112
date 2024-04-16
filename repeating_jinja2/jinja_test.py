from jinja2 import FileSystemLoader, Environment


env = Environment(loader=FileSystemLoader("templates"))
r = env.get_template("content.html").render(title = "ТИтульна сторінка") # імя шаблону, а в рендер можна передати
# список словників, а в аргументи рендеру можна називати змінні та давати їм значення для використання у інших
# документії
# коли змінив із login.html на content.html, то спрацював код extends. Тобто extends розширює login.html, a login.html
# у свою чергу бере макро із index.html. ЗАПУСКАТИ ПОТРІБНО ФАЙЛ ЯКИЙ Є extends
print(r)

# усі block мають бути в одному файлі так, як запуск програми почнеться саме з того самого файлу




