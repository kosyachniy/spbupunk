from func.vk_group import *

with open('keyboards.json', 'r') as file:
	keyboards = json.loads(file.read())

for i in dial():
	send(i, 'Бот обновлён!', keyboard=keyboards[0])