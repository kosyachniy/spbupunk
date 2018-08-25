from func.vk_group import *

keyboard = [
	['Добраться до города'],
	['Где магазины', 'Где столовые'],
	['Учебные корпуса', 'Карта общежитий'],
	['Частые вопросы', 'Расписание'],
	['Сети', 'Контакты'], #'Структуры', 
	['Про бота'],
]

with open('answers.json', 'r') as file:
	answers = json.loads(file.read())

while True:
	try:
		all_messages = read()
	except:
		time.sleep(1)
		continue

	for i in all_messages:
		# if i[0] not in users():
		# 	send(i[0], 'Сначала подпишитесь на группу бота!\nhttps://vk.com/spbupunk', keyboard=keyboard)
		# 	continue

		if i[0] not in users():
			send(i[0], 'Никто не любит спам и мы тоже. Подпишись на группу бота, чтобы не пропустить ничего важного в наших постах! Мероприятия в ПУНКе и наиболее важные объявления.\nhttps://vk.com/spbupunk', keyboard=keyboard)

		mes = i[1].lower().strip()
		try:
			f = True
			for req in answers:
				if mes in req['questions']:
					f = False
					send(i[0], req['answer'], req['attachments'], keyboard)

			if f:
				send(i[0], 'Выберите действие:', keyboard=keyboard)

		except:
			try:
				send(i[0], 'Какое-то сложное сообщение. Бот не может ответить.', keyboard=keyboard)
			except:
				pass

	# time.sleep(0.5)