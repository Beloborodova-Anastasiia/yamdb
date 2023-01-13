# Project YaMDb

![Workflow status](https://github.com/Beloborodova-Anastasiia/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg
)

### Description

The YaMDb project collects user's reviews on works of art.

The works of ast themselves are not stored in YaMDb.
Users can write text review on work, rate the work in the range from one to ten. From user's ratings  is formed the rating.

Interraction with functional part od YaMDb occurs through API-servise.

The project is packaged in a docker container. 

In the project is configured Git-actiont. It makes authomatic tests runing and Docker Hub images updating.

### Technologies

Python 3.7

Django 2.2.19

Django REST framework 3.12.4

Docker 20.10.17

### Local project run:

Clone a repository and navigate to it on the command line:

```
git clone git@github.com:Beloborodova-Anastasiia/yamdb.git
```

```
cd yamdb/infra
```

Create env-file by template:

```
MY_KEY='Key django-project'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=PASSWORD
DB_HOST=db
DB_PORT=5432
```

Run build docker-container:

```
for Windows or Mac:
docker-compose up -d --build
```
```
for Linux:
sudo docker-compose up -d --build
```

Move data to database:

```
for Windows or Mac:
docker-compose exec web python manage.py loaddata fixtures.json
```
```
for Linux:
sudo docker-compose exec web python manage.py loaddata fixtures.json
```

Create a superuser if necessary:

```
for Windows or Mac:
docker-compose exec web python manage.py createsuperuser
```
```
for Linux:
sudo docker-compose exec web python manage.py createsuperuser
```

The project administrator's website is available at:

```
http://localhost/admin

```
Project's documentation is available at:

```
http://localhost/redoc
```

### API request examples

# New user's registration algorithm

User sends POST-request at endpoint /api/v1/auth/signup/ with parameters: email address and username.
The servise sends email with confirmation code on the email address.
Then users sends at endpoint /api/v1/auth/token/ POST-request with parammeters:
usernsame, confirmation code. User recieves JWT-token in the response.
User edits his profile to send PATCH-request at endpoint /api/v1/users/me/ if hi wants.


New user registration:

```
POST: /api/v1/auth/signup/
```
```
Request body:
{
  "email": "string",
  "username": "string"
}
```
```
Response:
{
  "email": "string",
  "username": "string"
}
```

JWT-ещлут receiving:
```
POST: /api/v1/auth/token/
```
```
Request body:
{
  "username": "string",
  "confirmation_code": "string"
}
```
```
Response:
{
  "token": "string"
}
```

All categories receiving:

```
GET: /api/v1/categories/
```
```
Response:
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

New review adding:

```
POST: /api/v1/titles/{title_id}/reviews/
```
```
Request body:
{
  "text": "string",
  "score": 1
}
```
```
Response:
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

Profile changing:

```
PATCH: /api/v1/users/{username}/
```
```
Request body:
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
Response:
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```


### Author

Anastasiia Beloborodova 

anastasiia.beloborodova@gmail.com