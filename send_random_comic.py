import os
from random import randint
import requests
import telegram
from dotenv import load_dotenv
from pathlib import Path


def download_random_comic():
    random_num = randint(1, 2933)
    url = f'https://xkcd.com/{random_num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comic = response.json()

    Path('files').mkdir(parents=True, exist_ok=True)
    image_path = Path('files/random_comic.png')
    with open(image_path, 'wb') as file:
        file.write(requests.get(comic['img']).content)

    return comic['alt']


def send_comic(id, telegram_bot):
    image_path = 'files\\random_comic.png'
    with open(image_path, 'rb'):
        telegram_bot.send_document(
            chat_id=id,
            document=open('files\\random_comic.png', 'rb')
        )


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_bot = telegram.Bot(token=telegram_bot_token)
    comic_alt = download_random_comic()
    id = '@apofiz_comics'
    download_random_comic()
    send_comic(id, telegram_bot)
    os.remove('files/random_comic.png')
