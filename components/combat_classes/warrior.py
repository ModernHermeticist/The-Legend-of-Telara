import libtcodpy as libtcod

from random import randint

from game_messages import Message



class Warrior():
	def __init__(self, class_name='Warrior', hp=10, mp=0, armor=0, min_damage=0, max_damage=1, 
				strength=1, dexterity=0, stamina=1, intelligence=0, xp=0):
		self.base_max_hp =            hp
		self.hp =                     hp
		self.base_max_mp =            mp
		self.mp =                     mp
		self.base_min_damage =        min_damage
		self.base_max_damage =        max_damage
		self.base_armor =             armor
		self.base_strength =          strength
		self.base_dexterity =         dexterity
		self.base_stamina =           stamina
		self.base_intelligence =      intelligence
		self.xp =                     xp
		self.class_name =             class_name

		self.turns_until_rest =       0

	@property
	def max_hp(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.max_hp_bonus + (int(self.stamina / 3)*10)
		else:
			bonus = 0

		return self.base_max_hp + bonus

	@property
	def strength(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.strength_bonus
		else:
			bonus = 0

		return self.base_strength + bonus

	@property
	def dexterity(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.dexterity_bonus
		else:
			bonus = 0

		return self.base_dexterity + bonus

	@property
	def stamina(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.stamina_bonus
		else:
			bonus = 0

		return self.base_stamina + bonus

	@property
	def intelligence(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.intelligence_bonus
		else:
			bonus = 0

		return self.base_intelligence + bonus

	@property
	def armor(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.armor_bonus
		else:
			bonus = 0

		return self.base_armor + bonus

	@property
	def min_damage(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.min_damage_bonus
		else:
			bonus = 0

		return self.base_min_damage + bonus + int(self.strength / 3)

	@property
	def max_damage(self):
		if self.owner and self.owner.equipment:
			bonus = self.owner.equipment.max_damage_bonus
		else:
			bonus = 0

		return self.base_max_damage + bonus + int(self.strength / 3)

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

		if self.turns_until_rest == 5:
			pass
		else:
			self.turns_until_rest = 5


		return results

	def heal(self, amount):
		self.hp += amount

		if self.hp > self.max_hp:
			self.hp = self.max_hp

	def rest(self):
		if self.turns_until_rest != 0:
			return 'The recent combat keeps you from resting.'
		rest_max = int(0.55 * self.max_hp) 
		if self.hp >= rest_max:
			return 'Resting can only soothe your wounds so much.'

		amount = randint(1, int(self.max_hp / 20))
		self.hp += amount

		if self.hp > rest_max:
			self.hp = rest_max

		return 'You sense that the noise made by resting may have drawn enemies. Despite that you feel slightly refreshed.'

	def attack(self, target):
		results = []

		damage = int(randint(self.min_damage, self.max_damage) * (1 / (1+target.combat_class.armor)))

		if damage > 0:
			results.append({'message': Message('{0} attacks {1} for {2} damage.'.format(
				self.owner.name.capitalize(), target.name, str(damage)), libtcod.lighter_orange)})
			results.extend(target.combat_class.take_damage(damage))
		else:
			results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
				self.owner.name.capitalize(), target.name), libtcod.light_orange)})

		return results
