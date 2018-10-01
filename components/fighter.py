import libtcodpy as libtcod

from random import randint

from game_messages import Message



class Fighter():
	def __init__(self, hp, mp, defense, power, xp=0):
		self.base_max_hp = hp
		self.hp = hp
		self.base_max_mp = mp
		self.mp = mp
		self.base_defense = defense
		self.base_power = power
		self.min_power = 1
		self.xp = xp

	@property
	def max_hp(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.max_hp_bonus
		else:
			bonus = 0

		return self.base_max_hp + bonus

	@property
	def power(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.power_bonus
		else:
			bonus = 0

		return self.base_power + bonus

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

		damage = int(randint(self.min_power, self.power) * (1 / (1+target.combat_class.armor)))

		if damage > 0:
			results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(
				self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
			results.extend(target.combat_class.take_damage(damage))
		else:
			results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
				self.owner.name.capitalize(), target.name), libtcod.white)})

		return results
