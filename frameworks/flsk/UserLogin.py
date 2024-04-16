from flask_login import UserMixin # має додаткові методи(прописані внизу)
from flask import url_for


class UserLogin(UserMixin): # Цей клас може бути використаний для роботи з користувачами в рамках Flask-додатку,
    # забезпечуючи легке взаємодію з даними користувача та їх аутентифікацію.

    def from_db(self, user_id, db): #  Метод приймає ідентифікатор користувача (user_id) і об'єкт бази даних (db),
        # використовуючи який він здійснює запит до бази даних для отримання інформації про користувача.
        # Ця інформація зберігається в приватному атрибуті __user. Після цього, метод повертає сам об'єкт, дозволяючи використовувати ланцюгові виклики.
        self.__user = db.get_user(user_id)
        return self

    def create(self, user): # Цей метод призначений для ініціалізації об'єкта UserLogin безпосередньо з переданого словника user,
        # який містить інформацію про користувача.
        # Також, цей метод зберігає інформацію про користувача в атрибуті __user і повертає сам об'єкт.
        self.__user = user
        return self

    def get_id(self): #  Використовується Flask-Login для отримання унікального ідентифікатора користувача.
        # Цей метод повертає ідентифікатор користувача у формі рядка, взятого з атрибута __user.
        return str(self.__user['id'])

    def get_name(self): # Повертає ім'я користувача з атрибута __user, якщо воно існує. В іншому випадку повертає 'Without name'.
        return self.__user['name'] if self.__user else 'Without name'

    def get_email(self): # Аналогічно до get_name, цей метод повертає електронну адресу користувача, якщо така існує. В іншому випадку повертає 'Without email'.
        return self.__user['email'] if self.__user else 'Without email'

    def get_avatar(self, app): # Метод призначений для отримання аватару користувача.
        # Якщо користувач не має власного аватару (__user['avatar'] не існує),
        # метод намагається відкрити файл за замовчуванням з папки static/images. В разі успіху, метод повертає вміст файлу.
        # В іншому випадку, якщо файл не знайдено, виводиться повідомлення про помилку, і метод повертає None.
        # Якщо у користувача є власний аватар, метод повертає його без спроби зчитування файлу за замовчуванням.
        img = None
        if not self.__user['avatar']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename = 'images/default.png'),'rb') as f:
                    img = f.read()
            except FileNotFoundError as e:
                print('There is no avatar default' + str(e))
        else:
            img = self.__user['avatar']
        return img


# def is_authenticated(self) метод авторизації return True

# def is_anonymus(self) метод перевірки неавторизованих return False
# def is_active(self) метод перевірки авторизованих return True
