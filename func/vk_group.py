import time, requests, vk_api, json

GROUP_ID = 170498641
# ALBUM_ID = 247265476

with open('keys.json', 'r') as file:
	s = json.loads(file.read())

	vk = vk_api.VkApi(token=s['vk'])

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
	return messages

def dial():
	messages = []

	offset = 0
	while True:
		conversations = vk.method('messages.getConversations', {
			'count': 200,
			'offset': offset,
		})['items']

		for i in conversations:
			messages.append(i['conversation']['peer']['id'])

		if len(conversations) < 200:
			break
		offset += 200

	return messages

def stats():
	# messages = []
	timeline = {}

	offset = 0
	while True:
		conversations = vk.method('messages.getConversations', {
			'count': 200,
			'offset': offset,
		})['items']

		for i in conversations:
			id = i['conversation']['peer']['id']

			conversation = vk.method('messages.getHistory', {
				'peer_id': id,
			})

			# k = 0
			for j in conversation['items']:
				if j['out'] == 0:
					day = j['date'] // 86400
					# k += 1

					if day not in timeline:
						timeline[day] = {
							id: 1,
						}
					else:
						if id in timeline[day]:
							timeline[day][id] += 1
						else:
							timeline[day][id] = 1

			# messages.append(conversation)

		if len(conversations) < 200:
			break
		offset += 200

	stat = []
	line = sorted(list(timeline.keys()))
	for i in line:
		sum_mes = 0
		for j in timeline[i]:
			sum_mes += timeline[i][j]

		stat.append((i, len(timeline[i]), sum_mes))

	return stat

def users():
	return vk.method('groups.getMembers', {'group_id': 170498641})['items']