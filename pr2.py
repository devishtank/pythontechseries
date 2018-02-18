from Tkinter import *

class Application(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.numOfTry = 3
		self.create_widget()

	def accept(self):
		print "You are allowed to enter the system ", self.su.get()

	def deny(self):
		print "You are not allowed to enter the system ", self.su.get()

	def create_widget(self):
		self.lu = Label(window, text="Username:")
		self.lu.grid(row=0, column=0)
		self.su = StringVar()
		self.w1 = Entry(window, textvariable=self.su)
		self.w1.grid(row=0, column=1)

		self.lp = Label(window, text="Password:")
		self.lp.grid(row=1, column=0)
		self.sp = StringVar()
		self.w2 = Entry(window, textvariable=self.sp, show="*")
		self.w2.grid(row=1, column=1)

		self.btn_login = Button(window, text="login (3 try(s) left)", command=self.update_count_num)
		self.btn_login.grid(row=2, column=0)

	def update_count_num(self):
		self.numOfTry -= 1
		self.btn_login['text'] = "login (" + str(self.numOfTry) + " try(s) left)"

		if(self.su.get().rstrip() == "procodecg" and self.sp.get().rstrip() == "12345678"):
			self.accept()
		else:
			self.deny()

		if(self.numOfTry <= 0):
			self.btn_login['state'] = 'disabled'

window = Tk(className = "My Simple Password")
window.title("Enter username and password")
app = Application(window)

window.mainloop()