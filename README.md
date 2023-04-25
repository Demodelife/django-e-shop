# E-shop "Megano"
Simple e-shop based on DRF.

## Main External Libraries
* Django               4.1.7
* djangorestframework  3.14.0
* drf-yasg             1.21.5
* frontend             0.2
* Jinja2               3.1.2
* et al.

# Интернет-магазин "Megano"
Простой интернет-магазин, основанный на DRF.

## Installation
1. Clone all the contents of the repository to your working directory.
2. Install all libraries from the requirements.txt file: `pip install -r requirements.txt`.
3. Run the migrations in root project: 
   * `python manage.py makemigrations`
   * `python manage.py migrate`.
4. Create superuser: `python manage.py createsuperuser`.
5. Run server: `python manage.py runserver`
6. Navigate to the suggested URL in the console (127.0.0.1:8000).
7. Log in to the administrator site with the username and password of the superuser.
   * http://127.0.0.1:8000/admin/
8. To load fixtures, use the commands:
   * for load users: `python manage.py loaddatta fixtures/users-fixtures-data.json`
   * for load products: `python manage.py loaddatta fixtures/products-fixtures-data.json`
   * for load orders: `python manage.py loaddatta fixtures/orders-fixtures-data.json`

## Important Points
* At the root there is a `frontend` directory responsible 
  for the frontend. Changing the files there, 
  you need to remove the frontend package 
  from your virtual environment to build the package again. 
  Instructions in the `README.md` file in the same place.
* All `manage.py` commands are executed directly in the `backend` directory

## Установка
1. Склонируйте все содержимое репозитория в свой рабочую директорию.
2. Установите все библиотеки из файла requirements.txt: `pip install -r requirements.txt`.
3. Запустите миграцию в корневом проекте:
    * `python manage.py makemigrations`
    * `миграция python manage.py`.
4. Создайте суперпользователя: `python manage.py createsuperuser`.
5. Запустите сервер: `python manage.py runserver`
6. Перейдите к предложенному URL-адресу в консоли (127.0.0.1:8000).
7. Войдите на сайт администратора с именем пользователя и паролем суперпользователя.
    * http://127.0.0.1:8000/админ/
8. Для загрузки фикстур используйте команды:
    * для загрузки пользователей: `python manage.py loaddatta Fixtures/users-fixtures-data.json`
    * для загрузки продуктов: `python manage.py loaddatta Fixtures/products-fixtures-data.json`
    * для загрузки заказов: `python manage.py loaddatta Fixtures/orders-fixtures-data.json`

## Важные Моменты
* В корне находится директория `frontend`, отвечающая за
   интерфейс веб-приложения. Меняя файлы там,
   вам нужно удалить пакет
   из вашей виртуальной среды, чтобы снова собрать пакет.
   Инструкция в файле `README.md` там же.
* Все команды `manage.py` выполняются непосредственно в директории `backend`, 
  где находится файл `manage.py`.