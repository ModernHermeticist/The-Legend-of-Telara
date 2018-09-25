import libtcodpy as libtcod

from components.combat_classes.fighter import Fighter
from components.combat_classes.warrior import Warrior
from components.combat_classes.archer import Archer
from components.races.human import Human
from components.inventory import Inventory
from components.level import Level
from components.equipment import Equipment
from components.equippable import Equippable

from interfaces.character_creation_menu import select_race_menu, select_combat_class_menu, select_name_menu, select_sex_menu

from input_handlers import handle_keys

from entity import Entity

from equipment_slots import EquipmentSlots

from game_messages import MessageLog

from game_states import GameStates

from map_objects.game_map import GameMap

from render_functions import RenderOrder

def get_constants():
	window_title = 'The Legend of Telara'

	screen_width = 120
	screen_height = 70

	bar_width = 21
	panel_height = 7
	message_panel_height = 7
	char_info_panel_height = 8
	area_info_panel_height = 1
	under_mouse_panel_height = 1
	panel_y = screen_height - panel_height

	message_panel_width = int((screen_width / 3) + 15)
	char_info_panel_width = int((screen_width / 4))
	area_info_panel_width = int((screen_width / 4) - 10)
	under_mouse_panel_width = int((screen_width / 4) - 10)

	message_log_x = message_panel_width - 6
	#message_width = screen_width - bar_width - 6
	message_width = message_panel_width
	message_height = panel_height - 1


	# Size of the map
	map_width = 110
	map_height = 50

	# Some variables for the rooms in the map
	room_max_size = 10
	room_min_size = 4
	max_rooms = 60

	fov_algorithm = 0
	fov_light_walls = True
	fov_radius = 7

	max_monsters_per_room = 8

	max_items_per_room = 2

	colors = {
		'dark_wall':            libtcod.Color(0, 0, 100),
		'dark_ground':          libtcod.Color(50, 50, 150),
		'light_wall':           libtcod.Color(130, 110, 50),
		'light_ground':         libtcod.Color(200, 180, 50),
		'area_of_effect':       libtcod.Color(255, 140, 0),
		'targeting_range':      libtcod.Color(152, 251, 152)  
	}

	sexes = ['Male',
		     'Female']

	races = ['Human']

	combat_classes = ['Warrior',
					  'Archer']
	

	constants = {
				'window_title':             window_title,
				'screen_width':             screen_width,
				'screen_height':            screen_height,
				'bar_width':                bar_width,
				'panel_height':             panel_height,
				'area_info_panel_height':   area_info_panel_height,
				'char_info_panel_height':   char_info_panel_height,
				'panel_y':                  panel_y,
				'message_log_x':            message_log_x,
				'message_width':            message_width,
				'message_panel_height':     message_panel_height,
				'message_panel_width':      message_panel_width,
				'under_mouse_panel_height': under_mouse_panel_height,
				'under_mouse_panel_width':  under_mouse_panel_width,
				'char_info_panel_width':    char_info_panel_width,
				'area_info_panel_width':    area_info_panel_width,
				'map_width':                map_width,
				'map_height':               map_height,
				'room_max_size':            room_max_size,
				'room_min_size':            room_min_size,
				'max_rooms':                max_rooms,
				'fov_algorithm':            fov_algorithm,
				'fov_light_walls':          fov_light_walls,
				'fov_radius':               fov_radius,
				'max_monsters_per_room':    max_monsters_per_room,
				'max_items_per_room':       max_items_per_room,
				'colors':                   colors,
				'sexes':                    sexes,
				'races':                    races,
				'combat_classes':           combat_classes
	}

	return constants

