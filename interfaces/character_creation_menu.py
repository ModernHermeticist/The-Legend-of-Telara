import libtcodpy as libtcod

from interfaces.menus import menu

from entity import Entity

from components.combat_classes.warrior import Warrior
from components.races.human import Human

from components.level import Level

from components.inventory import Inventory
from components.equipment import Equipment
from components.equippable import Equippable
from equipment_slots import EquipmentSlots
from render_functions import RenderOrder

def character_creation_menu(con, character_creation_width, screen_width, screen_height, combat_classes, races):
	inventory_component = Inventory(26)
	level_component = Level()
	equipment_component = Equipment()
	"""
	SO HERE WE NEED TO HANDLE DECIDING WHAT OUR CHARACTER WILL BE SO WE CAN SET "PLAYER" EQUAL TO IT
	"""


	player = Entity(0, 0, '@', libtcod.white, 'Player', blocks=True, render_order=RenderOrder.ACTOR, 
					combat_class=class_component, inventory=inventory_component, level=level_component,
					equipment=equipment_component)


	"""
	HERE WE ARE ASSIGNING INITIAL EQUIPMENT
	ACTUALLY WE COULD PROBABLY HARD CODE THE CLASS TEMPLATES WITH GEAR
	"""


	equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2)
	dagger = Entity(0,0, '-', libtcod.sky, 'Dagger', equippable=equippable_component)
	player.inventory.add_item(dagger)
	player.equipment.toggle_equip(dagger)

	return player

	