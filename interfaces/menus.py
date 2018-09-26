import libtcodpy as libtcod

def menu(con, header, background_color, options, width, screen_width, screen_height, ordered=True):
	if len(options) > 26: raise ValueError("Cannot have a menu with more than 26 options.")

	# Calculate total height for the header (after auto-wrap) and one line per option
	header_height = libtcod.console_get_height_rect(con, 0, 0, width, screen_height, header)
	height = len(options) + header_height

	# Create an off-screen console that represents the menu's window
	window = libtcod.console_new(width, height)

	# Print the header, with auto-wrap
	libtcod.console_set_default_background(window, background_color)
	libtcod.console_set_default_foreground(window, libtcod.white)
	libtcod.console_clear(window)
	libtcod.console_print_rect_ex(window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header)

	if ordered:
		# Print all the options
		y = header_height
		letter_index = ord('a')
		for option_text in options:
			text = "(" + chr(letter_index) + ")" + option_text
			libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
			y += 1
			letter_index += 1

	else:
		# Print all the options
		y = header_height
		for option_text in options:
			libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, option_text)
			y += 1

	# Blit the contents of "window" to the root console
	x = int(screen_width / 2 - width / 2)
	y = int(screen_height / 2 - height / 2)
	libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.9)



def inventory_menu(con, header, player, inventory_width, screen_width, screen_height):
	# Show a menu with each item of the inventory as an option
	if len(player.inventory.items) == 0:
		options = ["Inventory is empty."]
	else:
		options = []

		for item in player.inventory.items:
			if player.equipment.main_hand == item:
				options.append('{0} (in main hand)'.format(item.name))
			elif player.equipment.off_hand == item:
				options.append('{0} (in off hand)'.format(item.name))
			elif player.equipment.chest == item:
				options.append('{0} (on chest)'.format(item.name))
			elif player.equipment.legs == item:
				options.append('{0} (on legs)'.format(item.name))
			elif player.equipment.feet == item:
				options.append('{0} (on feet)'.format(item.name))
			elif player.equipment.arms == item:
				options.append('{0} (on arms)'.format(item.name))
			elif player.equipment.hands == item:
				options.append('{0} (on hands)'.format(item.name))
			elif player.equipment.shoulders == item:
				options.append('{0} (on shoulders)'.format(item.name))
			elif player.equipment.head == item:
				options.append('{0} (on head)'.format(item.name))
			elif player.equipment.wrists == item:
				options.append('{0} (on wrists)'.format(item.name))
			elif player.equipment.back == item:
				options.append('{0} (on back)'.format(item.name))
			else:
				options.append(item.name)

	menu(con, header, libtcod.darker_blue, options, inventory_width, screen_width, screen_height)

def main_menu(con, background_image, screen_width, screen_height):
	#libtcod.image_blit_2x(background_image, 0, 0, 0)
	libtcod.console_set_default_foreground(0, libtcod.white)

	libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2) - 15, libtcod.BKGND_NONE, libtcod.CENTER,
							 'THERE IS A BUG WHERE ON SAVE AND LOAD THE PLAYER CHARACTER SHOWS UP AGAIN ON ANOTHER FLOOR')
	libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2) - 14, libtcod.BKGND_NONE, libtcod.CENTER,
							 'ALSO THE NEXT THING ON THE TODO LIST IS ADDING PURE RANGED ATTACKS (WEAPONS/CHARACTER SPELLS)')
	libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2) - 13, libtcod.BKGND_NONE, libtcod.CENTER,
							 'ADD BOWS!!!!')
	libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2) - 12, libtcod.BKGND_NONE, libtcod.CENTER,
							 'ADD SOME KIND OF FLOOR RESPAWN SYSTEM (THAT\'S MONSTERS AND ITEMS)')


	libtcod.console_set_default_foreground(0, libtcod.light_yellow)

	libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2) - 6, libtcod.BKGND_NONE, libtcod.CENTER,
							 'THE LEGEND OF TELARA')
	libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2) - 4, libtcod.BKGND_NONE, libtcod.CENTER,
							 'THIS GAME IS UNBALANCED, UNSTABLE, AND UNFORGIVING')
	libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height - 3), libtcod.BKGND_NONE, libtcod.CENTER,
							 'PRE-ALPHA VERSION 0.01')
	libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height - 2), libtcod.BKGND_NONE, libtcod.CENTER,
							 'By Jacob Queen, 2018')

	menu(con, '', libtcod.black, ['Play a new game', 'Continue last game', 'Controls', 'Quit'], 22, screen_width, screen_height)

def level_up_menu(con, header, player, menu_width, screen_width, screen_height):
	options = ['Strength     (+1 strength)',
			   'Dexterity    (+1 dexterity)',
			   'Stamina      (+1 stamina)',
			   'Intelligence (+1 intelligence']

	menu(con, header, libtcod.darker_grey, options, menu_width, screen_width, screen_height)

