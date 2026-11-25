# Demo

Сайт для записи на курсы вождения.

## Стек
- Python 3.13
- Django 6.0
- PostgreSQL
- pytest + pytest-django

## Установка и запуск

1. Создай и активируй виртуальное окружение:
python -m venv venv
source venv/bin/activate

2. зависимости:
pip install -r requirements.txt

3. .env по примеру .env.example и укажи настройки.

4.  миграции:
python manage.py migrate

5.  фикстуры (по порядку):
python manage.py loaddata fixtures/accounts.json
python manage.py loaddata fixtures/staff.json
python manage.py loaddata fixtures/students.json
python manage.py loaddata fixtures/courses.json
python manage.py loaddata fixtures/requests.json

6. сервер:
python manage.py runserver

## Тестовые аккаунты
- Админ: admin26 / demo20
- Студент: first / firstpswrd
- Учитель: teach1 / qwerfghnjk

## Тесты
- pytest