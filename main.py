import requests,user_agent,json,flask,telebot,random,os,sys,time
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	
    
    
    mas = types.InlineKeyboardMarkup(row_width=2)
    
    A = types.InlineKeyboardButton(text ="USER (BFFFL)", callback_data="F1")
    
    E = types.InlineKeyboardButton(text ="USER (BFFF2)", callback_data="F2")
    
    M = types.InlineKeyboardButton('المطور', url='https://t.me/uaechecker')
    
    mas.add(A,E,M)
    
    bot.send_message(message.chat.id, f"- أهلاً بكً  !\n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="SidraTools":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="USER (BFFFL)", callback_data="F1")

		E = types.InlineKeyboardButton(text ="USER (BFFF2)", callback_data="F2")
		
		M = types.InlineKeyboardButton('المطور', url='https://t.me/uaechecker')
		
		M = types.InlineKeyboardButton('المطور', url='https://t.me/uaechecker')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)

	elif call.data =="F1":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			username = str(us)+str(un)+str(un)+str(un)+str(ua)
			url = "https://accounts.snapchat.com/accounts/get_username_suggestions"
			headers = {
			'accept': '*/*',
		        'accept-encoding': 'gzip, deflate, br',
        		'accept-language': 'en-US,en;q=0.9',
        		'content-length': '57',
        		'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        		'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
        		'origin': 'https://accounts.snapchat.com',
        		'referer': 'https://accounts.snapchat.com/',
        		'sec-fetch-dest': 'empty',
        		'sec-fetch-mode': 'same-origin',
        		'sec-fetch-site': 'same-origin',
        		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        		}
        		data_checker = {
            		'requested_username': user,
            		'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}
        		response = requests.get(url, data=data_checker, headers=headers_check)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ ᴜѕᴇʀɴᴀᴍᴇ ᴛᴇʟᴇɢʀᴀᴍ  ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : @{username}\n────── • ✧✧ • ──────\n• @UAE60")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/uaechecker')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
			
		
		
	elif call.data =="F2":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xm = "0987654321"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			bs = str(''.join(random.choice(xm)for i in range(1))) 
			username = str(us)+str(un)+str(un)+str(un)+str(bs)
			url = "https://accounts.snapchat.com/accounts/get_username_suggestions"
			headers = {
			'accept': '*/*',
		        'accept-encoding': 'gzip, deflate, br',
        		'accept-language': 'en-US,en;q=0.9',
        		'content-length': '57',
        		'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        		'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
        		'origin': 'https://accounts.snapchat.com',
        		'referer': 'https://accounts.snapchat.com/',
        		'sec-fetch-dest': 'empty',
  		        'sec-fetch-mode': 'same-origin',
        		'sec-fetch-site': 'same-origin',
        		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
        		}
        		data_checker = {
            		'requested_username': user,
            		'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}
  		     	response = requests.get(url, data=data_checker, headers=headers_check)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ ᴜѕᴇʀɴᴀᴍᴇ ᴛᴇʟᴇɢʀᴀᴍ  ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : @{username}\n────── • ✧✧ • ──────\n• @UAE60")
				#+str(username)
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}', callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/uaechecker')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://coinsinstabot.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
