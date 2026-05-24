# FoodAdapter

FoodAdapter — современный веб-проект доставки еды на Flask, HTML5, CSS3, JavaScript и Bootstrap 5.

## О проекте

В корне проекта находится Flask-приложение с динамическим сервером, шаблонами Jinja2 и API для корзины.

### Локальный запуск Flask

1. Откройте PowerShell в корне проекта.
2. Создайте и активируйте виртуальное окружение:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

3. Установите зависимости:

```powershell
pip install -r requirements.txt
```

4. Запустите приложение:

```powershell
python run.py
```

5. Откройте в браузере:

```
http://127.0.0.1:5000
```

## GitHub Pages

GitHub Pages не может запускать Flask-сервер. Поэтому для GitHub Pages добавлен статический демо-сайт в папке docs/.

### Статический сайт на GitHub Pages

- Содержимое docs/ доступно как статический сайт.
- Чтобы открыть на GitHub Pages, в настройках репозитория установите источник Pages на docs/.
- После этого сайт будет доступен по адресу:

```
https://Dava0709.github.io/kursovayaMaksimka/
```

### Что будет доступно на GitHub Pages

- Статическая главная страница с дизайном вашего проекта.
- Статические страницы cart.html и checkout.html.
- Динамическая корзина и реальный серверный Checkout работать не будут.

## Структура проекта

```text
FoodAdapter/
  adapters/
  models/
  services/
  static/
    css/
    js/
  templates/
  docs/
    index.html
    cart.html
    checkout.html
    css/
      style.css
    .nojekyll
  app.py
  run.py
  requirements.txt
  README.md
```

## Репозиторий

https://github.com/Dava0709/kursovayaMaksimka
