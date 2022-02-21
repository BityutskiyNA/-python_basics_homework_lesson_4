# -python_basics_homework_lesson_4

## Список рецептов

Сервис для хранения списка кулинарных рецептов

## Использование Docker

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

При первом запуске данный процесс может занять несколько минут.

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```
#### Применение миграций:

```bash
docker-compose run web python manage.py migrate
```


#### Создание суперпользователя

```bash
docker-compose run web python manage.py createsuperuser
```

#### Добавление фикстур

```bash
docker-compose run web python manage.py loaddata Ingredient Recipe
```

Проект доступен по адресу http://127.0.0.1:8000