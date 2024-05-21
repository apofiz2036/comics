import os
from random import randint
import requests
import telegram
from dotenv import load_dotenv
import argparse


def download_random_comic():
    start_comic_id = 1
    end_comic_id = 2933
    random_num = randint(start_comic_id, end_comic_id)
    url = f'https://xkcd.com/{random_num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comic = response.json()

    with open(image_path, 'wb') as file:
        file.write(requests.get(comic['img']).content)

    return comic['alt']


def send_comic(chat_id, telegram_bot, image_path):
    with open(image_path, 'rb') as file:
        telegram_bot.send_document(
            chat_id=chat_id,
            document=file
        )


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_bot = telegram.Bot(token=telegram_bot_token)

    os.makedirs('files', exist_ok=True)
    image_path = os.path.join('files', 'random_comic.png')
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    try:
        comic_alt = download_random_comic()
        send_comic(chat_id, telegram_bot, image_path, )
    finally:
        os.remove(image_path)
