import sqlite3
import datetime as dt
class DB:
	def __init__(self):
		self.conn = sqlite3.connect("phones.sqlite")
	def addNumber(self, num):
		nums = self.selectNumbers()
		if(num not in nums):
			c=self.c()
			c.execute("INSERT INTO numbers (number,time) VALUES (?,?)",(num,dt.datetime.now()))
			self.conn.commit()
		else:
			print("Number already added")
	def readNumbers(self):
		nums = self.selectNumbers()
		return nums
	def exit(self):
		self.conn.close()
	def selectNumbers(self):
		c = self.c()
		results = c.execute('SELECT number FROM numbers')
		res = [x[0] for x in results]
		return res
	def c(self):
		return self.conn.cursor()
