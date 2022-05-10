import json
from generator import getRandomCode



def url_in_db(link):
	with open("database/urls.json", "r") as read_file:
		data = json.load(read_file)
		for url in data.keys():
			if link == url:
				return data[url]

		else:
			return False

def key_in_db(key):
	with open("database/urls.json", "r") as read_file:
		data = json.load(read_file)
		for i in data.items():
			if i[1] == key:
				return i[0] # возвращаем оригинальную ссылку
		else:
			return False

def genNewURL(link):
	with open("database/urls.json", "r") as read_file:
		data = json.load(read_file)
	with open("database/urls.json", "w") as read_file:
		key = getRandomCode(6)
		data[link] = key
		json.dump(data, read_file)