def inspect_item_menu(con, header, item, menu_width, menu_height, screen_width, screen_height):

	y = 0
	window = libtcod.console_new(menu_width, menu_height)

	libtcod.console_set_default_background(window, libtcod.darker_blue)
	libtcod.console_set_default_foreground(window, libtcod.white)
	libtcod.console_clear(window)

	libtcod.console_print_rect_ex(window, 0, y, menu_width, menu_height, libtcod.BKGND_NONE,
									libtcod.LEFT, '{0}'.format(item.name))

	y += 2

	libtcod.console_print_rect_ex(window, 0, y, menu_width, menu_height, libtcod.BKGND_NONE,
									libtcod.LEFT, '{0}'.format(item.item.description))

	x = screen_width // 2 - menu_width // 2
	y = screen_height // 2 - menu_height // 2
	libtcod.console_blit(window, 0, 0, menu_width, menu_height, 0, x, y, 1.0, 1.0)


def controls_menu(con, header, menu_width, screen_width, screen_height):
	options = ['MOVE NORTH:                 i',
			   'MOVE SOUTH:                 ,',
			   'MOVE WEST:                  j',
			   'MOVE EAST:                  l',
			   'MOVE NORTH-WEST:            u',
			   'MOVE NORTH-EAST:            o',
			   'MOVE SOUTH-WEST:            m',
			   'MOVE SOUTH-EAST:            .',
			   'PICK UP ITEM:               g',
			   'INVENTORY:                  c',
			   'CHARACTER SCREEN:           z',
			   'USE STAIRS:                 q',
			   'INSPECT:                space',
			   'STOP INSPECTING:          esc',
			   'CLOSE SCREEN:             esc',
			   'MAIN MENU:                esc',
			   'FULL SCREEN:        alt+enter',
			   '',
			   'Press ESC to return.']

	libtcod.console_set_default_foreground(0, libtcod.white)
	libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2) - 11, libtcod.BKGND_NONE, libtcod.CENTER,
							 'Controls')
	menu(con, header, libtcod.black, options, menu_width, screen_width, screen_height, False)

def character_screen(player, character_screen_width, character_screen_height, screen_width, screen_height):
	y = 0
	window = libtcod.console_new(character_screen_width, character_screen_height)

	libtcod.console_set_default_background(window, libtcod.darker_blue)
	libtcod.console_set_default_foreground(window, libtcod.white)
	libtcod.console_clear(window)

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Character Information')

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Name: {0}'.format(player.name))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Sex: {0}'.format(player.sex))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Race: {0}'.format(player.race.race_name))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Class: {0}'.format(player.combat_class.class_name))

	y += 2

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Level: {0}'.format(player.level.current_level))

	y += 1	

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Experience: {0}'.format(player.level.current_xp))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Experience to level: {0}'.format(player.level.experience_to_next_level))

	y += 2

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'HP/Max HP: {0}/{1}'.format(player.combat_class.hp, player.combat_class.max_hp))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Damage: {0} - {1}'.format(player.combat_class.min_damage, player.combat_class.max_damage))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Armor: {0}'.format(player.combat_class.armor))

	y += 2

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Strength: {0}'.format(player.combat_class.strength))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Dexterity: {0}'.format(player.combat_class.dexterity))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Stamina: {0}'.format(player.combat_class.stamina))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Intelligence: {0}'.format(player.combat_class.intelligence))
	


	x = screen_width // 2 - character_screen_width // 2
	y = screen_height // 2 - character_screen_height // 2
	libtcod.console_blit(window, 0, 0, character_screen_width, character_screen_height, 0, x, y, 1.0, 1.0)

def dialogue_screen(player, npc, dialogue_screen_width, dialogue_screen_height, screen_width, screen_height):
	# X = 50 Y = 30
	window = libtcod.console_new(dialogue_screen_width, dialogue_screen_height)
	libtcod.console_set_default_background(window, libtcod.darker_grey)
	libtcod.console_set_default_foreground(window, libtcod.white)
	libtcod.console_clear(window)

	libtcod.console_print_rect_ex(window, 0, 0, dialogue_screen_width, dialogue_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, '{0}'.format(npc.dialogue.dialogue))
	libtcod.console_print_rect_ex(window, 0, 29, dialogue_screen_width, dialogue_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Press ESC to close this window.')

	x = screen_width // 2 - dialogue_screen_width // 2
	y = screen_height // 2 - dialogue_screen_height // 2
	libtcod.console_blit(window, 0, 0, dialogue_screen_width, dialogue_screen_height, 0, x, y, 1.0, 1.0)

	

def message_box(con, header, background_color, width, screen_width, screen_height):
	menu(con, header, background_color, [], width, screen_width, screen_height)
