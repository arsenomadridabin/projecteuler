class Hotel:
	def __init__(self,name,star):
		self.name=name
		self.star=star
	def __str__(self):
		return self.name

hotel= Hotel("shankar","five")
name=getattr(hotel,'name')
print(name)
