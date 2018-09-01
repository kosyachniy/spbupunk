from func.vk_group import *

with open('keyboards.json', 'r') as file:
	keyboards = json.loads(file.read())

with open('whitelist.json', 'r') as file:
	whitelist = json.loads(file.read())

def dispatch(text):
	for i in dial():
		if i not in whitelist:
			send(i, text, keyboard=keyboards[6])