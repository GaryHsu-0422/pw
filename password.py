password = 'a123456'
i = 3
while True: 
	pw = input('enter your password: ')
	if pw == password:
		print('logged in')
		break
	else:
		i = i - 1
		print('wrong password, you still have', i ,'chances')
		if i == 0:
			break
