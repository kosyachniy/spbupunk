from func.vk_group import *

with open('keyboards.json', 'r') as file:
	keyboards = json.loads(file.read())

with open('answers.json', 'r') as file:
	answers = json.loads(file.read())

while True:
	try:
		with open('whitelistvk.json', 'r') as file:
			whitelist = json.loads(file.read())
	except:
		whitelist = []

	try:
		all_messages = read()
	except:
		time.sleep(1)
		continue

	for i in all_messages:
		# if i[0] not in users():
		# 	send(i[0], 'Сначала подпишитесь на группу бота!\nhttps://vk.com/spbupunk', keyboard=keyboard)
		# 	continue

		# if i[0] not in users():
		# 	send(i[0], 'Никто не любит спам и мы тоже. Подпишись на группу бота, чтобы не пропустить ничего важного в наших постах! Мероприятия в ПУНКе и наиболее важные объявления.\nhttps://vk.com/spbupunk')

		if i[0] in whitelist:
			continue

		mes = i[1].lower().strip()
		try:
			f = True
			for req in answers:
				if mes in req['questions']:
					f = False
					print('!1', i)
					send(i[0], req['answer'], req['attachments'], keyboards[req['keyboard']-1] if req['keyboard'] else None)

			if f:
				if mes == 'выключить рассылку':
					whitelist.append(i[0])

					with open('whitelistvk.json', 'w') as file:
						print(json.dumps(whitelist), file=file)
				else:
					send(i[0], 'Выберите действие:', keyboard=keyboards[0])

		except:
			try:
				send(i[0], 'Какое-то сложное сообщение. Бот не может ответить.', keyboard=keyboard)
			except:
				pass

	# time.sleep(0.5)