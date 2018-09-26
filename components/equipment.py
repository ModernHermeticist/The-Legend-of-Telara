from equipment_slots import EquipmentSlots

class Equipment:
	def __init__(self, main_hand=None, off_hand=None, chest=None, legs=None, feet=None, \
					arms=None, hands=None, shoulders=None, head=None, wrists=None, back=None):
		self.main_hand =    main_hand
		self.off_hand =     off_hand
		self.chest =        chest
		self.legs =         legs
		self.feet =         feet
		self.arms =         arms
		self.hands =        hands
		self.shoulders =    shoulders
		self.head =         head
		self.wrists =       wrists
		self.back =         back

	@property
	def max_hp_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.max_hp_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.max_hp_bonus

		if self.chest and self.chest.equippable:
			bonus += self.chest.equippable.max_hp_bonus

		if self.legs and self.legs.equippable:
			bonus += self.legs.equippable.max_hp_bonus

		if self.feet and self.feet.equippable:
			bonus += self.feet.equippable.max_hp_bonus

		if self.arms and self.arms.equippable:
			bonus += self.arms.equippable.max_hp_bonus

		if self.hands and self.hands.equippable:
			bonus += self.hands.equippable.max_hp_bonus

		if self.shoulders and self.shoulders.equippable:
			bonus += self.shoulders.equippable.max_hp_bonus

		if self.head and self.head.equippable:
			bonus += self.head.equippable.max_hp_bonus

		if self.wrists and self.wrists.equippable:
			bonus += self.wrists.equippable.max_hp_bonus

		if self.back and self.back.equippable:
			bonus += self.back.equippable.max_hp_bonus

		return bonus

	@property
	def max_mp_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.max_mp_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.max_mp_bonus

		if self.chest and self.chest.equippable:
			bonus += self.chest.equippable.max_mp_bonus

		if self.legs and self.legs.equippable:
			bonus += self.legs.equippable.max_mp_bonus

		if self.feet and self.feet.equippable:
			bonus += self.feet.equippable.max_mp_bonus

		if self.arms and self.arms.equippable:
			bonus += self.arms.equippable.max_mp_bonus

		if self.hands and self.hands.equippable:
			bonus += self.hands.equippable.max_mp_bonus

		if self.shoulders and self.shoulders.equippable:
			bonus += self.shoulders.equippable.max_mp_bonus

		if self.head and self.head.equippable:
			bonus += self.head.equippable.max_mp_bonus

		if self.wrists and self.wrists.equippable:
			bonus += self.wrists.equippable.max_mp_bonus

		if self.back and self.back.equippable:
			bonus += self.back.equippable.max_mp_bonus

		return bonus

	@property
	def min_damage_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.min_damage_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.min_damage_bonus

		if self.chest and self.chest.equippable:
			bonus += self.chest.equippable.min_damage_bonus

		if self.legs and self.legs.equippable:
			bonus += self.legs.equippable.min_damage_bonus

		if self.feet and self.feet.equippable:
			bonus += self.feet.equippable.min_damage_bonus

		if self.arms and self.arms.equippable:
			bonus += self.arms.equippable.min_damage_bonus

		if self.hands and self.hands.equippable:
			bonus += self.hands.equippable.min_damage_bonus

		if self.shoulders and self.shoulders.equippable:
			bonus += self.shoulders.equippable.min_damage_bonus

		if self.head and self.head.equippable:
			bonus += self.head.equippable.min_damage_bonus

		if self.wrists and self.wrists.equippable:
			bonus += self.wrists.equippable.min_damage_bonus

		if self.back and self.back.equippable:
			bonus += self.back.equippable.min_damage_bonus

		return bonus

	@property
	def max_damage_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.max_damage_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.max_damage_bonus

		if self.chest and self.chest.equippable:
			bonus += self.chest.equippable.max_damage_bonus

		if self.legs and self.legs.equippable:
			bonus += self.legs.equippable.max_damage_bonus

		if self.feet and self.feet.equippable:
			bonus += self.feet.equippable.max_damage_bonus

		if self.arms and self.arms.equippable:
			bonus += self.arms.equippable.max_damage_bonus

		if self.hands and self.hands.equippable:
			bonus += self.hands.equippable.max_damage_bonus

		if self.shoulders and self.shoulders.equippable:
			bonus += self.shoulders.equippable.max_damage_bonus

		if self.head and self.head.equippable:
			bonus += self.head.equippable.max_damage_bonus

		if self.wrists and self.wrists.equippable:
			bonus += self.wrists.equippable.max_damage_bonus

		if self.back and self.back.equippable:
			bonus += self.back.equippable.max_damage_bonus

		return bonus

	@property
	def strength_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.strength_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.strength_bonus

		if self.chest and self.chest.equippable:
			bonus += self.chest.equippable.strength_bonus

		if self.legs and self.legs.equippable:
			bonus += self.legs.equippable.strength_bonus

		if self.feet and self.feet.equippable:
			bonus += self.feet.equippable.strength_bonus

		if self.arms and self.arms.equippable:
			bonus += self.arms.equippable.strength_bonus

		if self.hands and self.hands.equippable:
			bonus += self.hands.equippable.strength_bonus

		if self.shoulders and self.shoulders.equippable:
			bonus += self.shoulders.equippable.strength_bonus

		if self.head and self.head.equippable:
			bonus += self.head.equippable.strength_bonus

		if self.wrists and self.wrists.equippable:
			bonus += self.wrists.equippable.strength_bonus

		if self.back and self.back.equippable:
			bonus += self.back.equippable.strength_bonus

		return bonus

	@property
	def dexterity_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.dexterity_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.dexterity_bonus

		if self.chest and self.chest.equippable:
			bonus += self.chest.equippable.dexterity_bonus

		if self.legs and self.legs.equippable:
			bonus += self.legs.equippable.dexterity_bonus

		if self.feet and self.feet.equippable:
			bonus += self.feet.equippable.dexterity_bonus

		if self.arms and self.arms.equippable:
			bonus += self.arms.equippable.dexterity_bonus

		if self.hands and self.hands.equippable:
			bonus += self.hands.equippable.dexterity_bonus

		if self.shoulders and self.shoulders.equippable:
			bonus += self.shoulders.equippable.dexterity_bonus

		if self.head and self.head.equippable:
			bonus += self.head.equippable.dexterity_bonus

		if self.wrists and self.wrists.equippable:
			bonus += self.wrists.equippable.dexterity_bonus

		if self.back and self.back.equippable:
			bonus += self.back.equippable.dexterity_bonus

		return bonus

	@property
	def stamina_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.stamina_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.stamina_bonus

		if self.chest and self.chest.equippable:
			bonus += self.chest.equippable.stamina_bonus

		if self.legs and self.legs.equippable:
			bonus += self.legs.equippable.stamina_bonus

		if self.feet and self.feet.equippable:
			bonus += self.feet.equippable.stamina_bonus

		if self.arms and self.arms.equippable:
			bonus += self.arms.equippable.stamina_bonus

		if self.hands and self.hands.equippable:
			bonus += self.hands.equippable.stamina_bonus

		if self.shoulders and self.shoulders.equippable:
			bonus += self.shoulders.equippable.stamina_bonus

		if self.head and self.head.equippable:
			bonus += self.head.equippable.stamina_bonus

		if self.wrists and self.wrists.equippable:
			bonus += self.wrists.equippable.stamina_bonus

		if self.back and self.back.equippable:
			bonus += self.back.equippable.stamina_bonus

		return bonus

	@property
	def intelligence_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.intelligence_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.intelligence_bonus

		if self.chest and self.chest.equippable:
			bonus += self.chest.equippable.intelligence_bonus

		if self.legs and self.legs.equippable:
			bonus += self.legs.equippable.intelligence_bonus

		if self.feet and self.feet.equippable:
			bonus += self.feet.equippable.intelligence_bonus

		if self.arms and self.arms.equippable:
			bonus += self.arms.equippable.intelligence_bonus

		if self.hands and self.hands.equippable:
			bonus += self.hands.equippable.intelligence_bonus

		if self.shoulders and self.shoulders.equippable:
			bonus += self.shoulders.equippable.intelligence_bonus

		if self.head and self.head.equippable:
			bonus += self.head.equippable.intelligence_bonus

		if self.wrists and self.wrists.equippable:
			bonus += self.wrists.equippable.intelligence_bonus

		if self.back and self.back.equippable:
			bonus += self.back.equippable.intelligence_bonus

		return bonus

	@property
	def armor_bonus(self):
		bonus = 0

		if self.main_hand and self.main_hand.equippable:
			bonus += self.main_hand.equippable.armor_bonus

		if self.off_hand and self.off_hand.equippable:
			bonus += self.off_hand.equippable.armor_bonus

		if self.chest and self.chest.equippable:
			bonus += self.chest.equippable.armor_bonus

		if self.legs and self.legs.equippable:
			bonus += self.legs.equippable.armor_bonus

		if self.feet and self.feet.equippable:
			bonus += self.feet.equippable.armor_bonus

		if self.arms and self.arms.equippable:
			bonus += self.arms.equippable.armor_bonus

		if self.hands and self.hands.equippable:
			bonus += self.hands.equippable.armor_bonus

		if self.shoulders and self.shoulders.equippable:
			bonus += self.shoulders.equippable.armor_bonus

		if self.head and self.head.equippable:
			bonus += self.head.equippable.armor_bonus

		if self.wrists and self.wrists.equippable:
			bonus += self.wrists.equippable.armor_bonus

		if self.back and self.back.equippable:
			bonus += self.back.equippable.armor_bonus

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

		elif slot == EquipmentSlots.CHEST:
			if self.chest == equippable_entity:
				self.chest = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.chest:
					results.append({'unequipped': self.chest})

				self.chest = equippable_entity
				results.append({'equipped': equippable_entity})

		elif slot == EquipmentSlots.LEGS:
			if self.legs == equippable_entity:
				self.legs = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.legs:
					results.append({'unequipped': self.legs})

				self.legs = equippable_entity
				results.append({'equipped': equippable_entity})

		elif slot == EquipmentSlots.FEET:
			if self.feet == equippable_entity:
				self.feet = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.feet:
					results.append({'unequipped': self.feet})

				self.feet = equippable_entity
				results.append({'equipped': equippable_entity})

		elif slot == EquipmentSlots.ARMS:
			if self.arms == equippable_entity:
				self.arms = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.arms:
					results.append({'unequipped': self.arms})

				self.arms = equippable_entity
				results.append({'equipped': equippable_entity})

		elif slot == EquipmentSlots.HANDS:
			if self.hands == equippable_entity:
				self.hands = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.hands:
					results.append({'unequipped': self.hands})

				self.hands = equippable_entity
				results.append({'equipped': equippable_entity})

		elif slot == EquipmentSlots.SHOULDERS:
			if self.shoulders == equippable_entity:
				self.shoulders = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.shoulders:
					results.append({'unequipped': self.shoulders})

				self.shoulders = equippable_entity
				results.append({'equipped': equippable_entity})

		elif slot == EquipmentSlots.HEAD:
			if self.head == equippable_entity:
				self.head = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.head:
					results.append({'unequipped': self.head})

				self.head = equippable_entity
				results.append({'equipped': equippable_entity})

		elif slot == EquipmentSlots.WRISTS:
			if self.wrists == equippable_entity:
				self.wrists = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.wrists:
					results.append({'unequipped': self.wrists})

				self.wrists = equippable_entity
				results.append({'equipped': equippable_entity})

		elif slot == EquipmentSlots.BACK:
			if self.back == equippable_entity:
				self.back = None
				results.append({'unequipped': equippable_entity})
			else:
				if self.back:
					results.append({'unequipped': self.back})

				self.back = equippable_entity
				results.append({'equipped': equippable_entity})


		return results