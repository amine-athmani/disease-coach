import os
import logging
from telegram import Update, __version__ as TG_VER
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
)
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
AI71_API_KEY = os.getenv("AI71_API_KEY")

# Set up OpenAI client
client = openai.OpenAI(api_key=AI71_API_KEY, base_url="https://api.ai71.ai/v1/")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define states for the ConversationHandler
CHOOSING, TYPING_REPLY = range(2)

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        'Hello! I am your assistant specialized in Types 1 diabetes. How can I assist you today?'
    )
    return CHOOSING

# Define a function to handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_input = update.message.text
    messages = [
        {"role": "assistant", "content": "You are an expert assistant specializing in Type 1 diabetes. Provide tips, advice, and answer questions specifically related to Type 1 diabetes."},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(model="tiiuae/falcon-180b-chat", messages=messages)
    bot_response = response.choices[0].message.content
    await update.message.reply_text(bot_response)

    # After responding, go back to the CHOOSING state to allow for more interactions
    return CHOOSING

# Define the cancel command handler
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Goodbye! Feel free to reach out anytime you need assistance.')
    return ConversationHandler.END

# Main function to set up the bot
def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
