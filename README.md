### Проект API YATUBE
___
Проект API YATUBE позволяет обращаться к социальной сети Yatube с помощью запросов.

####Доступные возможности:
* Подписка на пользователей.
* Создание, просмотр, изменение и удаление постов.
* Создание, просмотр, изменение и удаление комментариев.
* Создание и просмотр групп.


####Стек технологий

* Python
* Django
* djangorestframework
___

####Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:GucciMane204/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
___
#### Примеры запросов

* Получить JWT-токен
```
POST /api/v1/jwt/create/
body: {"username": "string", "password": "string"}
```
* Обновить JWT-токен
```
POST /api/v1/jwt/refresh/
body: {"refresh": "string"}
```
* Создание публикации
```
POST /api/v1/posts/
body: {"text": "string", "image": "string or null <binary>" group":"integer or null"}
```
* Получение комментария по его id
```
GET /api/v1/posts/{post_id}/comments/{id}/
```