
from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram.ext.dispatcher import run_async
import pickle

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

#------------------------------
#------------------------------
GET_TEXT=1

def cancel(bot, update,user_data):
    user = update.message.from_user
    #logger.info("User %s canceled the conversation." % user.first_name)
    update.message.reply_text('aborted :) ',reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
#@run_async
def start(bot, update,user_data):
    update.message.reply_text("'Hi! I keep track of machine learning books on uploaded on dropbox maintained by @machinelearning group.\nUse /start to activate the bot \nEnter any book or author keyword to search")
    return 1
#@run_async
def get_text(bot, update,user_data):
    inp = update.message.text
    print(inp)
    flag = True
    with open('filenames.pickle', 'rb') as fp:
        filenames=pickle.load(fp)
    #print(filenames)
    for i in filenames:
        if inp.lower() in i.lower():
            print(i)
            flag = False
            bot.send_message(update.message.chat_id,i)
    if flag:
        bot.send_message(update.message.chat_id,"Sorry book not found :(")
        
    return GET_TEXT
    
def main():
    t=''
    updater = Updater(t)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start,pass_user_data=True)],

        states={
            GET_TEXT: [MessageHandler(Filters.text, get_text,pass_user_data=True),CommandHandler('cancel', cancel,pass_user_data=True)],
        },
        fallbacks=[CommandHandler('cancel', cancel,pass_user_data=True)]
    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
