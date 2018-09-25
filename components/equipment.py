from equipment_slots import EquipmentSlots

class Equipment:
	def __init__(self, main_hand=None, off_hand=None, chest=None, legs=None, feet=None, \
					arms=None, hands=None, shoulders=None, head=None, wrists=None):
		self.main_hand = main_hand
		self.off_hand = off_hand
		self.chest = chest
		self.legs = legs
		self.feet = feet
		self.arms = arms
		self.hands = hands
		self.shoulders = shoulders
		self.head = head
		self.wrists = wrists

	@property
	def max_hp_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.max_hp_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.max_hp_bonus

		return bonus

	@property
	def max_mp_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.max_mp_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.max_mp_bonus

		return bonus

	@property
	def min_damage_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.min_damage_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.min_damage_bonus

		return bonus

	@property
	def max_damage_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.max_damage_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.main_hand.equippable.max_damage_bonus

		return bonus

	@property
	def strength_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.strength_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.strength_bonus

		return bonus

	@property
	def dexterity_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.dexterity_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.dexterity_bonus

		return bonus

	@property
	def defense_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.defense_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.defense_bonus

		return bonus

	def toggle_equip(self, equippable_entity):
		results = []

		slot = equippable_entity.equippable.slot

		if slot == EquipmentSlots.MAIN_HAND:
			if self.main_hand == equippable_entity:
				self.main_hand = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.main_hand:
					results.append({'unequipped': self.main_hand})

				self.main_hand = equippable_entity
				results.append({'equipped': equippable_entity})

		elif slot == EquipmentSlots.OFF_HAND:
			if self.off_hand == equippable_entity:
				self.off_hand = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.off_hand:
					results.append({'unequipped': self.off_hand})

				self.off_hand = equippable_entity
				results.append({'equipped': equippable_entity})

		return results