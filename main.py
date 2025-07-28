from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, ContextTypes
from datetime import datetime
import pytz

TOKEN = "7259725892:AAHU6l388Sdc0pu3xNrs08DF7pLfiVbBQ8s"

def generate_signal_now():
    time_now = datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%H:%M")
    return f"""📊 Sinyal Saat Ini
🗓️ Tanggal: {datetime.now(pytz.timezone("Asia/Jakarta")).strftime('%d-%m-%Y')} | WIB
⏱️ Jam: {time_now}

Asia Composite: {time_now} - B
Crypto Composite: {time_now} - S (lemah)
Europe Composite: {time_now} - B
Nusantara Halal: {time_now} - B
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 Sinyal Sekarang", callback_data='sinyal_sekarang')],
        [InlineKeyboardButton("📆 Sinyal 24 Jam", callback_data='sinyal_24jam')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selamat datang di VanTrader Bot VVIP 🚀\nSilakan pilih menu:", reply_markup=reply_markup)

async def sinyal_sekarang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=generate_signal_now())

async def sinyal_24jam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = "📆 Sinyal 24 Jam (00:00–23:55 WIB):\n\n"
    for h in range(0, 24):
        for m in range(0, 60, 5):
            jam = f"{h:02}:{m:02}"
            text += f"{jam} - B\n"
    await query.edit_message_text(text=text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
