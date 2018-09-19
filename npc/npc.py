

class NPC():
	def __init__(self, name, inventory, hp, mp, power, defense, **kwargs):
		self.name = name
		self.inventory = inventory
		self.hp = hp
		self.mp = mp
		self.power = power
		self.defense = defense
		self.function_kwargs = kwargs