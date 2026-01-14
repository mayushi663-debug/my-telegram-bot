import telebot
from telebot import types

# --- CONFIGURATION ---
API_TOKEN = '8285077978:AAHUEOurZeP71RLlev4dFSizFbqx6WprFRc'

# APNI SAHI IDs YAHAN DALEIN (Rose bot se check karke)
CHANNEL_1_ID = -1003428201522
CHANNEL_2_ID = -1002003373537
CHANNEL_3_ID = -1003114607622  # <--- ISSE ZAROOR CHANGE KAREIN

# Links
CHANNEL_1_URL = "https://t.me/WinGo_CustomerService"
CHANNEL_2_URL = "https://t.me/uonorummy123"
CHANNEL_3_URL = "https://t.me/earnmoneytips132"
APP_LINK = "https://www.zmintly.com/?invite_code=20672"
CUSTOMER_SERVICE = "Minitly"

bot = telebot.TeleBot(API_TOKEN)
bot.remove_webhook()

def is_user_member(user_id):
    channels = [CHANNEL_1_ID, CHANNEL_2_ID, CHANNEL_3_ID]
    allowed = ['member', 'creator', 'administrator']
    
    try:
        for ch_id in channels:
            status = bot.get_chat_member(ch_id, user_id).status
            if status not in allowed:
                return False
        return True
    except Exception as e:
        # Yeh line aapko batayegi ki error kahan hai
        print(f"Error with ID {ch_id}: {e}")
        return False

@bot.message_handler(commands=['start'])
def start(message):
    if is_user_member(message.from_user.id):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🚀 Open App", url=APP_LINK))
        markup.add(types.InlineKeyboardButton("💬 Support", url=f"https://t.me/{CUSTOMER_SERVICE}"))
        bot.send_message(message.chat.id, "✅ Access Granted!", reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Join 1", url=CHANNEL_1_URL), types.InlineKeyboardButton("Join 2", url=CHANNEL_2_URL))
        markup.add(types.InlineKeyboardButton("Join 3", url=CHANNEL_3_URL))
        markup.add(types.InlineKeyboardButton("🔄 Verify", callback_data="verify"))
        bot.send_message(message.chat.id, "❌ Join all channels first!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "verify")
def verify(call):
    if is_user_member(call.from_user.id):
        bot.edit_message_text("✅ Success! Type /start", call.message.chat.id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, "❌ Not joined yet!", show_alert=True)

print("Bot is running... IDs check karein.")
bot.infinity_polling()