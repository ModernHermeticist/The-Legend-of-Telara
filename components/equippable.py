class Equippable:
	def __init__(self, slot, min_power_bonus=0, max_power_bonus=0, defense_bonus=0, max_hp_bonus=0, max_mp_bonus=0):
		self.slot = slot
		self.max_power_bonus = max_power_bonus
		self.min_power_bonus = min_power_bonus
		self.defense_bonus = defense_bonus
		self.max_hp_bonus = max_hp_bonus
		self.max_mp_bonus = max_mp_bonus