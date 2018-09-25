import libtcodpy as libtcod

from random import randint

from game_messages import Message



class Fighter():
	def __init__(self, hp, mp, armor, min_damage=0, max_damage=1, xp=0):
		self.base_max_hp = hp
		self.hp = hp
		self.base_max_mp = mp
		self.mp = mp
		self.armor = armor
		self.min_damage = min_damage
		self.max_damage = max_damage
		self.xp = xp

	
	"""
	@property
	def max_hp(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.max_hp_bonus
		else:
			bonus = 0

		return self.base_max_hp + bonus

	@property
	def min_damage(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.strength_bonus
		else:
			bonus = 0

		return self.base_strength + bonus

	@property
	def defense(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.defense_bonus
		else:
			bonus = 0

		return self.base_defense + bonus

	@property
	def max_mp(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.max_mp_bonus
		else:
			bonus = 0

		return self.base_max_mp + bonus
	"""
	

	def take_damage(self, amount):
		results = []

		self.hp -= amount

		if self.hp <= 0:
			results.append({'dead': self.owner, 'xp': self.xp})

		return results

	def heal(self, amount):
		self.hp += amount

		if self.hp > self.max_hp:
			self.hp = self.max_hp

	def attack(self, target):
		results = []

		damage = randint(self.min_damage, self.max_damage) - target.combat_class.armor

		if damage > 0:
			results.append({'message': Message('{0} attacks {1} for {2} damage.'.format(
				self.owner.name.capitalize(), target.name, str(damage)), libtcod.orange)})
			results.extend(target.combat_class.take_damage(damage))
		else:
			results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
				self.owner.name.capitalize(), target.name), libtcod.dark_orange)})

		return results
