# Simple Weather API with Yandex Backend

## How to run
1. Create virtualenv
2. Install dependencies with
```
$ pip install -r requirements.txt
```
3. Apply migrations with:
```
$ python manage.py migrate
```
4. Load fixture with all cities:
```
$ python manage.py loaddata weather/fixtures/City.json --app weather.City
```
5. Get your personal API key from yandex: [see docs](https://yandex.ru/dev/weather/doc/dg/concepts/about.html#about__onboarding)
6. Run server with YANDEX_API_KEY env variable like this:
```
$ YANDEX_API_KEY=<your_key> python ./manage.py runserver
```
7. Visit page
```
http://127.0.0.1:8000/weather?city=<название_на_русском>
```

## How to start Telegram Bot
1. Run Django backend as described above
2. Register your bot with `@BotFather`
3. In same venv as Django backend run `telegram_bot/main.py` with key as env variable:
```
$ TG_API_KEY=<your_bot_key> python ./telegram_bot/main.py
```
4. Open your bot in Telegram

## Troubleshooting
If you can't connect to Django server, you may need to change variable `WEATHER_API_URL` in `telegram_bot/config.py`. It should point to your running Django server instance.
