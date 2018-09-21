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


def select_name_menu(con, select_race_width, screen_width, screen_height):
	libtcod.console_clear(con)
	libtcod.console_set_default_background(con, libtcod.black)
	libtcod.console_set_default_foreground(con, libtcod.white)

	menu(con, 'Character Creation\n\nEnter Name: ', libtcod.darker_blue, "", 26, screen_width, screen_height, False)

def select_race_menu(con, select_race_width, screen_width, screen_height, races):
	libtcod.console_clear(con)
	libtcod.console_set_default_background(con, libtcod.black)
	libtcod.console_set_default_foreground(con, libtcod.white)

	menu(con, 'Character Creation\n\nSelect Race\n\n', libtcod.darker_blue, races, 22, screen_width, screen_height)



def select_combat_class_menu(con, select_race_width, screen_width, screen_height, combat_classes):
	libtcod.console_clear(con)
	libtcod.console_set_default_background(con, libtcod.black)
	libtcod.console_set_default_foreground(con, libtcod.white)

	menu(con, 'Character Creation\n\nSelect Class\n\n', libtcod.darker_blue, combat_classes, 22, screen_width, screen_height)




	