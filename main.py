from func.vk_group import *

keyboard = [
	['Добраться до города'],
	['Где магазины', 'Где столовые'],
	['Учебные корпуса', 'Карта общежитий'],
	['Частые вопросы', 'Расписание'],
	['Сети', 'Контакты'], #'Структуры', 
	['Про бота'],
]

while True:
	for i in read():
		if i[0] not in users():
			send(i[0], 'Сначала подпишитесь на группу бота!\nhttps://vk.com/spbupunk', keyboard=keyboard)
			continue

		mes = i[1].lower().strip()
		try:
			if mes in ('добраться до города', 'город', 'уехать отсюда', 'уехать', 'электричка', 'автобус', 'автобусы', 'поезд', 'транспорт', 'в город', 'электрички', 'дорога', 'хочу в город'):
				send(i[0], 'До Автово (станция метро)\nАвтобусы: 210\nМаршрутки: 404, 424\nДля постоянных поездок в город и по городу покупают БСК.\n\nРасписание электричек (от Университета до Балтийского вокзала)\nВ город: https://t.rasp.yandex.ru/search/suburban/?fromId=s9603770&toId=s9602498\nИз города: https://t.rasp.yandex.ru/search/suburban/?fromId=s9602498&toId=s9603770\nОбычный билет — 72₽, по студенческому — 36₽.', ['photo-170498641_456239017'], keyboard)

			elif mes in ('где магазины', 'магазины', 'магазин', 'супермаркет', 'гипермаркет', 'маркет', 'где магазин', 'купить', 'лента', 'перекрёсток', 'перекресток', 'пятёрочка', 'пятерочка', 'андреевский', 'хочу в магазин'):
				send(i[0], 'Простой путь — Андреевский (находится в 12 общежитии)\n\nЕсли нужен ассортимент побольше — Лента (оптимальный вариант)\nПерелазить через забор очень плохо!\n\nЕсли хочется погулять — Пятёрочка и Перекрёсток (они рядом)', ['photo-170498641_456239019', 'photo-170498641_456239020'], keyboard)

			elif mes in ('где столовые', 'столовые', 'столовая', 'где столовая', 'kfc', 'mc', 'bk', 'бк', 'мак', 'кфс', 'еда', 'хочу есть', 'хочу кушать', 'кушать', 'есть', 'кушац', 'поесть', 'забегаловка', 'фастфуд', 'кафе', 'бар'):
				send(i[0], 'Столовые есть в учебных корпусах и 12 общежитии. Есть одна большая столовая — Мавзолей.\nНо очереди везде большие)\n\nBurgerKing, McDonald\'s и KFC в петергофе нет :(\nПоэтому обычно заказывают в Pizza Rich (http://pizzarich.ru/), Додо пицца (https://dodopizza.ru/petergof/chicherinskaya2), Dostaевский (https://dostaevsky.ru/), TakeEat (https://vk.com/takeeat).', ['photo-170498641_456239030'], keyboard)

			elif mes in ('учебные корпуса', 'учиться', 'учёба', 'корпуса', 'корпус', 'где корпус', 'где корпуса', 'где учебные корпуса', 'хочу учиться'):
				send(i[0], '', ['photo-170498641_456239018'], keyboard)

			elif mes in ('карта общежитий', 'общежития', 'общежитие', 'карта', 'схема', 'схема общежитий', 'общага', 'общаги', 'хочу домой', 'хочу в общагу', 'хочу в общежитие', 'где общежитие'):
				send(i[0], 'Банкоматы в 10, 14, 16 общежитиях. Сбербанк — 10, 16.\n\nПрачечная между 21 и 22 общежитиями. Стирка 100 рублей, сушка 100 рублей. Работает ежедневно с 10 до 2 ночи.\n\nПарикмахерская находится между 22 и 23 общежитиями. Работает ежедневно с 11 до 20.\n\nИ не спрашивайте, где 11 общежитие.\n\nПодробнее: http://campus.spbu.ru/uslugi.html', ['photo-170498641_456239031'], keyboard)

			elif mes in ('частые вопросы', 'вопросы', 'вопрос', 'хочу спросить', 'есть вопрос'):
				send(i[0], '— Когда можно будет переселиться?\n— Только в октябре.\n\n— Что такое мёртвые души?\n— Соседи, которые не живут в блоке.\n\n— Сколько стоит проживание?\n— Около 250 рублей в месяц (для бюджетников).\n\n— Куда лучше переселяться?\n— 10, 12, 13 общежития самые новые. 14 и 15 культовое место, если пошалить, то сюда. 16, 20-23 семейные, есть кухня в блоке, но далеко не везде хороший ремонт.\n\n— Что по интернету?\n— Есть 3 тарифа. Самый дешёвый 200 рублей - его хватит на весь блок, покупайте роутер.\n\nЕсть другие вопросы? Пишите мне: https://vk.com/freakiller', keyboard=keyboard)

			elif mes in ('структуры',):
				send(i[0], 'Для ПМ-ПУ:', [''], keyboard)

			elif mes in ('сети', 'instagram', 'ig', 'вк', 'vk', 'сайты', 'паблики', 'признавашки', 'мемы', 'объявления', 'хочу узнать', 'инстаграмм', 'инстаграм', 'вконтакте', 'контакт'):
				send(i[0], '[overhearspbsu|Подслушано]\n\n[spbu_advert|Объявления СПбГУ]\n\n[apmems|Мемы]\n\n[spbu_love|Признавашки]\n\nInstagram ПУНК: @punk_today\n\nНу и.. подписывайтесь на меня) @mr.poloz', ['photo-170498641_456239024'], keyboard)

			elif mes in ('контакты',):
				send(i[0], 'Сайт СПбГУ: https://spbu.ru/\n\nДля ПМ-ПУ:\nОфициальный сайт: http://www.apmath.spbu.ru/ru/\nНеофициальный сайт, конспекты: http://pm-pu.ru', keyboard=keyboard)

			elif mes in ('расписание', 'расписание пар', 'когда пары', 'пара', 'пары', 'расписания', 'расписания пар'):
				send(i[0], 'https://timetable.spbu.ru/', keyboard=keyboard)

			elif mes in ('про бота', 'about', 'бот', 'предложение', 'кто ты', 'автор', 'кто тебя создал', 'создатель'):
				send(i[0], 'Автор: Алексей Полоз\nПо всем вопросам и предложениям — [freakiller|обращайтесь ко мне].\n\nИ конечно подписывайтесь на Instagram\nhttps://www.instagram.com/mr.poloz', keyboard=keyboard)

			else:
				send(i[0], 'Выберите действие:', keyboard=keyboard)

		except:
			try:
				send(i[0], 'Какое-то сложное сообщение. Бот не может ответить.', keyboard=keyboard)
			except:
				pass

	# time.sleep(0.5)