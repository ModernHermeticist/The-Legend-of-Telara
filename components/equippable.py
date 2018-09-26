class Equippable:
	def __init__(self, slot, ranged=False, min_damage_bonus=0, max_damage_bonus=0, strength_bonus=0, dexterity_bonus=0, 
				stamina_bonus=0, intelligence_bonus=0, armor_bonus=0, max_hp_bonus=0, max_mp_bonus=0):
		self.slot =                 slot
		self.ranged =               ranged
		self.min_damage_bonus =     min_damage_bonus
		self.max_damage_bonus =     max_damage_bonus
		self.strength_bonus =       strength_bonus
		self.dexterity_bonus =      dexterity_bonus
		self.stamina_bonus =        stamina_bonus
		self.intelligence_bonus =   intelligence_bonus
		self.armor_bonus =          armor_bonus
		self.max_hp_bonus =         max_hp_bonus
		self.max_mp_bonus =         max_mp_bonus