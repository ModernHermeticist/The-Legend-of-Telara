import libtcodpy as libtcod
#from pygame import mixer


from death_functions import kill_monster, kill_player
from entity import get_blocking_entities_at_location, get_non_blocking_entities_at_location
from fov_functions import initialize_fov, recompute_fov
from game_messages import Message
from game_states import GameStates
from input_handlers import handle_keys, handle_mouse, handle_main_menu, handle_controls_menu
from render_functions import clear_all, render_all
from loader_functions.initialize_new_game import get_constants, get_new_game_variables
from loader_functions.data_loaders import load_game, save_game
from interfaces.menus import main_menu, message_box, controls_menu

from font_functions import load_customfont


def play_game(player, entities, game_map, message_log, game_state, con, message_panel,
					 char_info_panel, area_info_panel, under_mouse_panel, constants, floor_index, 
					 original_entity_index, entity_index, fov_index):
	fov_recompute = True
	fov_map = initialize_fov(game_map)
	key = libtcod.Key()
	mouse = libtcod.Mouse()

	game_state = GameStates.PLAYERS_TURN
	previous_game_state = game_state

	mouse_x = mouse.cx
	old_mouse_x = mouse_x

	mouse_y = mouse.cy
	old_mouse_y = mouse_y

	#attack_animation_x = 0
	#attack_animation_y = 0

	clean_map = False

	#attacked = False

	#animation_time = 200
	#animation_distance = 0

	targeting_item = None

	equipment_choice = 0

	npc = None

	item = None

	while not libtcod.console_is_window_closed():
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
		"""
		if animation_time == 0:
			if attacked:
				animation_distance += 1
			animation_time = 200

		if animation_distance == 5:
			animation_distance = 0
			attacked = False
		"""

		if clean_map == True:
			fov_recompute = True
			clean_map = False

		if fov_recompute:
			recompute_fov(fov_map, player.x, player.y, constants['fov_radius'], constants['fov_light_walls'], constants['fov_algorithm'])

		render_all(con, message_panel, char_info_panel, area_info_panel, under_mouse_panel, entities, 
				   player, game_map, fov_map, fov_recompute, message_log, constants['screen_width'], 
				   constants['screen_height'], constants['bar_width'], constants['panel_height'], 
				   constants['panel_y'], mouse, constants['tiles'], constants['colors'], game_state, npc, targeting_item, item, equipment_choice)


		fov_recompute = False

		libtcod.console_flush()

		clear_all(con, entities, fov_map, game_map)

		action = handle_keys(key, game_state)
		mouse_action = handle_mouse(mouse)

		############################################
		if game_state == GameStates.EQUIPMENT_SCREEN and not action.get('exit'):
			for equipment in action:
				if equipment:
					equipment_choice = equipment
					break

		############################################

		move =                  action.get('move')
		ranged_attack =         action.get('ranged_attack')
		interact =              action.get('interact')
		inspect_item =          action.get('inspect_item')
		wait =                  action.get('wait')
		pickup =                action.get('pickup')
		show_inventory =        action.get('show_inventory')
		drop_inventory =        action.get('drop_inventory')
		inventory_index =       action.get('inventory_index')
		take_stairs =           action.get('take_stairs')
		level_up =              action.get('level_up')
		show_character_screen = action.get('show_character_screen')
		show_equipment_screen = action.get('show_equipment_screen')
		exit =                  action.get('exit')
		fullscreen =            action.get('fullscreen')

		left_click = mouse_action.get('left_click')
		right_click = mouse_action.get('right_click')

		player_turn_results = []

		if move and game_state == GameStates.PLAYERS_TURN:
			dx, dy = move
			destination_x = player.x + dx
			destination_y = player.y + dy

			if not game_map.is_blocked(destination_x, destination_y):
				target = get_blocking_entities_at_location(entities, destination_x, destination_y)

				if target and not target.invulnerable:
					attack_results = player.combat_class.attack(target)
					player_turn_results.extend(attack_results)

					clean_map = True


				elif not target:
					player.move(dx, dy)

					if player.combat_class.turns_until_rest == 0:
						pass
					else:
						player.combat_class.turns_until_rest -= 1

					fov_recompute = True

				game_state = GameStates.ENEMY_TURN

		elif move and game_state == GameStates.INTERACT:
			dx, dy = move
			destination_x = player.x + dx
			destination_y = player.y + dy

			if not game_map.is_blocked(destination_x, destination_y):
				blocking_target = get_blocking_entities_at_location(entities, destination_x, destination_y)
				non_blocking_target = get_non_blocking_entities_at_location(entities, destination_x, destination_y)

				if blocking_target:
					try:
						if blocking_target.dialogue.dialogue:
							npc = blocking_target
					except (AttributeError):
						pass
					if blocking_target.bonfire is not None:
						message_log.add_message(Message('You see a mysterious bonfire. You cannot resist touching it', libtcod.light_violet))
						entity_index = blocking_target.bonfire.reset_entities(game_map, original_entity_index, entity_index)
						game_state = GameStates.PLAYERS_TURN
					else:
						message_log.add_message(Message('You see {0}'.format(blocking_target.name), libtcod.white))

				elif non_blocking_target:
					message_log.add_message(Message('You see {0}'.format(non_blocking_target.name), libtcod.white))

				else:
					message_log.add_message(Message('There is nothing to inspect here.', libtcod.white))



		elif wait:
			if player.combat_class.turns_until_rest == 0:
				pass
			else:
				player.combat_class.turns_until_rest -= 1

			message = player.combat_class.rest()
			message_log.add_message(Message(message, libtcod.green))
			game_state = GameStates.ENEMY_TURN

		elif pickup and game_state == GameStates.PLAYERS_TURN:
			for entity in entities:
				if entity.item and entity.x == player.x and entity.y == player.y:
					pickup_results = player.inventory.add_item(entity)
					player_turn_results.extend(pickup_results)

					break
			else:
				message_log.add_message(Message('There is nothing here to pick up.', libtcod.white))

		if show_inventory:
			previous_game_state = game_state
			game_state = GameStates.SHOW_INVENTORY

		if drop_inventory:
			previous_game_state = game_state
			game_state = GameStates.DROP_INVENTORY

		if interact:
			previous_game_state = GameStates.PLAYERS_TURN
			game_state = GameStates.INTERACT
			message_log.add_message(Message('You begin to look around.'))

		if ranged_attack:
			if player.equipment.main_hand.equippable.ranged:
				previous_game_state = GameStates.PLAYERS_TURN
				game_state = GameStates.TARGETING
				message_log.add_message(Message('Choose a target to attack.'))
			else:
				message_log.add_message(Message('This weapon cannot attack at range.'))

		if inventory_index is not None and previous_game_state != GameStates.PLAYER_DEAD and \
			inventory_index < len(player.inventory.items):
			item = player.inventory.items[inventory_index]

			if game_state == GameStates.SHOW_INVENTORY:
				player_turn_results.extend(player.inventory.use(item, entities=entities, fov_map=fov_map))
			elif game_state == GameStates.DROP_INVENTORY:
				player_turn_results.extend(player.inventory.drop_item(item))

			elif game_state == GameStates.CHOOSE_ITEM_TO_INSPECT:
				previous_game_state = GameStates.CHOOSE_ITEM_TO_INSPECT
				game_state = GameStates.INSPECT_ITEM
				message_log.add_message(Message('You inspect the {0}.'.format(item.name)))

		if take_stairs and game_state == GameStates.PLAYERS_TURN:
			for entity in entities:
				if entity.stairs and entity.x == player.x and entity.y == player.y:
					if entity.name == 'Stairs Down':
						if len(floor_index) == game_map.dungeon_level:
							entities = game_map.new_floor(player, message_log, constants)
							fov_map = initialize_fov(game_map)
							floor_index.append(game_map.tiles)
							entity_index.append(entities)
							original_entity_index.append(entities)
							fov_index.append(fov_map)
							fov_recompute = True
							libtcod.console_clear(con)
							break

						elif len(floor_index) > game_map.dungeon_level:
							# Update the entity index with the floors NEW entity list
							entity_index[game_map.dungeon_level-1] = entities
							entities, player, fov_map = game_map.next_floor(player, entity_index, floor_index, fov_index, message_log, constants)
							fov_recompute = True
							libtcod.console_clear(con)
							break


					elif entity.name == 'Stairs Up':
							entity_index[game_map.dungeon_level-1] = entities
							entities, player, fov_map = game_map.previous_floor(player, entity_index, floor_index, fov_index, message_log, constants)
							fov_recompute = True
							libtcod.console_clear(con)
							break

			else:
				message_log.add_message(Message('There are no stairs here.', libtcod.yellow))

		if level_up:
			if level_up == 'str':
				player.combat_class.base_strength += 1
			elif level_up == 'dex':
				player.combat_class.base_dexterity += 1
			elif level_up == 'sta':
				player.combat_class.base_stamina += 1
			elif level_up == 'int':
				player.combat_class.base_intelligence += 1

			game_state = previous_game_state

		if show_character_screen:
			previous_game_state = game_state
			game_state = GameStates.CHARACTER_SCREEN

		if show_equipment_screen:
			previous_game_state = game_state
			game_state = GameStates.EQUIPMENT_SCREEN


		if game_state == GameStates.TARGETING:
			mouse_x = mouse.cx
			mouse_y = mouse.cy


			if (old_mouse_y != mouse_y or old_mouse_x != mouse_x) and libtcod.map_is_in_fov(fov_map, mouse_x, mouse_y):
				fov_recompute = True
			elif libtcod.map_is_in_fov(fov_map, old_mouse_x, old_mouse_y) and not libtcod.map_is_in_fov(fov_map, mouse_x, mouse_y):
				clean_map = True

			old_mouse_x = mouse_x
			old_mouse_y = mouse_y
			if left_click and targeting_item != None:
				target_x, target_y = left_click
				
				item_use_results = player.inventory.use(targeting_item, entities=entities, fov_map=fov_map,
															target_x=target_x, target_y=target_y)
				player_turn_results.extend(item_use_results)
				fov_recompute = True

			elif right_click:
				player_turn_results.append({'targeting_cancelled': True})
				fov_recompute = True

			elif left_click and targeting_item == None:
				target_x, target_y = left_click
				if not game_map.tiles[target_x][target_y].blocked:
					target = get_blocking_entities_at_location(entities, target_x, target_y)
				else:
					message_log.add_message(Message('You can\'t attack that.', libtcod.yellow))	

				if target and not target.invulnerable:
					attack_results = player.combat_class.attack(target)
					player_turn_results.extend(attack_results)
					fov_recompute = True
					game_state = GameStates.ENEMY_TURN



		if game_state == GameStates.SHOW_INVENTORY:
			if inspect_item:
				previous_game_state = game_state
				game_state = GameStates.CHOOSE_ITEM_TO_INSPECT
				message_log.add_message(Message('Choose an item to inspect.', libtcod.yellow))

		if game_state == GameStates.EQUIPMENT_SCREEN:
			if equipment_choice:
				previous_game_state = game_state
				game_state = GameStates.EQUIPMENT_DETAILS


		if exit:
			if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY, GameStates.CHARACTER_SCREEN, 
							  GameStates.INTERACT):
				if game_state == (GameStates.INTERACT):
					player_turn_results.append({'interacting_cancelled': True})
					game_state = previous_game_state
					npc = None
				else:
					game_state = previous_game_state

			elif game_state == GameStates.CHOOSE_ITEM_TO_INSPECT:
				game_state = GameStates.SHOW_INVENTORY
				previous_game_state = GameStates.PLAYERS_TURN
				message_log.add_message(Message('Item inspection cancelled.', libtcod.yellow))

			elif game_state == GameStates.INSPECT_ITEM:
				game_state = previous_game_state

			elif game_state == GameStates.EQUIPMENT_SCREEN:
				game_state = GameStates.PLAYERS_TURN

			elif game_state == GameStates.EQUIPMENT_DETAILS:
				game_state = previous_game_state
				equipment_choice = False

			elif game_state == GameStates.TARGETING:
				player_turn_results.append({'targeting_cancelled': True})
				game_state = previous_game_state
				fov_recompute = True

			else:
				libtcod.console_clear(0)
				save_game(player, entities, game_map, message_log, game_state, floor_index, original_entity_index, entity_index, fov_index)

				return True

		if fullscreen:
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

		for player_turn_result in player_turn_results:
			message =               player_turn_result.get('message')
			dead_entity =           player_turn_result.get('dead')
			item_added =            player_turn_result.get('item_added')
			item_consumed =         player_turn_result.get('consumed')
			item_dropped =          player_turn_result.get('item_dropped')
			equip =                 player_turn_result.get('equip')
			targeting =             player_turn_result.get('targeting')
			targeting_cancelled =   player_turn_result.get('targeting_cancelled')
			xp =                    player_turn_result.get('xp')
			interacting_cancelled = player_turn_result.get('interacting_cancelled')

			if message:
				message_log.add_message(message)

			if dead_entity:
				if dead_entity == player:
					message, game_state = kill_player(dead_entity)
				else:
					dead_entity.alive = False
					message = kill_monster(dead_entity)

				message_log.add_message(message)

			if item_added:
				entities.remove(item_added)
				game_state = GameStates.ENEMY_TURN

			if item_consumed:
				game_state = GameStates.ENEMY_TURN

			if equip:
				equip_results = player.equipment.toggle_equip(equip)

				for equip_result in equip_results:
					equipped = equip_result.get('equipped')
					unequipped = equip_result.get('unequipped')

					if equipped:
						message_log.add_message(Message('You equipped the {0}.'.format(equipped.name)))

					if unequipped:
						message_log.add_message(Message('You unequipped the {0}.'.format(unequipped.name)))

				game_state = GameStates.ENEMY_TURN

			if targeting:
				previous_game_state = GameStates.PLAYERS_TURN
				game_state = GameStates.TARGETING

				targeting_item = targeting

				message_log.add_message(targeting_item.item.targeting_message)


			if targeting_cancelled:
				game_state = previous_game_state
				message_log.add_message(Message('Targeting cancelled.'))

			if interacting_cancelled:
				game_state = previous_game_state
				message_log.add_message(Message('You stop looking around.'))

			if xp:
				leveled_up = player.level.add_xp(xp)
				message_log.add_message(Message('You gain {0} experience points.'.format(xp), libtcod.lighter_yellow))

				if leveled_up:
					message_log.add_message(Message(
						'Your skills grow more honed. You reach level {0}'.format(
							player.level.current_level) + "!", libtcod.yellow))
					previous_game_state = game_state
					game_state = GameStates.LEVEL_UP

			if item_dropped:
				entities.append(item_dropped)
				game_state = GameStates.ENEMY_TURN

		if game_state == GameStates.ENEMY_TURN:
				for entity in entities:
					if entity.ai:
						if wait:
							enemy_turn_results = entity.ai.approach_player_on_wait(player, fov_map, game_map, entities)
						else:
							enemy_turn_results = entity.ai.take_turn(player, fov_map, game_map, entities)

							for enemy_turn_result in enemy_turn_results:
								message = enemy_turn_result.get('message')
								dead_entity = enemy_turn_result.get('dead')

								if message:
									message_log.add_message(message)

								if dead_entity:
									if dead_entity == player:
										message, game_state = kill_player(dead_entity)
									else:
										message = kill_monster(dead_entity)

									message_log.add_message(message)

									if game_state == GameStates.PLAYER_DEAD:
										break

						if game_state == GameStates.PLAYER_DEAD:
							break
				else:
					game_state = GameStates.PLAYERS_TURN

			#animation_time -= 1


