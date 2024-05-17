# Отправка в телеграмм случайного комикса xkcd

Эта программа позволяет отправлять случайный комикс xkcd в группу или телеграмм канал. Сначала комикс загружается в папку files, затем отпавляется телеграмм ботом в группу или канал. После отправки изображение удаляется.

## Установка
Для работы программы требуется  Python 3.6 или выше, библиотека requests версии 2.31.0, библиотека python-dotenv версии 1.0.1 и python-telegram-bot версии 13.0.

Все библиотеки прописаны в файле requirements.txt для их быстрой установки можно использовать команду:

```shell
 pip install -r requirements.txt.
```

Для работы требуется указать токен телеграмм бота. Прописать ключ нужно в файле .env следующим образом:

```.env
TELEGRAM_BOT_TOKEN=ваш токен
```
## Использование

Для работы программы требуется прописать следующую команду в консоли:

```shell
python send_random_comic.py
```

Дополнительные параметры не требуются

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.