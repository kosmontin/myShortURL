# Короткие ссылки

Учебная задача в рамках модуля "API веб-сервисов — Урок 2. Посчитайте клики по ссылкам" для учебной платформы [dvmn.org](https://dvmn.org)

Скрипт использует API сайта [bitly.com](https://bitly.com/) для сокращения ссылок, а так же для отображения счетчика переходов запрашиваемых "битлинков".

Скрипт работает как в режиме диалога, так и через аргументы командной строки

# Подготовка к использованию

Для запуска необходимо следующее:
- Установленный Python 3
- Установлены зависимости командой 
```commandline
pip install -r requirements.txt
```
- API TOKEN. Для этого необходимо зарегистрироваться на сайте [bitly.com](https://bitly.com/) и скопировать его в [личном кабинете](https://app.bitly.com/settings/api/)
- разместить в общей папке с проектом файл .env, в котором сохранить TOKEN в формате:
```
BITLY_TOKEN = ваш_ключ
``` 
### Примечание
В качестве примера, в папке проекта есть файл `.env.EXAMPLE`, который можно перименовать и заполнить своими данными. 

# Использование

Для запуска скрипта необходимо воспользоваться командой:
```
python shorten_url.py [<URL>]
```

### Примеры вывода

```
$ python shorten_url.py
Введите ссылку: https://www.google.com/maps/@55.7356077,37.5039418,10z
Битлинк:  https://bit.ly/3LlYyUn
```
```
$ python shorten_url.py
Введите ссылку: https://bit.ly/3uD7cZ0
По вашей ссылке прошли: 2 раз(а)
```
```
$ python shorten_url.py https://bit.ly/3uD7cZ0
По вашей ссылке прошли: 2 раз(а)
```
