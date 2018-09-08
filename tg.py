from func.tg_bot import *
import re

with open('keyboards.json', 'r') as file:
	keyboards = json.loads(file.read())

with open('answers.json', 'r') as file:
	answers = json.loads(file.read())

@bot.message_handler(content_types=["text"])
def answ(message):
	user = message.chat.id
	mes = message.text.lower().strip()

	# try:
	f = True
	for req in answers:
		if mes in req['questions']:
			f = False
			if req['answer']:
				for i in re.findall(r'\[\w+\|[\w ]+\]', req['answer']):
					name = i.split('|')[1][:-1]
					src = i.split('|')[0][1:]
					req['answer'] = req['answer'].replace(i, name + ' (vk.com/' + src + ')')
				bot.send_message(user, req['answer'], reply_markup=keyboard(keyboards[req['keyboard']-1]) if req['keyboard'] else None)

			for i in req['attachments']:
				with open('attachments/' + i + '.png', 'rb') as file:
					bot.send_photo(user, file)

	if f:
		if mes == 'выключить рассылку':
			try:
				with open('whitelisttg.json', 'r') as file:
					users = json.loads(file.read())
			except:
				users = [user]
			else:
				users.append(user)

			with open('whitelisttg.json', 'w') as file:
				print(json.dumps(users), file=file)
		else:
			bot.send_message(user, 'Выберите действие:', reply_markup=keyboard(keyboards[0]))

	# except:
	# 	pass

if __name__ == '__main__':
	while True:
		try:
			bot.polling(none_stop=True)
		except:
			time.sleep(5)