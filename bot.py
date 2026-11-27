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
    "أختك بعتتلي صورة كسها المبلول وبتقولي عايزة تتناك من غير رحمة.",
    "شفت الطيز دي؟ ده طيز أختك وأنا داخل فيها دلوقتي وبضربها بقوة.",
    "يا نياك، أختك بتركع قدامي وبتمص قضيبي وبتترجاني أفشخ طيزها بعد كده.",
    "أختك بتدعك في كسها قدامي وبتقولي إنها عايزة صاحبك يفشخها مش أنت.",
    "أنا خلّصت في طيز أختك وهي بتبكي من النشوة وبترجيني أكمل.",
    "أختك لابسة الكلوت الوردي وبتفتح رجليها وتقولي يفشخ الطيز دي.",
    "يا ابن القحبة، أختك بتبعتلي فيديو وهي بتدعك في كسها وبتترجاني أجي أفشخها.",
    "طيز أختك كبيرة أوي وأنا بضربها دلوقتي وهي بتصرخ يا صاحبي أعمق.",
    "أختك قالتلي إنها عايزة تتناك في طيزها قدامك عشان تتشمت.",
    "أنا داخل في كس أختك دلوقتي وهي مبلولة أوي وبتترجاني أروح للطيز.",
    "يا نياك أختك، هي بعتتلي صورة صدرها وطيزها وقالتلي خدني.",
    "أختك بتترجاني أفشخ طيزها بلا رحمة وأنا بعملها دلوقتي.",
    "شفت الصورة؟ ده كس أختك وأنا بلحسه وبدخله دلوقتي.",
    "أختك بتقولي إنها ملكي النهاردة وهتتناك في كل حتة."
]

messages_mom = [
    "أمك دلوقتي تحتي وبتترجاني أفشخ طيزها الكبيرة لآخره.",
    "يا ابن الوسخة، أمك بعتتلي صورة كسها وبتقولي عايزة صاحبك يفشخها.",
    "أمك بتركع وبتمصني وبتترجاني أدخل في طيزها بعد كده.",
    "أنا خلّصت في طيز أمك وهي بتبكي وبترجيني أكتر.",
    "أمك لابسة الكلوت وبتفتح رجليها وتقولي يفشخ الطيز دي قدام ابنها.",
    "يا نياك أمك، هي بتدعك في كسها وبتترجاني أفشخها بقوة.",
    "أمك قالتلي إنها عايزة تتناك في طيزها وأنت تتفرج.",
    "طيز أمك كبيرة وأنا بضربها دلوقتي وهي بتصرخ.",
    "أمك بتبعتلي فيديو وهي بتدعك وبتقولي تعالى يفشخني.",
    "أنا داخل في كس أمك وهي مبلولة وبتترجاني أروح للطيز.",
    "يا ابن القحبة، أمك بتتناك مني دلوقتي وبتترجاني أعمق.",
    "أمك بعتتلي صورة صدرها الكبير وطيزها وقالتلي خدني يا صاحبي ابني.",
    "أمك بتترجاني أفشخ طيزها بلا رحمة وأنا بعملها.",
    "شفت الصورة؟ ده طيز أمك وأنا داخل فيه دلوقتي.",
    "أمك بتقولي إنها عايزة تتناك كل يوم من صاحبك مش من ابنها."
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

if __name__ == "__main__":
    main()
