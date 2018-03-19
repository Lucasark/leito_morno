from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, CallbackQueryHandler)
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

OPTIONS, LOCALSAI, LOCALCHE = range(3)

def b2(bot, update):
    keyboard = [[InlineKeyboardButton("Saindo...", callback_data='0'), InlineKeyboardButton("Chegando...", callback_data='1')],
        [InlineKeyboardButton("Parado no DCE!", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(chat_id=update.message.chat_id, text="O bus UFF esta...", reply_markup=reply_markup)
    return OPTIONS


def options(bot, update):
    query = update.callback_query
    user = update.message.from_user
    logger.info("Option of %s: %s" % (user.first_name, update.message.text))

    if query == '0':
        keyboard = [[InlineKeyboardButton("TESTE1", callback_data='0'), InlineKeyboardButton("TESTE2", callback_data='1')],
            [InlineKeyboardButton("TESTE3", callback_data='2'), InlineKeyboardButton("TESTE4", callback_data='4')]]

        bot.send_message(chat_id=update.message.chat_id, text="...saindo do...", reply_markup=ReplyKeyboardRemove())
        return LOCALSAI

    if query == '1':
        keyboard = [[InlineKeyboardButton("TESTE1", callback_data='0'), InlineKeyboardButton("TESTE2", callback_data='1')],
            [InlineKeyboardButton("TESTE3", callback_data='2'), InlineKeyboardButton("TESTE4", callback_data='4')]]

        bot.send_message(chat_id=update.message.chat_id, text="...chegando no...", reply_markup=ReplyKeyboardRemove())
        return LOCALCHE

    else:
        bot.send_message(chat_id=update.message.chat_id, text="Estou parado no DCE! by %s" % user.first_name, reply_markup=ReplyKeyboardRemove())
        logger.info("User %s parado no DCE" % user.first_name)
        return

#Para ser chamado quando o botão "Saindo" é precionado, criando um novo menu / It is to be a new menu when "Saindo" is pressed
def localsai(bot, update):
    query = update.callback_query
    user = update.message.from_user

    if query == '0':
        bot.send_message(text="%s disse esta saindo do TESTE1")
        logger.info("%s - SAINDO - TESTE1" % user.first_name)
    if query == '1':
        bot.send_message(text="%s disse esta saindo do TESTE2")
        logger.info("%s - SAINDO - TESTE2" % user.first_name)
    if query == '2':
        bot.send_message(text="%s disse esta saindo do TESTE3")
        logger.info("%s - SAINDO - TESTE3" % user.first_name)
    else:
        bot.send_message(text="%s disse esta saindo do TESTE4")
        logger.info("%s - SAINDO - TESTE4" % user.first_name)

    return

#Para ser chamado quando o botão "chegando" é precionado, criando um novo menu / It is to be a new menu when "Chegando" is pressed 
def localche(bot, update):
    query = update.callback_query
    user = update.message.from_user

    if query == '0':
        bot.send_message(text="%s disse esta chegando do TESTE1")
        logger.info("%s - chegando - TESTE1" % user.first_name)
    if query == '1':
        bot.send_message(text="%s disse esta chegando do TESTE2")
        logger.info("%s - chegando - TESTE2" % user.first_name)
    if query == '2':
        bot.send_message(text="%s disse esta chegando do TESTE3")
        logger.info("%s - chegando - TESTE3" % user.first_name)
    else:
        bot.send_message(text="%s disse esta chegando do TESTE4")
        logger.info("%s - chegando - TESTE4" % user.first_name)

    return

def cancel(bot, update):
    user = update.message.from_user
    logger.info("%s cancelou interacao." % user.first_name)
    update.message.reply_text('Cancelado', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():

    updater = Updater("TOKEN")

    dp = updater.dispatcher

    #Ainda não to entendo como usar o QueryHandler / Stil don't undestanding how to use QueryHandler

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('b2', b2)],
        states=
        {
            OPTIONS: [CallbackQueryHandler(options)],

            LOCALCHE: [CallbackQueryHandler(localche)],

            LOCALSAI: [CallbackQueryHandler(localsai)]
        },
        fallbacks = [CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
