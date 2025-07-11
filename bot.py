from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# 📌 IDs de los canales
CANAL_MADRE = -1002696641261
CANALES_DESTINO = [-1002571474161, -1002381224215]

# 🔐 Token del bot
BOT_TOKEN = "7797698567:AAFUCmY71DgZdNyteRl6RnaXp2c14rcGKCM"

app = ApplicationBuilder().token(BOT_TOKEN).build()

async def reenviar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == CANAL_MADRE:
        for destino in CANALES_DESTINO:
            try:
                await context.bot.copy_message(
                    chat_id=destino,
                    from_chat_id=CANAL_MADRE,
                    message_id=update.message.message_id
                )
            except Exception as e:
                print(f"❌ Error al reenviar a {destino}: {e}")

app.add_handler(MessageHandler(filters.ALL, reenviar))

print("✅ Bot corriendo...")
app.run_polling()
