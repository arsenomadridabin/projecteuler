class Hotel:
	def __init__(self,name,location):
		self.name = name
		self.location = location 

	@classmethod
	def get_location(cls):
		print("class=",cls)
		return "kathmadnu"

	@staticmethod
	def get_star(name):
		if name=="royal":
			return 5
		else:
			return 3

hotel =Hotel("Annapurna","Jamal")
print(Hotel.get_location())
print(hotel.get_star("royal"))

