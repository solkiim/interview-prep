class Pet(object):
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def getName(self):
		return self.name

	def getSpecies(self):
		return self.species

	def __str__(self):
		return "%s is a %s" % (self.name, self.species)


class Cat(Pet):
	def __init__(self, name, hates_dogs):
		Pet.__init__(self, name, "Cat")
		self.hates_dogs = hates_dogs
	
	def hatesDogs(self):
		return self.hates_dogs

	
polly = Pet("Polly", "parrot")
print polly

jumper = Cat("Jumper", True)
print jumper
print str(jumper.hatesDogs())
