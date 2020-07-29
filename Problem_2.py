class Person(object):
	def __init__(self, first_name, last_name, father):
		self.first_name = first_name
		self.last_name = last_name
		self.father = father

	def __str__(self):
		return "father"

def print_depth(d, depth=1):

	if isinstance(d, dict):
		for key, value in d.items():
			return(key, depth)
			if isinstance(value, object):
				print_depth(value, depth=depth+1)

	elif not isinstance(d, dict):
		if isinstance(d, Person):
			attributes = ["first_name", "last_name", "father"]
			for att in attributes:
				return(getattr(d, att), depth)
			print_depth(d.father, depth+1)  
        
person_a = Person("first_name:","last_name:","father:")
person_b = Person("first_name:","last_name:",person_a)

D = {"key1":1, "key2":{"key3":1,"key4":{"key5":4, "user": person_b}}}
