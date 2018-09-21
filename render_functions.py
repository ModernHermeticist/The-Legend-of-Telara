import libtcodpy as libtcod

from enum import Enum

from game_states import GameStates

from interfaces.menus import inventory_menu, level_up_menu, character_screen, controls_menu, dialogue_screen, inspect_item_menu

class RenderOrder(Enum):
	STAIRS = 1
	CORPSE = 2
	ITEM = 3
	ACTOR = 4

def render_all(con, message_panel, char_info_panel, area_info_panel, under_mouse_panel, entities, 
				player, game_map, fov_map, fov_recompute, message_log,
				screen_width, screen_height, bar_width, panel_height, panel_y, mouse, colors, game_state, npc, item):
	if fov_recompute:
		# Draw all the tile in the game map
		for y in range(game_map.height):
			for x in range(game_map.width):
				visible = libtcod.map_is_in_fov(fov_map, x, y)
				wall = game_map.tiles[x][y].block_sight

				if visible:
					if wall:
						libtcod.console_set_char_background(con, x, y, colors.get('light_wall'), libtcod.BKGND_SET)
					else:
						libtcod.console_set_char_background(con, x, y, colors.get('light_ground'), libtcod.BKGND_SET)

					game_map.tiles[x][y].explored = True

				elif game_map.tiles[x][y].explored:
					if wall:
						libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)

					else:
						libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)

	entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)

	# Draw all entities in the list
	for entity in entities_in_render_order:
		draw_entity(con, entity, fov_map, game_map)

	libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

	libtcod.console_set_default_background(message_panel, libtcod.darkest_grey)
	libtcod.console_set_default_background(char_info_panel, libtcod.black)
	libtcod.console_set_default_background(area_info_panel, libtcod.black)
	libtcod.console_set_default_background(under_mouse_panel, libtcod.black)
	libtcod.console_clear(under_mouse_panel)
	libtcod.console_clear(char_info_panel)
	libtcod.console_clear(char_info_panel)
	libtcod.console_clear(message_panel)

	# Print the game message, one line at a time
	y = 1
	for message in message_log.messages:
		libtcod.console_set_default_foreground(message_panel, message.color)
		libtcod.console_print_ex(message_panel, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, message.text)
		y += 1

	render_bar(char_info_panel, 1, 0, bar_width, "HP", player.combat_class.hp, 
				player.combat_class.max_hp, libtcod.light_red, libtcod.darker_red, libtcod.black)
	render_bar(char_info_panel, 1, 1, bar_width, "MP", player.combat_class.mp, 
				player.combat_class.max_mp, libtcod.light_blue, libtcod.darker_blue, libtcod.black)
	render_bar(char_info_panel, 1, 2, bar_width, "XP", player.level.current_xp, 
				player.level.experience_to_next_level, libtcod.gold, libtcod.brass, libtcod.black)
	libtcod.console_set_default_foreground(char_info_panel, libtcod.white)
	libtcod.console_print_ex(char_info_panel, 1, 3, libtcod.BKGND_NONE, libtcod.LEFT,
								'Player Level: {0}'.format(player.level.current_level))
	libtcod.console_print_ex(area_info_panel, 1, 0, libtcod.BKGND_NONE, libtcod.LEFT,
								'Dungeon Level: {0}'.format(game_map.dungeon_level))

	libtcod.console_set_default_foreground(under_mouse_panel, libtcod.white)
	libtcod.console_print_ex(under_mouse_panel, 1, 0, libtcod.BKGND_NONE, libtcod.LEFT,
							get_names_under_mouse(mouse, entities, fov_map))

	if game_state in (GameStates.SHOW_INVENTORY, GameStates.CHOOSE_ITEM_TO_INSPECT):
		inventory_menu(con, "Press the key next to an item to use it, or Esc to cancel.\n",
						player, 50, screen_width, screen_height)

	elif game_state in (GameStates.DROP_INVENTORY, GameStates.CHOOSE_ITEM_TO_INSPECT):
		inventory_menu(con, "Press the key next to an item to drop it, or Esc to cancel.\n",
						player, 50, screen_width, screen_height)

	elif game_state == GameStates.INSPECT_ITEM:
		inspect_item_menu(con, '', item, 30, 30, screen_width, screen_height)

	elif game_state == GameStates.LEVEL_UP:
		level_up_menu(con, 'Level up! Choose a stat to raise:', player, 40, screen_width, screen_height)

	elif game_state == GameStates.CHARACTER_SCREEN:
		character_screen(player, 30, 10, screen_width, screen_height)

	elif game_state == GameStates.INTERACT and npc:
		dialogue_screen(player, npc, 50, 30, screen_width, screen_height )

	libtcod.console_blit(message_panel, 0, 0, screen_width, panel_height, 0, 30, panel_y - 1)
	libtcod.console_blit(char_info_panel, 0, 0, screen_width, panel_height, 0, 0, panel_y)
	libtcod.console_blit(area_info_panel, 0, 0, screen_width, panel_height, 0, 0, panel_y + 4)
	libtcod.console_blit(under_mouse_panel, 0, 0, screen_width, panel_height, 0, 0, panel_y - 1)


def clear_all(con, entities):
	for entity in entities:
		clear_entity(con, entity)


def draw_entity(con, entity, fov_map, game_map):
	if libtcod.map_is_in_fov(fov_map, entity.x, entity.y) or (entity.stairs and game_map.tiles[entity.x][entity.y].explored):
		libtcod.console_set_default_foreground(con, entity.color)
		libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity):
	# Erase the character that represents this object
	libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)


def get_names_under_mouse(mouse, entities, fov_map):
	(x, y) = (mouse.cx, mouse.cy)

	names = [entity.name for entity in entities
			if entity.x == x and entity.y == y and libtcod.map_is_in_fov(fov_map, entity.x, entity.y)]

	names = ', '.join(names)

	return names.capitalize()


def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color, text_color=libtcod.white):
	bar_width = int(float(value) / maximum * total_width)

	libtcod.console_set_default_background(panel, back_color)
	libtcod.console_rect(panel, x, y, total_width, 1, False, libtcod.BKGND_SCREEN)

	libtcod.console_set_default_background(panel, bar_color)
	if bar_width > 0:
		libtcod.console_rect(panel, x, y, bar_width, 1, False, libtcod.BKGND_SCREEN)

	libtcod.console_set_default_foreground(panel, text_color)
	libtcod.console_print_ex(panel, int(x + total_width / 2), y, libtcod.BKGND_NONE,
							libtcod.CENTER, "{0}: {1}/{2}".format(name, value, maximum))