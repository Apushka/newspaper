# Приложение Newspaper (Django Rest Framework)

http://81.163.29.113

## Установкa

    mkdir newspaper-app

    cd newspaper-app

    python3 -m venv venv
    source venv/bin/activate

    git clone https://github.com/Apushka/newspaper.git

    cd newspaper

    Переименовать .env.example в .env и заполнить нужными данными
    
    Для генерации SECRET_KEY в консоли:
    python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

    pip install -r requirements.txt

## Запуск приложения

     python3 manage.py runserver

# REST API

    Эндпоинты

## API Routes

### Локально
`http://127.0.0.1:8000/api`

### Демо
`http://81.163.29.113/api`

## Админ

    username: admin
    password: admin

## Регистрация нового пользователя

### Запрос

`POST /register/`

    {
        "username": "username",
        "password": "password",
        "password2": "password"
    }

### Ответ

    {
        "username": "username"
    }

## Войти с именем пользователя и паролем

### Запрос

`POST /auth/`

    {
        "username": "username",
        "password": "password"
    }

### Ответ

    {
        "token": "64dfertbc21bae7537987f6a86d0da46f586681992d2e"
    }

## Получить список новостей

### Запрос

`GET /news/`

### Ответ

    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "title": "new title",
                "content": "new content",
                "author": "author",
                "created": "2023-11-26T21:49:46.242592Z",
                "comments": [],
                "likes_count": 0,
                "comments_count": 0
            },
            ...
    ]

}

## Получить одну новость

### Запрос

`GET /news/1`

### Ответ

    {
        "id": 1,
        "title": "new title",
        "content": "new content",
        "author": "author",
        "created": "2023-11-26T21:00:35.440518Z",
        "comments": [],
        "likes_count": 0,
        "comments_count": 0
    }

## Создать новость

### Запрос

`POST /news/`

    {
        "title": "new title",
        "content": "new content"
    }

### Ответ

    {
        "id": 1,
        "title": "new title",
        "content": "new content",
        "author": "author",
        "created": "2023-11-27T10:21:15.810186Z",
        "comments": [],
        "likes_count": 0,
        "comments_count": 0
    }

## Редактировать новость

### Запрос

`PUT /news/1`

    {
        "title": "new title",
        "content": "new content"
    }

### Ответ

    {
        "id": 1,
        "title": "new title",
        "content": "new content",
        "author": "author",
        "created": "2023-11-27T10:21:15.810186Z",
        "comments": [],
        "likes_count": 0,
        "comments_count": 0
    }

## Удалить новость

### Запрос

`DELETE /news/1`

## Создать комментарий к новости

### Запрос

`POST /comments/`

    {
        "content": "comment",
        "new": 1
    }

### Ответ

    {
        "id": 1,
        "created": "2023-11-27T08:45:10.975630Z",
        "content": "comment",
        "author": "author",
        "new": 1
    }

## Редактировать комментарий

### Запрос

`PUT /comments/1`

    {
        "content": "comment edited"
    }

### Ответ

    {
        "id": 1,
        "created": "2023-11-27T08:43:43.546624Z",
        "content": "comment edited",
        "author": "author",
        "new": 1
    }

## Удалить комментарий

### Запрос

`DELETE /comments/1`

## Поставить/удалить лайк новости

### Запрос

`PUT /likes/:new_id`

### Ответ

    {
        "id": 1,
        "title": "new title",
        "content": "new content",
        "author": "author",
        "created": "2023-11-26T21:00:35.440518Z",
        "comments": [],
        "likes_count": 0,
        "comments_count": 0
    }
