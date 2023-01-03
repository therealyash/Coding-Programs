# Extract username from a mail then change the mail

mail = 'yashlimkar15@gmail.com'



def change_mail(mail):
	
	mail_len = len(mail)
	index = mail.index('@')
	username = mail[0:index]
	rem_mail = mail[index:]
	new_mail = ''
	new_username = input('Enter a new username: ')
	new_mail = new_username + rem_mail
	
	print('Old Mail:',mail)
	print('Old Username:',username)
	print('New Mail: ',new_mail)

change_mail(mail)
