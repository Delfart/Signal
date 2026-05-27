from telethon import TelegramClient, events
import feedparser
import asyncio
import requests
import os
import random

API_ID = 30421152
API_HASH = 'eed12ff5110226ece7a8e0566fb88e26'
BOT_TOKEN = '8772059051:AAHDVedn7QzlbvHELWup6KBd4anetZB9As4'
UNSPLASH_KEY = 'duRwdHJKE52sTaSEudYrCq1z9-wlUfvZQ3FtmJ2IF-w'

SOURCE_CHANNEL = 'goldusdsignalsprofessor11'
TARGET_CHANNEL = 'Signal_Filter_Hub'

SIGNATURES = [
    "\n--------------\nI'll help you pick a trusted broker - and tell you exactly when to enter the trade\nWant to start? DM me and I'll guide you personally -> @Goldcaptions",
    "\n--------------\nDon't know which broker to trust? I'll guide you step by step - from account setup to your first XAU/USD trade\nDrop @Goldcaptions a message and I'll take care of the rest.",
    "\n--------------\nI trade gold every day. I'll show you the entry, the target, and the broker that won't let you down\nReady to start? Reach out to @Goldcaptions directly.",
    "\n--------------\nStop guessing. Subscribe and get real-time signals + broker recommendations from someone who actually trades\nSend @Goldcaptions a DM and I'll get you started today."
]

def get_signature():
    return random.choice(SIGNATURES)

RSS_URL = 'https://www.investing.com/rss/news_25.rss'
posted_news = set()

user_client = TelegramClient('user_session', API_ID, API_HASH)
bot_client = TelegramClient('bot_session', API_ID, API_HASH)

def get_gold_photo():
    try:
        url = f'https://api.unsplash.com/photos/random?query=gold+trading&client_id={UNSPLASH_KEY}'
        response = requests.get(url)
        data = response.json()
        photo_url = data['urls']['regular']
        img_data = requests.get(photo_url).content
        with open('temp_photo.jpg', 'wb') as f:
            f.write(img_data)
        return 'temp_photo.jpg'
    except Exception as e:
        print(f"Ошибка фото: {e}")
        return None

async def post_news():
    while True:
        try:
            feed = feedparser.parse(RSS_URL)
            for entry in feed.entries[:3]:
                if entry.link not in posted_news:
                    posted_news.add(entry.link)
                    text = f"📰 {entry.title}\n\n{entry.link}{get_signature()}"
                    photo = get_gold_photo()
                    if photo:
                        await bot_client.send_file(TARGET_CHANNEL, photo, caption=text)
                        os.remove(photo)
                    else:
                        await bot_client.send_message(TARGET_CHANNEL, text)
                    print(f"Новость с фото опубликована: {entry.title[:50]}...")
                    await asyncio.sleep(5)
        except Exception as e:
            print(f"Ошибка новостей: {e}")
        await asyncio.sleep(1800)

async def main():
    await user_client.start()
    await bot_client.start(bot_token=BOT_TOKEN)
    print("Бот запущен! Слушаем канал и новости...")

    @user_client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handler(event):
        message = event.message
        text = message.text or getattr(message, 'caption', '') or ''
        full_text = text + get_signature()

        if message.photo:
            photo = await user_client.download_media(message.photo)
            await bot_client.send_file(TARGET_CHANNEL, photo, caption=full_text)
            print("Фото с подписью опубликовано!")

        elif message.document:
            doc = await user_client.download_media(message.document)
            await bot_client.send_file(TARGET_CHANNEL, doc, caption=full_text)
            print("Документ опубликован!")

        elif full_text.strip():
            photo = get_gold_photo()
            if photo:
                await bot_client.send_file(TARGET_CHANNEL, photo, caption=full_text)
                os.remove(photo)
            else:
                await bot_client.send_message(TARGET_CHANNEL, full_text)
            print(f"Сигнал опубликован: {text[:50]}...")

    await asyncio.gather(
        post_news(),
        user_client.run_until_disconnected()
    )

asyncio.run(main())



