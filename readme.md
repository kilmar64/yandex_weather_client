# Simple Weather API with Yandex Backend

## How to run
1. Create virtualenv
2. Install dependencies with
```
$ pip install -r requirements.txt
```
3. Get your personal API key from yandex: [see docs](https://yandex.ru/dev/weather/doc/dg/concepts/about.html#about__onboarding)
4. Run server with YANDEX_API_KEY env variable like this:
```
$ YANDEX_API_KEY=<your_key> python ./manage.py runserver
```
5. Visit page
```
http://127.0.0.1:8000/weather?city=<название_на_русском>
```