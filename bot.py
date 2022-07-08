import time
import os
import telegram
from telegram import *
from telegram import TelegramError
from telegram import parsemode
from telegram.ext import *
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import datetime

# from Chatbot import chat

load_dotenv()

tkn = "TOKEN"

FN, LN, EMAIL, COUNTRY, STATE, COMPANYN, COMPANYW = range(7)

bot = Bot(os.getenv(tkn))
updater = Updater(os.getenv(tkn), use_context=True)

dispatcher = updater.dispatcher

cluster = MongoClient(
    "REMOVED THIS FOR SECURITY PURPOSE. COPY PASTE AGAIN FROM MONGODB ATLAS :)"
)
if cluster:
    print("Connected")

db = cluster["demo-bot"]
collection = db["registrations"]

model = {
    "_id": "",
    "username": "",
    "chat_id": "",
    "registration_date": datetime.datetime.today().replace(microsecond=0),
}

boring = False


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = update._effective_user.id
    message_id = update._effective_message.message_id
    first_name = update._effective_user.first_name
    last_name = update._effective_user.last_name
    username = update._effective_user.username
    query.answer()

    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    choice = query.data
    bot.send_chat_action(chat_id, action="typing")

    if choice == "boring-y":
        global boring
        try:
            bot.send_animation(
                chat_id,
                animation="https://media.giphy.com/media/fxU6WfJ8eembhmZBC6/giphy.gif",
                caption="I'm really sorry 🙁\n\nI'll finish my explanation in just next two messages.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(2)
        except:
            bot.send_message(
                chat_id,
                text="I'm really sorry 🙁\n\nI'll finish my explanation in just next two messages.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(2)

        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/HAUxypcipk4AvnHdp0/giphy.gif",
                caption=f"<b>4.</b> I can be used as a medium between you and your customers or students. \n  • I can clear their most common doubts instead of you",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        except:
            bot.send_message(
                chat_id=chat_id,
                text=f"<b>4.</b> I can be used as a medium between you and your customers or students. \n  • I can clear their most common doubts instead of you",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/qKltgF7Aw515K/giphy.gif",
                caption=f"<b>5.</b> I can be used as a medium to collect information Feedback or Queries or Issues from customers and store it into your personal database  and you can go-through it later on an interactive desktop application developed by us.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        except:
            bot.send_message(
                chat_id=chat_id,
                text=f"<b>5.</b> I can be used as a medium to collect information Feedback or Queries or Issues from customers and store it into your personal database and you can go-through it later on an interactive desktop application developed by us.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)

        bot.send_message(
            chat_id=chat_id,
            text=f"Finally, These <b>alone are not my limitations</b>, I can be customized as per your needs and I can be added with functionalities as per your requirements. 🤩",
            parse_mode=ParseMode.HTML,
        )
        time.sleep(4)
        bot.send_message(
            chat_id=chat_id,
            text=f"That's all from my side, I think I've explained enough and Kept a Boring-Less conversation",
            parse_mode=ParseMode.HTML,
        )

        time.sleep(4)
        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/brHaCdJqCXijm/giphy.gif",
                caption=f"You can contact @Lahfir for further details. Thanks for your patience and Nice talking with you 😊.\n\nI'm so curious to be a part of your Business or Group 😁.",
                parse_mode=ParseMode.HTML,
            )
        except:
            bot.send_message(
                chat_id=chat_id,
                text=f"You can contact @Lahfir for further details. \n\nThanks for your patience and Nice talking with you 😊.\n\nI'm so curious to be a part of your Business or Group 😁.",
                parse_mode=ParseMode.HTML,
            )
        bot.send_message(
            chat_id,
            "You can use the following commands to chat with me\n\n<b>1.</b> /start - I will start explaining about me and my functionalities\n<b>2.</b> /about - Use this command to know about me <i>in detail</i>\n<b>3.</b> /functionality - Use this command to see my functionalities <i>in detail</i>",
            parse_mode=ParseMode.HTML,
        )
        message = bot.send_message(
            chat_id, "<b>Processing Photo...</b>", parse_mode=ParseMode.HTML
        )

        try:
            while True:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=open("Functionalities.png", "rb"),
                    caption="This photo explains the functionalities of Myself",
                )
                bot.delete_message(
                    chat_id=chat_id,
                    message_id=message.message_id,
                )
                message = bot.send_message(
                    chat_id, "<b>Processing Video...</b>", parse_mode=ParseMode.HTML
                )
                bot.send_video(
                    chat_id=chat_id,
                    video=open("Web-App Exp-1.m4v", "rb"),
                    caption="This video explains the functionalities of the Web-App",
                    supports_streaming=True,
                )
                break
            bot.delete_message(
                chat_id=chat_id,
                message_id=message.message_id,
            )
        except telegram.error.NetworkError as e:
            print(e)
            bot.delete_message(
                chat_id=chat_id,
                message_id=message.message_id,
            )
            bot.send_message(
                chat_id=chat_id,
                text="Really Sorry, There was a technical error. Please try again",
            )
    elif choice == "boring-n":
        try:
            bot.send_animation(
                chat_id,
                animation="https://media.giphy.com/media/6txsGT5gGdMK2ChMA5/giphy.gif",
                caption="I know, I don't make boring conversations 😁\n\nI'll finish my explanation in just next two messages.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(2)
        except:
            bot.send_message(
                chat_id,
                text="I know, I don't make boring conversations 😁\n\nI'll finish my explanation in just next two messages.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(2)

        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/HAUxypcipk4AvnHdp0/giphy.gif",
                caption=f"<b>4.</b> I can be used as a medium between you and your customers or students. \nI can clear their most common doubts instead of you",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        except:
            bot.send_message(
                chat_id=chat_id,
                text=f"<b>4.</b> I can be used as a medium between you and your customers or students. \nI can clear their most common doubts instead of you",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/qKltgF7Aw515K/giphy.gif",
                caption=f"<b>5.</b> I can be used as a medium to collect information Feedback or Queries or Issues from customers and store it into your personal database  and you can go-through it later on an interactive desktop application developed by us.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        except:
            bot.send_message(
                chat_id=chat_id,
                text=f"<b>5.</b> I can be used as a medium to collect information Feedback or Queries or Issues from customers and store it into your personal database and you can go-through it later on an interactive desktop application developed by us.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)

        bot.send_message(
            chat_id=chat_id,
            text=f"Finally, These <b>alone are not my limitations</b>, I can be customized as per your needs and I can be added with functionalities as per your requirements. 🤩",
            parse_mode=ParseMode.HTML,
        )
        time.sleep(4)
        bot.send_message(
            chat_id=chat_id,
            text=f"That's all from my side, I think I've explained enough and Kept a Boring-Less conversation",
            parse_mode=ParseMode.HTML,
        )

        time.sleep(4)
        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/brHaCdJqCXijm/giphy.gif",
                caption=f"You can contact @Lahfir for further details. Thanks for your patience and Nice talking with you 😊.\n\nI'm so curious to be a part of your Business or Group 😁.",
                parse_mode=ParseMode.HTML,
            )
        except:
            bot.send_message(
                chat_id=chat_id,
                text=f"You can contact @Lahfir for further details. \n\nThanks for your patience and Nice talking with you 😊.\n\nI'm so curious to be a part of your Business or Group 😁.",
                parse_mode=ParseMode.HTML,
            )
        bot.send_message(
            chat_id,
            "You can use the following commands to chat with me\n\n<b>1.</b> /start - I will start explaining about me and the functionalities\n<b>2.</b> /about - Use this command to know about me <i>in detail</i>\n<b>3.</b> /functionality - Use this command to see my functionalities <i>in detail</i>",
            parse_mode=ParseMode.HTML,
        )
        message = bot.send_message(
            chat_id, "<b>Processing Photo...</b>", parse_mode=ParseMode.HTML
        )

        try:
            while True:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=open("Functionalities.png", "rb"),
                    caption="This photo explains the functionalities of Myself",
                )
                bot.delete_message(
                    chat_id=chat_id,
                    message_id=message.message_id,
                )
                message = bot.send_message(
                    chat_id, "<b>Processing Video...</b>", parse_mode=ParseMode.HTML
                )
                bot.send_video(
                    chat_id=chat_id,
                    video=open("Web-App Exp-1.m4v", "rb"),
                    caption="This video explains the functionalities of the Web-App",
                    supports_streaming=True,
                )
                break
            bot.delete_message(
                chat_id=chat_id,
                message_id=message.message_id,
            )
        except telegram.error.NetworkError as e:
            print(e)
            bot.delete_message(
                chat_id=chat_id,
                message_id=message.message_id,
            )
            bot.send_message(
                chat_id=chat_id,
                text="Really Sorry, There was a technical error. Please try again",
            )


def yes_no(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = update._effective_message.chat.id
    username = update._effective_message.chat.username
    first_name = update._effective_message.chat.first_name
    query.answer()
    choice = query.data
    bot.send_chat_action(chat_id, action="typing")

    if choice == "boring-y":
        bot.send_message(
            chat_id,
            text=f"Ohh! 😭, I'm really sorry {['@'+username if username else first_name][0]}\n\nI'll finish my explanation in just next two messages.\n\nOnce again I'm sorry 😁",
            parse_mode=ParseMode.HTML,
        )
    elif choice == "boring-n":
        bot.send_message(
            chat_id,
            text="I know, I don't make boring conversations 😁\n\nI'll finish my explanation in just next two messages.",
            parse_mode=ParseMode.HTML,
        )


def skip_website(update: Update, context: CallbackContext) -> int:
    """Skips the photo and asks for a location."""
    user = update.message.from_user
    update.message.reply_text(
        "Alright, Please enter your <b>First Name</b>", parse_mode=ParseMode.HTML
    )

    return FN


def skip_ln(update: Update, context: CallbackContext) -> int:
    """Skips the photo and asks for a location."""
    user = update.message.from_user
    update.message.reply_text(
        "Alright, Please enter your <b>Email Address</b>", parse_mode=ParseMode.HTML
    )

    return EMAIL


def start(update: Update, context: CallbackContext):
    global db, collection
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username
    bot.send_chat_action(chat_id, action="typing")

    model["_id"] = chat_id
    model["username"] = username
    model["chat_id"] = chat_id

    try:
        results = collection.insert_one(model)
    except DuplicateKeyError as dke:
        print("Already registered")

    try:
        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/3mfxH0nbfVFLt1gTpq/giphy.gif",
                caption=f"Hello {['@'+username if username else first_name][0]}\nThanks for your message.\n\nI'm So Excited to chat with you",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(1)
        except:
            bot.send_message(
                chat_id=chat_id,
                text=f"Hello {['@'+username if username else first_name][0]}\nThanks for your message.\n\nI'm So Excited to chat with you",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(1)
        bot.send_message(
            chat_id=chat_id,
            text=f"I'm <b>Engine</b>,\n\nI was Designed and Developed by @lahfir",
            parse_mode=ParseMode.HTML,
        )
        time.sleep(2)
        bot.send_message(
            chat_id=chat_id,
            text=f"Ok, So let me explain you What can I do to help you or your <b>business</b> or your <b>mentorship program</b> or your <b>service</b> as an Intelligent Bot",
            parse_mode=ParseMode.HTML,
        )
        time.sleep(6)
        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/yNU0cGq2Cu36sCf1WL/giphy.gif",
                caption=f"<b>1.</b> I can be customized to be your <b>Assistant</b>",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(4)
        except:
            bot.send_animation(
                chat_id=chat_id,
                text=f"<b>1.</b> I can be customized to be your <b>Assistant</b>",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(4)
        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/gT9QzllTygbedDOeRm/giphy.gif",
                caption=f"<b>2.</b> I can be put in a <b>Telegram group or channel</b> and the members can access me for simple doubts insteasd of flooding your inbox feed 😂 [ This will be very helpful if you offer any mentorship services or any VIP group ]",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        except:
            bot.send_message(
                chat_id=chat_id,
                text=f"<b>2.</b> I can be put in a <b>Telegram group or channel</b> and the members can access me for simple doubts insteasd of flooding your inbox feed 😂 [ This will be very helpful if you offer any mentorship services or any VIP group ]",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        try:
            bot.send_animation(
                chat_id=chat_id,
                animation="https://media.giphy.com/media/JrXas5ecb4FkwbFpIE/giphy.gif",
                caption=f"<b>3.</b> I can maintain a <b>database</b> for people in your mentorship program and it can be used to track The amount they payed or for how many months or year they paid for if you offer timely programs etc.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        except:
            bot.send_message(
                chat_id=chat_id,
                text=f"<b>3.</b> I can maintain a <b>database</b> for people in your mentorship program and it can be used to track The amount they payed or for how many months or year they paid for if you offer timely programs etc.",
                parse_mode=ParseMode.HTML,
            )
            time.sleep(6)
        keyboard = [
            [
                InlineKeyboardButton("Yes 😭", callback_data="boring-y"),
                InlineKeyboardButton("No 😁", callback_data="boring-n"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(
            chat_id=chat_id,
            text=f"Am I boring? 😕",
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
        )
    except Exception as e:
        print(e)
        if e.message == "Forbidden: bot was blocked by the user":
            keyboard = [
                [
                    InlineKeyboardButton("Start DEMO-BOT 🚀", url="t.me/SFTSETUPBOT"),
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update._effective_message.reply_text(
                text="Uh! You might have blocked or have not Started the BOT\n\nSTART him by clicking the button below 😊",
                reply_markup=reply_markup,
            )
        else:
            update._effective_message.reply_text(
                text="Uh! There is a technical problem with BOT, We'll rectify it soon.\n\nSorry For your Inconvenience"
            )


def about(update: Update, context: CallbackContext):
    global db, collection
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username
    bot.send_chat_action(chat_id, action="typing")

    message = bot.send_message(
        chat_id, "<b>Processing Photo...</b>", parse_mode=ParseMode.HTML
    )

    model["_id"] = chat_id
    model["username"] = username
    model["chat_id"] = chat_id

    try:
        while True:
            bot.send_photo(
                chat_id=chat_id,
                photo=open("About.png", "rb"),
                caption="This photo explains about me",
            )
            break
        bot.delete_message(
            chat_id=chat_id,
            message_id=message.message_id,
        )
    except telegram.error.NetworkError:
        bot.delete_message(
            chat_id=chat_id,
            message_id=message.message_id,
        )
        bot.send_message(
            chat_id=chat_id,
            text="Really Sorry, There was a technical error. Please try again",
        )


def functionality(update: Update, context: CallbackContext):
    global db, collection
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username
    bot.send_chat_action(chat_id, action="typing")

    message = bot.send_message(
        chat_id, "<b>Processing Photo...</b>", parse_mode=ParseMode.HTML
    )

    model["_id"] = chat_id
    model["username"] = username
    model["chat_id"] = chat_id

    try:
        while True:
            bot.send_photo(
                chat_id=chat_id,
                photo=open("Functionalities.png", "rb"),
                caption="This photo explains the functionalities of Myself",
            )
            bot.delete_message(
                chat_id=chat_id,
                message_id=message.message_id,
            )
            message = bot.send_message(
                chat_id, "<b>Processing Video...</b>", parse_mode=ParseMode.HTML
            )
            bot.send_video(
                chat_id=chat_id,
                width=1920,
                height=1080,
                video=open("Web-App Exp-1.m4v", "rb"),
                caption="This video explains the functionalities of the Web-App",
                supports_streaming=True,
            )
            break
        bot.delete_message(
            chat_id=chat_id,
            message_id=message.message_id,
        )
    except telegram.error.NetworkError as e:
        print(e)
        bot.delete_message(
            chat_id=chat_id,
            message_id=message.message_id,
        )
        bot.send_message(
            chat_id=chat_id,
            text="Really Sorry, There was a technical error. Please try again",
        )


def help(update: Update, context: CallbackContext):
    global db, collection
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username
    bot.send_chat_action(chat_id, action="typing")

    model["_id"] = chat_id
    model["username"] = username
    model["chat_id"] = chat_id

    bot.send_message(
        chat_id,
        "You can use the following commands to chat with me\n\n<b>1.</b> /start - I will start explaining about me and the functionalities\n<b>2.</b> /about - Use this command to know about me <i>in detail</i>\n<b>3.</b> /functionality - Use this command to see my functionalities <i>in detail</i>",
        parse_mode=ParseMode.HTML,
    )


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    update.message.reply_text(
        "Cancelled the Operation", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def companynamehandler(update: Update, context: CallbackContext):
    try:
        user = update.message.from_user
        keyboard = [
            [
                InlineKeyboardButton("✅ Yes", callback_data="compn-y"),
                InlineKeyboardButton("⚙️ Change", callback_data="compn-n"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            f"Confirm your Company Name: <b>{update.message.text}</b>\n\n",
            reply_markup=reply_markup,
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        print(e)


def handle_message(update: Update, context: CallbackContext):
    chat_id = update._effective_message.chat.id
    first_name = update._effective_message.chat.first_name
    last_name = update._effective_message.chat.last_name
    username = update._effective_message.chat.username

    text = str(update.effective_message.text).lower()
    try:
        # update._effective_message.reply_text(
        #     text=chat.Response(text), parse_mode=ParseMode.HTML
        # )
        update._effective_message.reply_text(text="Hello", parse_mode=ParseMode.HTML)
    except Exception as e:
        print(e)
        if e.message == "Forbidden: bot was blocked by the user":
            keyboard = [
                [
                    InlineKeyboardButton(
                        "Start ENGINE 🚀", url="https://t.me/TMSVIP_BOT"
                    ),
                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update._effective_message.reply_text(
                text="Uh! You might have blocked or have not Started ENGINE\n\nSTART him by clicking the button below 😊",
                reply_markup=reply_markup,
            )
        else:
            update._effective_message.reply_text(
                text="Uh! There is a technical problem with ENGINE, We'll rectify it soon.\n\nSorry For your Inconvenience"
            )


# conv_handler = ConversationHandler(
#     entry_points=[
#         CallbackQueryHandler(button),
#     ],
#     states={
#         COMPANYN: [
#             MessageHandler(Filters.text, companynamehandler),
#             CallbackQueryHandler(yes_no),
#         ],
#     },
#     fallbacks=[CommandHandler("cancel", cancel)],
# )

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("about", about))
dispatcher.add_handler(CommandHandler("functionality", functionality))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CallbackQueryHandler(button))
# dispatcher.add_handler(MessageHandler(Filters.text, handle_message))


while True:
    try:
        updater.start_polling()
        updater.idle()
    except ConnectionError as c:
        time.sleep(5)
