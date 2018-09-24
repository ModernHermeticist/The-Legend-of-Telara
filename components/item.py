class Item:
	def __init__(self, description=None, use_function=None, targeting=False, targeting_message=None,
				 targeting_range=None, area_of_effect=None, damage=None, heal_amount=None):
		self.description = description
		self.use_function = use_function
		self.targeting = targeting
		self.targeting_message = targeting_message
		self.targeting_range = targeting_range
		self.area_of_effect = area_of_effect
		self.damage = damage
		self.heal_amount = heal_amount