# Password re-set program
# Password = 'a123456'
# user can enter 3 times (Max)
# After each enter failure, print 'how many times can try'
# After successful enter the PW, print 'Log-in success'

n = 3

while True:
	password = input('Please enter your password: ')
	if password == 'a123456':
		print('log-in successed')
		break
	else:
		n = n - 1
		print('failed, _ times remaining: ', n)
		if n == 0:
			print('The account has been locked')
			break

