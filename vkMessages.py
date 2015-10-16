#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import vk_api
from colorama import init, Fore, Back, Style
import time

init(autoreset=True)

f = open('vk.res', 'w')
def main():
	login, password = '', ''
	vk = vk_api.VkApi(login, password)

	vk.authorization()

	options = {
		'out': 0,
	}
	count = 0
	ids = []
	response = vk.method('messages.get', options)  # Используем метод wall.get

	for index, value in enumerate(response["items"]):
		if value['read_state'] == 0:
			print(value)
			ids.append( str(value['user_id'] ))
			
			count += 1


	print(ids)
	id_str = ", ".join(ids)
	print(id_str)
	
	options = {
		'user_ids': id_str
	}
	response = vk.method('users.get', options)  # Используем метод wall.get

	file_str = str(count)
	
	if count != 0:
		file_str += " ["
		for index, value in enumerate(response):
			file_str += value['first_name'] + " "
			file_str += value['last_name']
			
			
			
			if index == response.count(1):
				 file_str += ", "
		file_str += "]"
	f.write(file_str)
	
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