cat > main.py << 'EOF'
from telethon import TelegramClient, events
import feedparser
import asyncio
import requests
import os
import random

API_ID = 30421152
API_HASH = 'eed12ff5110226ece7a8e0566fb88e26'
BOT_TOKEN = '8772059051:AAHDVedn7QzlbvHELWup6KBd4anetZB9As4'
UNSPLASH_KEY = 'duRwdHJKE52sTaSEudYrCq1z9-wlUfvZQ3FtmJ2IF-w'

SOURCE_CHANNEL = 'goldusdsignalsprofessor11'
TARGET_CHANNEL = 'Signal_Filter_Hub'

SIGNATURES = [
    "\n--------------\nI'll help you pick a trusted broker - and tell you exactly when to enter the trade\nWant to start? DM me and I'll guide you personally -> @Goldcaptions",
    "\n--------------\nDon't know which broker to trust? I'll guide you step by step - from account setup to your first XAU/USD trade\nDrop @Goldcaptions a message and I'll take care of the rest.",
    "\n--------------\nI trade gold every day. I'll show you the entry, the target, and the broker that won't let you down\nReady to start? Reach out to @Goldcaptions directly.",
    "\n--------------\nStop guessing. Subscribe and get real-time signals + broker recommendations from someone who actually trades\nSend @Goldcaptions a DM and I'll get you started today."
]

def get_signature():
    return random.choice(SIGNATURES)

RSS_URL = 'https://www.investing.com/rss/news_25.rss'
posted_news = set()

user_client = TelegramClient('user_session', API_ID, API_HASH)
bot_client = TelegramClient('bot_session', API_ID, API_HASH)

def get_gold_photo():
    try:
        url = f'https://api.unsplash.com/photos/random?query=gold+trading&client_id={UNSPLASH_KEY}'
        response = requests.get(url)
        data = response.json()
        photo_url = data['urls']['regular']
        img_data = requests.get(photo_url).content
        with open('temp_photo.jpg', 'wb') as f:
            f.write(img_data)
        return 'temp_photo.jpg'
    except Exception as e:
        print(f"Ошибка фото: {e}")
        return None

async def post_news():
    while True:
        try:
            feed = feedparser.parse(RSS_URL)
            for entry in feed.entries[:3]:
                if entry.link not in posted_news:
                    posted_news.add(entry.link)
                    text = f"📰 {entry.title}\n\n{entry.link}{get_signature()}"
                    photo = get_gold_photo()
                    if photo:
                        await bot_client.send_file(TARGET_CHANNEL, photo, caption=text)
                        os.remove(photo)
                    else:
                        await bot_client.send_message(TARGET_CHANNEL, text)
                    print(f"Новость с фото опубликована: {entry.title[:50]}...")
                    await asyncio.sleep(5)
        except Exception as e:
            print(f"Ошибка новостей: {e}")
        await asyncio.sleep(1800)

async def main():
    await user_client.start()
    await bot_client.start(bot_token=BOT_TOKEN)
    print("Бот запущен! Слушаем канал и новости...")

    @user_client.on(events.NewMessage(chats=SOURCE_CHANNEL))
    async def handler(event):
        message = event.message
        text = message.text or getattr(message, 'caption', '') or ''
        full_text = text + get_signature()

        if message.photo:
            photo = await user_client.download_media(message.photo)
            await bot_client.send_file(TARGET_CHANNEL, photo, caption=full_text)
            print("Фото с подписью опубликовано!")

        elif message.document:
            doc = await user_client.download_media(message.document)
            await bot_client.send_file(TARGET_CHANNEL, doc, caption=full_text)
            print("Документ опубликован!")

        elif full_text.strip():
            photo = get_gold_photo()
            if photo:
                await bot_client.send_file(TARGET_CHANNEL, photo, caption=full_text)
                os.remove(photo)
            else:
                await bot_client.send_message(TARGET_CHANNEL, full_text)
            print(f"Сигнал опубликован: {text[:50]}...")

    await asyncio.gather(
        post_news(),
        user_client.run_until_disconnected()
    )

asyncio.run(main())
