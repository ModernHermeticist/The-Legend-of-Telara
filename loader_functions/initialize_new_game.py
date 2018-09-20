import libtcodpy as libtcod

from components.combat_classes.fighter import Fighter
from components.combat_classes.warrior import Warrior
from components.races.human import Human
from components.inventory import Inventory
from components.level import Level
from components.equipment import Equipment
from components.equippable import Equippable

from interfaces.character_creation_menu import character_creation_menu

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
	char_info_panel_height = 4
	area_info_panel_height = 1
	under_mouse_panel_height = 1
	panel_y = screen_height - panel_height

	message_panel_width = int((screen_width / 3) + 10)
	char_info_panel_width = int((screen_width / 4))
	area_info_panel_width = int((screen_width / 4) - 10)
	under_mouse_panel_width = int((screen_width / 4) - 10)

	message_log_x = bar_width + 2
	message_width = screen_width - bar_width - 2
	message_height = panel_height - 1


	# Size of the map
	map_width = 110
	map_height = 50

	# Some variables for the rooms in the map
	room_max_size = 10
	room_min_size = 5
	max_rooms = 30

	fov_algorithm = 0
	fov_light_walls = True
	fov_radius = 7

	max_monsters_per_room = 8

	max_items_per_room = 2

	colors = {
		'dark_wall': libtcod.Color(0, 0, 100),
		'dark_ground': libtcod.Color(50, 50, 150),
		'light_wall': libtcod.Color(130, 110, 50),
		'light_ground': libtcod.Color(200, 180, 50)
	}

	races = {
		'human': Human()
	}

	combat_classes = {
		'warrior': Warrior()
	}

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
				'races':                    races,
				'combat_classes':           combat_classes
	}

	return constants

def get_new_game_variables(constants):

	player = character_creation_menu(0, 50, constants['screen_width'], constants['screen_height'],
										entity, constants['combat_classes'], constants['races'])

	entities = [player]

	game_map = GameMap(constants['map_width'], constants['map_height'])

	game_map.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
					  constants['map_width'], constants['map_height'], player, entities)
	message_log = MessageLog(constants['message_log_x'], constants['message_width'], constants['message_panel_height'])
	game_state = GameStates.PLAYERS_TURN

	return player, entities, game_map, message_log, game_state
