import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random
import os

TOKEN = "9147022896:AAF6ADi1drIXe2JiJrcYuwOTV2YmorZPtME"
IMAGES_FOLDER = "images"

if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)

logging.basicConfig(level=logging.INFO)

messages_sister = [
    "يا ابن الوسخة، أنا دلوقتي بنكت أختك في طيزها وهي بترجيني أفشخها أكتر.",
    "أختك بعتتلي صورة كسها وبتقولي عايزة تتناك من صاحبك.",
    "شفت الصورة؟ ده كس أختك وأنا داخل فيه دلوقتي.",
    "يا ابن القحبة، أنا دلوقتي بفشخ أختك في طيزها الكبيرة وهي بترجيني أكتر وتقولي يفشخني.",
    "أختك بعتتلي صورة كسها المبلول وبتترجاني أدخل فيها بقوة وأفشخها قدامك.",
    "شفت الصورة؟ ده طيز أختك وأنا داخل فيها دلوقتي وبضربها لحد ما تصرخ.",
    "يا نياك، أختك بتقولي عايزة تتناك في طيزها من غير رحمة وأنا بعملها دلوقتي."
]

messages_mom = [
    "أمك دلوقتي تحتي وبتترجاني أفشخ طيزها.",
    "أمك بعتتلي صورة صدرها وطيزها وقالتلي إنها عايزاك تشوفها وهي بتتناك.",
    "يا نياك أمك، أنا خلّصت في طيزها وهي بتبكي من النشوة.",
    "أمك دلوقتي تحتي وبتترجاني أفشخ طيزها الكبيرة وأدخل فيها لآخره.",
    "أمك بعتتلي صورة صدرها وطيزها وقالتلي إنها عايزة تتناك بقوة وأنت تشوف.",
    "يا ابن الوسخة، أنا خلّصت في طيز أمك وهي بتبكي من النشوة وبترجيني أكتر.",
    "أمك بتدعك في كسها قدامي وبتقولي يفشخ طيزها بلا رحمة وأنا بعملها."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال. ابعتلي صور وأنا هخزنها، أو استخدم /sister أو /mom عشان أذلك.")

async def sister(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = random.choice(messages_sister)
    await update.message.reply_text(msg)
    images = os.listdir(IMAGES_FOLDER)
    if images:
        img = random.choice(images)
        with open(os.path.join(IMAGES_FOLDER, img), 'rb') as photo:
            await update.message.reply_photo(photo)

async def mom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = random.choice(messages_mom)
    await update.message.reply_text(msg)
    images = os.listdir(IMAGES_FOLDER)
    if images:
        img = random.choice(images)
        with open(os.path.join(IMAGES_FOLDER, img), 'rb') as photo:
            await update.message.reply_photo(photo)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    filename = f"{IMAGES_FOLDER}/{photo.file_id}.jpg"
    await file.download_to_drive(filename)
    await update.message.reply_text("الصورة اتحفظت. هبعتلك منها لما تطلب.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sister", sister))
    app.add_handler(CommandHandler("mom", mom))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.run_polling()

if _name_ == "_main_":
    main()