def main():
	constants = get_constants()
	#mixer.init(frequency=44100, size=16, channels=2,buffer=4096)
	#mixer.music.load('A Memory Lost.ogg')
	#mixer.music.play(loops=0, start=0.0)
	#mixer.music.set_volume(0.01)

	libtcod.console_set_custom_font('terminal16x16_gs_ro.png', libtcod.FONT_LAYOUT_ASCII_INROW, 16, 18)


	libtcod.console_init_root(constants['screen_width'], constants['screen_height'], constants['window_title'], False, libtcod.RENDERER_OPENGL)

	con = libtcod.console_new(constants['screen_width'], constants['screen_height'])
	message_panel = libtcod.console_new(constants['message_panel_width'], constants['panel_height'])
	char_info_panel = libtcod.console_new(constants['char_info_panel_width'], constants['char_info_panel_height'])
	area_info_panel = libtcod.console_new(constants['area_info_panel_width'], constants['area_info_panel_height'])
	under_mouse_panel = libtcod.console_new(constants['under_mouse_panel_width'], constants['under_mouse_panel_height'])

	#load_customfont()


	player = None
	entities = []
	game_map = None
	message_log = None
	game_state = None

	show_main_menu = True
	show_load_error_message = False
	show_controls_menu = False


	main_menu_background_image = libtcod.image_load('menu_background.png')

	key = libtcod.Key()
	mouse = libtcod.Mouse()

	while not libtcod.console_is_window_closed():
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

		if show_main_menu:
			main_menu(con, main_menu_background_image, constants['screen_width'],
						constants['screen_height'])

			if show_load_error_message:
				message_box(con, 'No saved games to load', libtcod.darker_blue, 23, constants['screen_width'], constants['screen_height'])

			libtcod.console_flush()

			action = handle_main_menu(key)

			new_game = action.get('new_game')
			load_saved_game = action.get('load_game')
			controls = action.get('controls')
			exit_game = action.get('exit')

			if show_load_error_message and (new_game or load_saved_game or exit_game):
				show_load_error_message = False

			elif new_game:
				player, entities, game_map, message_log, game_state = get_new_game_variables(constants)

				if player != None:
					fov_map = initialize_fov(game_map)
					floor_index = []
					entity_index = []
					original_entity_index = entity_index
					fov_index = []
					floor_index.append(game_map.tiles)
					entity_index.append(entities)
					original_entity_index.append(entities)
					fov_index.append(fov_map)
					game_state = GameStates.PLAYERS_TURN
					show_main_menu = False

			elif load_saved_game:
				try:
					player, entities, game_map, message_log, game_state, floor_index, original_entity_index, \
					entity_index, fov_index = load_game()
					show_main_menu = False
				except FileNotFoundError:
					show_load_error_message = True

			elif controls and show_controls_menu == False:
				show_controls_menu = True
				show_main_menu = False

			elif exit_game:	
				break

		elif show_controls_menu:
			libtcod.console_clear(0)
			controls_menu(con, '', 30, constants['screen_width'], constants['screen_height'])
			action = handle_controls_menu(key)
			libtcod.console_flush()
			back_to_main_menu = action.get('exit')

			if back_to_main_menu:
				show_controls_menu = False
				show_main_menu = True
				libtcod.console_clear(0)


		elif show_main_menu == False and show_controls_menu == False:
			libtcod.console_clear(con)
			play_game(player, entities, game_map, message_log, game_state, con, message_panel,
					 char_info_panel, area_info_panel, under_mouse_panel, constants, floor_index, 
					 original_entity_index, entity_index, fov_index)

			show_main_menu = True

if __name__ == '__main__':
	main()