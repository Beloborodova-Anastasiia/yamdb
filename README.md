# Проект YaMDb


### Описание

Проект YaMDb собирает отзывы  пользователей на произведения.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется рейтинг произведения.

API для "YaMDb" дает возможность взаимодействоть с функциональной частью "YaMDb" через API-сервис.

Проект упакован в docker-контейнер, что дает возможность легко развернуть его на любом компьютере.

Также проект делает автоматический запуск тестов, обновление образов на Docker Hub,автоматический деплой на боевой сервер при пуше в главную ветку main.


### Статус workflow

![Workflow status](https://github.com/Beloborodova-Anastasiia/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg
)

### Технологии

Python 3.7

Django 2.2.19

Docker 20.10.17

### Как запустить проект локально:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Beloborodova-Anastasiia/yamdb_final.git
```

```
cd yamdb_final/infra
```

Создать env-файл по следующему шаблону:

```
MY_KEY='Key django-project'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=PASSWORD
DB_HOST=db
DB_PORT=5432
```

Запустить сборку docker-контейнера:

```
для Windows и Mac:
docker-compose up -d --build
```
```
дляLinux:
sudo docker-compose up -d --build
```

Перенести данные в базу данных:

```
для Windows и Mac:
docker-compose exec web python manage.py loaddata fixtures.json
```
```
дляLinux:
sudo docker-compose exec web python manage.py loaddata fixtures.json
```

При необходимости создать суперюзера следующей командой:

```
для Windows и Mac:
docker-compose exec web python manage.py createsuperuser
```
```
дляLinux:
sudo docker-compose exec web python manage.py createsuperuser
```

Сайт администратора проекта доступен по адресу;

```
http://localhost/admin
```


### Примеры запросов к API

# Алгоритм регистрации пользователей

Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт /api/v1/auth/signup/.
YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и заполняет поля в своём профайле (описание полей — в документации).

Регистрация нового пользователя:

```
POST: /api/v1/auth/signup/
```
```
Тело запроса:
{
  "email": "string",
  "username": "string"
}
```
```
Ответ:
{
  "email": "string",
  "username": "string"
}
```

Получение JWT-токена:
```
POST: /api/v1/auth/token/
```
```
Тело запроса:
{
  "username": "string",
  "confirmation_code": "string"
}
```
```
Ответ:
{
  "token": "string"
}
```

Получение списка всех категорий

```
GET: /api/v1/categories/
```
```
Ответ:
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```

Добавление нового отзыва:

```
POST: /api/v1/titles/{title_id}/reviews/
```
```
Тело запроса:
{
  "text": "string",
  "score": 1
}
```
```
Ответ:
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

Изменение данных пользователя по username:


```
PATCH: /api/v1/users/{username}/
```
```
Тело запроса:
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
```
Ответ:
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```


### Автор

Белобородова Анастасия  beloborodova.anastasiia@yandex.ru