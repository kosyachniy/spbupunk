import time, requests, vk_api, json

GROUP_ID = 170498641
# ALBUM_ID = 247265476

with open('keys.json', 'r') as file:
	s = json.loads(file.read())

	vk = vk_api.VkApi(token=s['token'])

	# vks=vk_api.VkApi(login=s['login'], password=s['password'])
	# vks.auth()

def send(user, cont, img=[], keyboard=None):
	for i in range(len(img)):
		if img[i][0:5] != 'photo':
			#Загружаем изображение на сервер
			with open('re.jpg', 'wb') as file:
				file.write(requests.get(img[i]).content)

			#Загружаем изображение в ВК
			# photo = vk_api.VkUpload(vks).photo('re.jpg', group_id=GROUP_ID, album_id=ALBUM_ID)[0]
			# img[i] = 'photo{}_{}'.format(photo['owner_id'], photo['id'])

	req = {
		'user_id': user,
		'message': cont,
		'attachment': ','.join(img),
	}

	if keyboard:
		buttons = []
		for j in keyboard:
			line = []
			for i in j:
				line.append({
					'action': {
						'type': 'text',
						'payload': '{\"button\": \"1\"}',
						'label': i,
					},
					'color': 'default',
				})
			buttons.append(line)

		req['keyboard'] = json.dumps({
			'one_time': False,
			'buttons': buttons,
		}, ensure_ascii=False)

	return vk.method('messages.send', req)

def read():
	messages = []
	for i in vk.method('messages.getConversations')['items']:
		if 'unanswered' in i['conversation']:
			messages.append((i['conversation']['peer']['id'], i['last_message']['text']))
			# for j in vk.method('messages.getHistory', {'user_id': i['conversation']['peer']['id']})['items']:
			# 	if 'read_state' in j and not j['read_state'] and not j['out']:
			# 		messages.append((j['from_id'], j['body']))
	return messages

def users():
	return vk.method('groups.getMembers', {'group_id': 170498641})['items']