import smtplib
import config

def send_email(subject, msg):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.SENDER_EMAIL_ADDRESS, config.PASSWORD)
		message = 'Subject: {}\n\n{}'.format(subject, msg)
		server.sendmail(config.SENDER_EMAIL_ADDRESS, config.RECIEVER_EMAIL_ADDRESS, message)
		server.quit()
	except:
		print("Email failed to send.")
