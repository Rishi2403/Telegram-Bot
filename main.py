import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN=os.getenv("TOKEN")

def start(update , context):
    update.message.reply_text("Hey there !! Welcome to Rishi's kingdom.")



def helpme(update, context):
    update.message.reply_text(

        """

        Hi There ! I'm Telegram bot created by Rishi. Ye command follow karo toh mujhe paoge :-

        /start - Toh shuru karne ke liye humse baat
        /about - To know who am I
        /contact - where u can fetch me
        /help - help karne ke liye 
        /hi - to talk


        I hope this helps ;)

        """
    )

def about(update, context):
    update.message.reply_text(

        """
         I am Rishi striving to learn new tech and also love geopolitics ,
           travelling , adventures , exploring different places
       

        """
    )



def contact(update, context):
    update.message.reply_text(

        """
        u can contact me at rishibhattasali@gmail.com
         
        """
    )
def hi (update, context):
    update.message.reply_text(

        """
            Hey there ! How are you doing??
         
        """
    )
def handle_message(update,context):
    update.message.reply_text(f"You said {update.message.text}")

updater=telegram.ext.Updater(TOKEN, use_context=True)
dispatch=updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start',start))
dispatch.add_handler(telegram.ext.CommandHandler('help',helpme))
dispatch.add_handler(telegram.ext.CommandHandler('about',about))
dispatch.add_handler(telegram.ext.CommandHandler('contact',contact))
dispatch.add_handler(telegram.ext.CommandHandler('hi',hi))


dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text ,handle_message))
updater.start_polling()
updater.idle()
