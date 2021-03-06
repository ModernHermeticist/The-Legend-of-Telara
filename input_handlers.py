import libtcodpy as libtcod

from game_states import GameStates


def handle_keys(key, game_state):
	if game_state == GameStates.PLAYERS_TURN:
		return handle_player_turn_keys(key)
	elif game_state == GameStates.PLAYER_DEAD:
		return handle_player_dead_keys(key)
	elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
		return handle_inventory_keys(key)
	elif game_state == GameStates.CHOOSE_ITEM_TO_INSPECT:
		return handle_choose_item_to_inspect_keys(key)
	elif game_state == GameStates.INSPECT_ITEM:
		return handle_inspect_item_keys(key)
	elif game_state == GameStates.TARGETING:
		return handle_targeting_keys(key)
	elif game_state == GameStates.LEVEL_UP:
		return handle_level_up_menu(key)
	elif game_state == GameStates.CHARACTER_SCREEN:
		return handle_character_screen(key)
	elif game_state == GameStates.EQUIPMENT_SCREEN:
		return handle_equipment_screen(key)
	elif game_state == GameStates.EQUIPMENT_DETAILS:
		return handle_equipment_details(key)
	elif game_state == GameStates.INTERACT:
		return handle_interacting_keys(key)
	elif game_state == GameStates.SELECT_RACE:
		return handle_select_race_keys(key)
	elif game_state == GameStates.SELECT_CLASS:
		return handle_select_combat_class_keys(key)
	elif game_state == GameStates.SELECT_SEX:
		return handle_select_sex_keys(key)

	return {}

def handle_player_turn_keys(key):

	key_char = chr(key.c)
	# Movement keys
	if key.vk == libtcod.KEY_UP or key_char == 'i':
		return {'move': (0, -1)}
	elif key.vk == libtcod.KEY_DOWN or key_char == ',':
		return {'move': (0, 1)}
	elif key.vk == libtcod.KEY_LEFT or key_char == 'j':
		return {'move': (-1, 0)}
	elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
		return {'move': (1, 0)}
	elif key_char == 'u':
		return {'move': (-1, -1)}
	elif key_char == 'o':
		return {'move': (1, -1)}
	elif key_char == 'm':
		return {'move': (-1, 1)}
	elif key_char == '.':
		return {'move': (1, 1)}
	elif key_char == 'z':
		return {'wait': True}
	elif key_char == 'g':
		return {'pickup': True}
	elif key_char == 'c':
		return {'show_inventory': True}
	elif key_char == 'd':
		return {'drop_inventory': True}
	elif key_char == 'q':
		return {'take_stairs': True}
	elif key_char == 'a':
		return {'show_character_screen': True}
	elif key_char == 'e':
		return {'show_equipment_screen': True}
	elif key_char == 'r':
		return {'ranged_attack': True}
	elif key.vk == libtcod.KEY_SPACE:
		return {'interact': True}

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: toggle full screen
		return {'fullscreen': True}

	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the game
		return {'exit': True}

	# No key was pressed
	return {}


def handle_equipment_screen(key):
	key_char = chr(key.c)

	if key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}

	elif key_char == 'e':
		return {'exit': True}

	elif key_char == 'm':
		return {'main_hand': True}

	elif key_char == 'o':
		return {'off_hand': True}

	elif key_char == 'h':
		return {'head': True}

	elif key_char == 's':
		return {'shoulders': True}

	elif key_char == 'a':
		return {'arms': True}

	elif key_char == 'w':
		return {'wrists': True}

	elif key_char == 'n':
		return {'hands': True}

	elif key_char == 'c':
		return {'chest': True}

	elif key_char == 'b':
		return {'belt': True}

	elif key_char == 'l':
		return {'legs': True}

	elif key_char == 'f':
		return {'feet': True}

	elif key_char == 'k':
		return {'back': True}

	return {}

def handle_equipment_details(key):
	if key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}

	return {}


def handle_character_screen(key):
	key_char = chr(key.c)

	if key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}

	elif key_char == 'a':
		return {'exit': True}

	return {}

def handle_inventory_keys(key):
	index = key.c - ord('a')

	if index >= 0:
		return {'inventory_index': index}

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: toggle fullscreen
		return {'fullscreen': True}

	elif key.vk == libtcod.KEY_SPACE:
		return {'inspect_item': True}

	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the menu
		return {'exit': True}

	return {}


def handle_choose_item_to_inspect_keys(key):
	index = key.c - ord('a')

	if index >= 0:
		return {'inventory_index': index}

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: toggle fullscreen
		return {'fullscreen': True}

	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the menu
		return {'exit': True}

	return {}

def handle_inspect_item_keys(key):
	if key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}

	return {}

def handle_select_sex_keys(key):
	key_char = chr(key.c)

	if key_char == 'a':
		return {'male': True}

	elif key_char == 'b':
		return {'female': True}

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: toggle fullscreen
		return {'fullscreen': True}

	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the menu
		return {'exit': True}

	return {}

def handle_select_race_keys(key):
	key_char = chr(key.c)

	if key_char == 'a':
		return {'human': True}

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: toggle fullscreen
		return {'fullscreen': True}

	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the menu
		return {'exit': True}

	return {}

def handle_select_combat_class_keys(key):
	key_char = chr(key.c)

	if key_char == 'a':
		return {'warrior': True}

	if key_char == 'b':
		return {'archer': True}

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: toggle fullscreen
		return {'fullscreen': True}

	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the menu
		return {'exit': True}

	return {}

def handle_targeting_keys(key):
	if key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}

	return {}

def handle_interacting_keys(key):
	key_char = chr(key.c)

	if key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}
	elif key.vk == libtcod.KEY_UP or key_char == 'i':
		return {'move': (0, -1)}
	elif key.vk == libtcod.KEY_DOWN or key_char == ',':
		return {'move': (0, 1)}
	elif key.vk == libtcod.KEY_LEFT or key_char == 'j':
		return {'move': (-1, 0)}
	elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
		return {'move': (1, 0)}
	elif key_char == 'u':
		return {'move': (-1, -1)}
	elif key_char == 'o':
		return {'move': (1, -1)}
	elif key_char == 'm':
		return {'move': (-1, 1)}
	elif key_char == '.':
		return {'move': (1, 1)}

	return {}

def handle_controls_menu(key):
	if key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}

	return {}



def handle_player_dead_keys(key):
	key_char = chr(key.c)

	if key_char == 'i':
		return {'show_inventory': True}

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: toggle fullscreen
		return {'fullscreen': True}
	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the menu
		return {'exit': True}

	return {}

def handle_main_menu(key):
	key_char = chr(key.c)

	if key_char == 'a':
		return {'new_game': True}

	elif key_char == 'b':
		return {'load_game': True}

	elif key_char == 'c':
		return {'controls': True}

	elif key_char == 'd' or key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}

	return {}

def handle_level_up_menu(key):
	if key:
		key_char = chr(key.c)

		if key_char == 'a':
			return {'level_up': 'str'}
		elif key_char == 'b':
			return {'level_up': 'dex'}
		elif key_char == 'c':
			return {'level_up': 'sta'}
		elif key_char == 'd':
			return {'level_up': 'int'}

	return {}

def handle_mouse(mouse):
	(x, y) = (mouse.cx, mouse.cy)

	if mouse.lbutton_pressed:
		return {'left_click': (x, y)}
	elif mouse.rbutton_pressed:
		return {'right_click': (x, y)}

	return {}