def get_new_game_variables(constants):
	race_component = None
	class_component = None
	game_state = GameStates.SELECT_SEX
	previous_game_state = game_state
	key = libtcod.Key()
	mouse = libtcod.Mouse()


	while not libtcod.console_is_window_closed():
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
		libtcod.console_flush()
		action = handle_keys(key, game_state)

		if game_state == GameStates.SELECT_SEX:
			select_sex_menu(0, 50, constants['screen_width'], constants['screen_height'], constants['sexes'])

			action = handle_keys(key, game_state)

			male = action.get('male')
			female = action.get('female')

			exit = action.get('exit')

			if male:
				sex = 'Male'
				game_state = GameStates.ENTER_PLAYER_NAME

			elif female:
				sex = 'Female'
				game_state = GameStates.ENTER_PLAYER_NAME

			elif exit:
				break



		elif game_state == GameStates.ENTER_PLAYER_NAME:
			select_name_menu(0, 50, constants['screen_width'], constants['screen_height'])
			libtcod.console_flush()
			name = enter_player_name(constants['screen_width'], constants['screen_height'])
			if name == None:
				game_state = GameStates.SELECT_SEX
			else:
				game_state = GameStates.SELECT_RACE

		elif game_state == GameStates.SELECT_RACE:
			select_race_menu(0, 50, constants['screen_width'], constants['screen_height'], constants['races'])

			action = handle_keys(key, game_state)

			human = action.get('human')

			exit = action.get('exit')

			if human:
				race_component = Human()
				game_state = GameStates.SELECT_CLASS

			elif exit:
				game_state = GameStates.ENTER_PLAYER_NAME

		elif game_state == GameStates.SELECT_CLASS:
			select_combat_class_menu(0, 50, constants['screen_width'], constants['screen_height'], constants['combat_classes'])

			action = handle_keys(key, game_state)

			warrior = action.get('warrior')
			archer =  action.get('archer')

			exit =    action.get('exit')

			if warrior:
				class_component = Warrior()
				break

			if archer:
				class_component = Archer()
				break

			elif exit:
				game_state = GameStates.SELECT_RACE
	if exit:
		libtcod.console_clear(0)
		libtcod.console_flush()
		return None, None, None, None, None		

	inventory_component = Inventory(26)
	level_component = Level()
	equipment_component = Equipment()

	player = Entity(0, 0, '@', libtcod.white, name, sex, blocks=True, render_order=RenderOrder.ACTOR, 
					combat_class=class_component, race=race_component, inventory=inventory_component, level=level_component,
					equipment=equipment_component)

	player = apply_class_stats_to_race(player)

	if player.combat_class.class_name == 'Warrior': 
		equippable_component = Equippable(EquipmentSlots.MAIN_HAND, min_damage_bonus=0, max_damage_bonus=1)
		dagger = Entity(0,0, '-', libtcod.sky, 'Dagger', equippable=equippable_component)

		dagger.item.description = "Better than your bare hands."

		player.inventory.add_item(dagger)
		player.equipment.toggle_equip(dagger)

	elif player.combat_class.class_name == 'Archer': 
		equippable_component = Equippable(EquipmentSlots.MAIN_HAND, min_damage_bonus=0, max_damage_bonus=1)
		dagger = Entity(0,0, '-', libtcod.sky, 'Dagger', equippable=equippable_component)

		dagger.item.description = "Better than your bare hands."

		player.inventory.add_item(dagger)
		player.equipment.toggle_equip(dagger)

	entities = [player]

	game_map = GameMap(constants['map_width'], constants['map_height'])

	game_map.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
					  constants['map_width'], constants['map_height'], player, entities)
	message_log = MessageLog(constants['message_log_x'], constants['message_width'], constants['message_panel_height'])
	game_state = GameStates.PLAYERS_TURN

	return player, entities, game_map, message_log, game_state

def apply_class_stats_to_race(player):

	player.combat_class.base_max_hp += player.race.hp
	player.combat_class.hp += player.race.hp

	player.combat_class.base_max_mp += player.race.mp
	player.combat_class.mp += player.race.mp

	player.combat_class.base_strength += player.race.strength

	player.combat_class.base_armor += player.race.armor

	player.combat_class.base_min_damage += player.race.min_damage
	player.combat_class.base_max_damage += player.race.max_damage
	return player

def enter_player_name(screen_width, screen_height):
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
			   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
			   'w', 'x', 'y', 'z']
	name = ''
	x = len(name) + int(screen_width / 2 - 11) + 10
	y = int(screen_height / 2)
	key = libtcod.console_wait_for_keypress(True)
	while True:
		if key.vk == libtcod.KEY_BACKSPACE:
			if len(name) >= 0:
				name = name[0:len(name)-1]
				libtcod.console_print_ex(0, x, y, libtcod.BKGND_NONE, libtcod.LEFT, ' ')
				libtcod.console_flush()
		else:
			letter = chr(key.c)
			for item in letters:
				if letter == item:
					if len(name) <= 12:
						name = name + letter  #add to the string
						if len(name) == 1:
							name = name.capitalize()
							letter = letter.capitalize()
						#libtcod.console_set_char(0, x,  y, letter)  #print new character at appropriate position on screen
						libtcod.console_print_ex(0, x, y, libtcod.BKGND_NONE, libtcod.LEFT, letter)

						libtcod.console_set_default_foreground(0, libtcod.white)  #make it white or something
						libtcod.console_flush()
					break
		x = len(name) + int(screen_width / 2 - 11) + 10
		key = libtcod.console_wait_for_keypress(True)

		if key.vk == libtcod.KEY_ESCAPE:
			libtcod.console_clear(0)
			libtcod.console_flush()
			return None
		elif len(name) > 0 and key.vk == libtcod.KEY_ENTER:
			return name