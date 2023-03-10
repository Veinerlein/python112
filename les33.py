"""
GIT BUSH HERE - робимо в будь-якому місці біля потрібного файлу, або по теці проєкту

git --version - - показує поточну версію встановленої програми GIT
git --help    - - показує усі поточні команди які є у GIT

git init - створюється репозиторій лише один раз для 1 проєкту (проєкт - поточна тека у котрій працюємо)/
            - утвориться файл init

git status - для контролю нашого статусу нашого репозиторія,
            On branch - гілка, master - імя головної гілки в гіті.
              в такому випадку ми в головній гілці гіта

            можна відійти від гілки мастер, скопіювати дані і працювати в іншій гілці
            із новою варіацією.
            untracked files - файли не під версіонним контролем

git add -A          -ми оберемо усі файли у теці та у її підтеках(Нічого не буде показано)
                                /можна перевірити git status
        (--all)
        *****.py    - імя нашого файлу якщо ми хочемо додати один файл
        .           -обере усі файли що є у папці але без вкладених тек

git restore --staged *******.py  - забрати файли із git add, тобто із staged зробити
                                        unstaged

(Примітка: У мене не показує файл 30-31.py а показує лише той, який )

git commit -m "імя поточного коміту"   -  (версія) контрольна точка яка нам
             (можна назвати як завгодно)                              необхідна
                -m  - означає message

git config --global user.name "user name" - назавжди реєструє і запамятовує імя користувача
           --local user.name "user name" - для кожного із репозиторіїв потрібно буде вводити імя
                                            та емейл
git config --global user.email "email of user" - ввести емейл
git config --global user.password "password"

(ПРИМІТКА: команда --global user.(name, or email, or password) покаже який логін, чи емейл, чи пароль у нас на даний
момент)
(ПРИМІТКА: ЯКЩО GIT НЕ КОМІТИТЬ ФАЙЛИ ЧЕРЕЗ ЯКІСЬ НЕПОТРІБНІ ФАЙЛИ, АБО У звязку із
ТЕКОЮ init, ТО ми створюємо звичайний файл тільки ЧЕРЕЗ ПЕЙЧАРМ із назвою ".gitignore" та
в середину файлу після команди слеш прописуємо імена файлів чи тек, які нам заважають.)
 Таким чином гіт буде ігнорувати їх)

git branch  - показує на якій гілці користувач знаходиться

$ git branch *НАЗВА ГІЛКИ* - Створити гілку

git branch -D **назва гілки** - ВИДАЛИТИ ГІЛКУ

git checkout *НАЗВА ГІЛКИ* - Перейти на цю гілку

git checkout -b *НАЗВА ГІЛКИ* - Створю гілку та переходжу на неї одразу

readme.md - звичайний док для опису поточного проекту

git merge *readme*  - (readme - це паралельна гілка) - Коли знаходишся на гілці мастер і
                      хочеш обєднати гілки

git log  -  Покаже історія комітів користувача

генерація токена на гітхаб. прописати його в своєму пк
SETTINGS/DEVELOPER SETTINGS/PERSONAL ACCESS TOKENS/ #GENERATE NEW TOKEN#/ВНЕСТИ ПАРОЛЬ/
/ВВЕСТИ СИСТЕМНЕ ІМЯ ТОКЕНУ/ТЕРНМІН ПРИДАТНОСТІ ТОКЕНУ/ ГАЛОЧКУ НА РЕПО\GENERATE TOKEN

У КОНСОЛІ ВІНДОВС КОМАНДА  - CONTROL
            АБО ТАК
            win+r=>control
ДИСПЕТЧЕР ОБЛІКОВИХ ДАНИХ
зявиться два пункти = WebCredentials  i  Windows Credentials(Потрібен цей)
додати адрес/
у Internet or network ввести адресу гітхабу(назву ресурсу який хочемо додати)
у user name вводимо так як ми реєструвались на гітхаб логін
у password вводимо увесь той токен

git remote add origin https://github.com/Veinerlein/python112.git
git push -u origin master

GIT PUSH  - ДЛЯ звичайного додавання файлів на існуючий повязаний репозиторій гіт хаб

git clone https://github.com/Veinerlein/python112.git - копія репозииторії в іншу папку

git pull - забрати дані із репозиторію собі на локальний ПК



"""











