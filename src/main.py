import telegram.ext as tgx
import telegram
import db


def buy(update: tgx.Update, context: tgx.ContextTypes.DEFAULT_TYPE):
    category: str = context.args[0]
    amount: int = context.args[1]
    db.write(category, amount)


def sell(update: tgx.Update, context: tgx.ContextTypes.DEFAULT_TYPE):
    category: str = context.args[0]
    amount: int = context.args[1]
    db.write(category, amount)


def merge(update: tgx.Update, context: tgx.ContextTypes.DEFAULT_TYPE):
    category: str = context.args[0]
    amount: int = context.args[1]
    db.patch(category, amount)


def cancel(update: tgx.Update, context: tgx.ContextTypes.DEFAULT_TYPE):
    category: str = cash(-1)
    amount: int = context.args[1]
    db.remove(category, amount)


def view(update: tgx.Update, context: tgx.ContextTypes.DEFAULT_TYPE):
    bot.send_message(chat_id=update.effective_chat.id, text=db_read())


if __name__ == '__main__':
    from os import getenv
    from dotenv import load_dotenv
    dotenv.load_dotenv()

    bot = tgx.ApplicationBuilder.token(
        os.getenv('TOKEN')
    ).build()

    bot.add_handler(
        tgx.CommandHandler('b', buy)
    )
    bot.add_handler(
        tgx.CommandHandler('s', sell)
    )
    bot.add_handler(
        tgx.CommandHandler('v', view)
    )

    bot.run_polling(poll_interval=2.0)