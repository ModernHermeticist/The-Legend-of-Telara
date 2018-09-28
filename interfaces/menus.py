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

	menu(con, header, libtcod.darkest_blue, options, inventory_width, screen_width, screen_height)

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

	menu(con, header, libtcod.darkest_blue, options, menu_width, screen_width, screen_height)

def inspect_item_menu(con, header, item, menu_width, menu_height, screen_width, screen_height):

	y = 0
	window = libtcod.console_new(menu_width, menu_height)

	libtcod.console_set_default_background(window, libtcod.darkest_blue)
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

	libtcod.console_set_default_background(window, libtcod.darkest_blue)
	libtcod.console_set_default_foreground(window, libtcod.white)
	libtcod.console_clear(window)

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Character Information')

	y += 2

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
									libtcod.LEFT, 'HP: {0}/{1}'.format(player.combat_class.hp, player.combat_class.max_hp))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, character_screen_width, character_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Damage: {0}-{1}'.format(player.combat_class.min_damage, player.combat_class.max_damage))

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


def equipment_screen(player, equipment_screen_width, equipment_screen_height, screen_width, screen_height):
	y = 0
	window = libtcod.console_new(equipment_screen_width, equipment_screen_height)

	libtcod.console_set_default_background(window, libtcod.darkest_blue)
	libtcod.console_set_default_foreground(window, libtcod.white)
	libtcod.console_clear(window)

	libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Character Equipment')

	y += 2

	# Check for main hand item, if no item print "Empty", else print the item
	if player.equipment.main_hand:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(M)ain Hand: {0}'.format(player.equipment.main_hand.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(M)ain Hand: Empty')

	y += 1

	# Check for off hand item, if no item print "Empty", else print the item
	if player.equipment.off_hand:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(O)ff Hand:  {0}'.format(player.equipment.off_hand.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(O)ff Hand:  Empty')

	y += 2

	# Check for head item, if no item print "Empty", else print the item
	if player.equipment.head:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(H)ead:      {0}'.format(player.equipment.head.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(H)ead:      Empty')

	y += 1

	# Check for shoulders item, if no item print "Empty", else print the item
	if player.equipment.shoulders:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(S)houlders: {0}'.format(player.equipment.shoulders.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(S)houlders: Empty')

	y += 1

	# Check for arms item, if no item print "Empty", else print the item
	if player.equipment.arms:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(A)rms:      {0}'.format(player.equipment.arms.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(A)rms:      Empty')

	y += 1

	# Check for wrists item, if no item print "Empty", else print the item
	if player.equipment.wrists:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(W)rists:    {0}'.format(player.equipment.wrists.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(W)rists:    Empty')

	y += 1

	# Check for hands item, if no item print "Empty", else print the item
	if player.equipment.hands:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, 'Ha(n)ds:     {0}'.format(player.equipment.hands.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, 'Ha(n)ds:     Empty')

	y += 1

	# Check for chest item, if no item print "Empty", else print the item
	if player.equipment.chest:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(C)hest:     {0}'.format(player.equipment.chest.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(C)hest:     Empty')

	y += 1

	# Check for belt item, if no item print "Empty", else print the item
	if player.equipment.belt:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(B)elt:      {0}'.format(player.equipment.belt.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(B)elt:      Empty')

	y += 1

	# Check for legs item, if no item print "Empty", else print the item
	if player.equipment.legs:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(L)egs:      {0}'.format(player.equipment.legs.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(L)egs:      Empty')

	y += 1

	# Check for feet item, if no item print "Empty", else print the item
	if player.equipment.feet:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(F)eet:      {0}'.format(player.equipment.feet.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, '(F)eet:      Empty')

	y += 1

	# Check for back item, if no item print "Empty", else print the item
	if player.equipment.back:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, 'Bac(k):      {0}'.format(player.equipment.back.name))
	else:
		libtcod.console_print_rect_ex(window, 0, y, equipment_screen_width, equipment_screen_height, libtcod.BKGND_NONE,
										libtcod.LEFT, 'Bac(k):      Empty')


	x = screen_width // 2 - equipment_screen_width // 2
	y = screen_height // 2 - equipment_screen_height // 2
	libtcod.console_blit(window, 0, 0, equipment_screen_width, equipment_screen_height, 0, x, y, 1.0, 1.0)


def equipment_details_screen(player, selection, equipment_details_screen_width, equipment_details_screen_height, \
							 screen_width, screen_height):


	if selection == 'main_hand':
		if player.equipment.main_hand != None:
			item_slot = 'Main Hand'
			if player.equipment.main_hand.name != None:
				item_name         = player.equipment.main_hand.name
			else:
				item_name         = ' '
			if player.equipment.main_hand.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.main_hand.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.main_hand.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.main_hand.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.main_hand.equippable.armor_bonus != None:
				item_armor        = player.equipment.main_hand.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.main_hand.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.main_hand.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.main_hand.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.main_hand.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.main_hand.equippable.strength_bonus != None:
				item_strength     = player.equipment.main_hand.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.main_hand.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.main_hand.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.main_hand.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.main_hand.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.main_hand.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.main_hand.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.main_hand.item.description != None:
				item_description  = player.equipment.main_hand.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Main Hand'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'off_hand':
		if player.equipment.off_hand != None:
			item_slot = 'Off Hand'
			if player.equipment.off_hand.name != None:
				item_name         = player.equipment.off_hand.name
			else:
				item_name         = ' '
			if player.equipment.off_hand.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.off_hand.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.off_hand.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.off_hand.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.off_hand.equippable.armor_bonus != None:
				item_armor        = player.equipment.off_hand.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.off_hand.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.off_hand.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.off_hand.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.off_hand.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.off_hand.equippable.strength_bonus != None:
				item_strength     = player.equipment.off_hand.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.off_hand.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.off_hand.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.off_hand.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.off_hand.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.off_hand.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.off_hand.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.off_hand.item.description != None:
				item_description  = player.equipment.off_hand.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Off Hand'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'head':
		if player.equipment.head != None:
			item_slot = 'Head'
			if player.equipment.head.name != None:
				item_name         = player.equipment.head.name
			else:
				item_name         = ' '
			if player.equipment.head.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.head.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.head.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.head.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.head.equippable.armor_bonus != None:
				item_armor        = player.equipment.head.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.head.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.head.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.head.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.head.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.head.equippable.strength_bonus != None:
				item_strength     = player.equipment.head.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.head.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.head.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.head.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.head.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.head.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.head.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.head.item.description != None:
				item_description  = player.equipment.head.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Head'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'shoulders':
		if player.equipment.shoulders != None:
			item_slot = 'Shoulders'
			if player.equipment.shoulders.name != None:
				item_name         = player.equipment.shoulders.name
			else:
				item_name         = ' '
			if player.equipment.shoulders.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.shoulders.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.shoulders.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.shoulders.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.shoulders.equippable.armor_bonus != None:
				item_armor        = player.equipment.shoulders.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.shoulders.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.shoulders.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.shoulders.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.shoulders.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.shoulders.equippable.strength_bonus != None:
				item_strength     = player.equipment.shoulders.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.shoulders.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.shoulders.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.shoulders.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.shoulders.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.shoulders.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.shoulders.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.shoulders.item.description != None:
				item_description  = player.equipment.shoulders.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Head'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'arms':
		if player.equipment.arms != None:
			item_slot = 'Arms'
			if player.equipment.arms.name != None:
				item_name         = player.equipment.arms.name
			else:
				item_name         = ' '
			if player.equipment.arms.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.arms.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.arms.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.arms.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.arms.equippable.armor_bonus != None:
				item_armor        = player.equipment.arms.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.arms.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.arms.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.arms.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.arms.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.arms.equippable.strength_bonus != None:
				item_strength     = player.equipment.arms.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.arms.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.arms.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.arms.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.arms.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.arms.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.arms.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.arms.item.description != None:
				item_description  = player.equipment.arms.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Arms'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'wrists':
		if player.equipment.wrists != None:
			item_slot = 'Wrists'
			if player.equipment.wrists.name != None:
				item_name         = player.equipment.wrists.name
			else:
				item_name         = ' '
			if player.equipment.wrists.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.wrists.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.wrists.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.wrists.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.wrists.equippable.armor_bonus != None:
				item_armor        = player.equipment.wrists.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.wrists.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.wrists.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.wrists.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.wrists.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.wrists.equippable.strength_bonus != None:
				item_strength     = player.equipment.wrists.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.wrists.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.wrists.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.wrists.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.wrists.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.wrists.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.wrists.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.wrists.item.description != None:
				item_description  = player.equipment.wrists.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Wrists'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'hands':
		if player.equipment.hands != None:
			item_slot = 'Hands'
			if player.equipment.hands.name != None:
				item_name         = player.equipment.hands.name
			else:
				item_name         = ' '
			if player.equipment.hands.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.hands.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.hands.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.hands.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.hands.equippable.armor_bonus != None:
				item_armor        = player.equipment.hands.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.hands.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.hands.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.hands.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.hands.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.hands.equippable.strength_bonus != None:
				item_strength     = player.equipment.hands.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.hands.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.hands.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.hands.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.hands.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.hands.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.hands.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.hands.item.description != None:
				item_description  = player.equipment.hands.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Hands'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'chest':
		if player.equipment.chest != None:
			item_slot = 'Chest'
			if player.equipment.chest.name != None:
				item_name         = player.equipment.chest.name
			else:
				item_name         = ' '
			if player.equipment.chest.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.chest.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.chest.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.chest.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.chest.equippable.armor_bonus != None:
				item_armor        = player.equipment.chest.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.chest.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.chest.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.chest.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.chest.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.chest.equippable.strength_bonus != None:
				item_strength     = player.equipment.chest.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.chest.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.chest.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.chest.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.chest.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.chest.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.chest.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.chest.item.description != None:
				item_description  = player.equipment.chest.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Chest'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'belt':
		if player.equipment.belt != None:
			item_slot = 'Belt'
			if player.equipment.belt.name != None:
				item_name         = player.equipment.belt.name
			else:
				item_name         = ' '
			if player.equipment.belt.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.belt.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.belt.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.belt.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.belt.equippable.armor_bonus != None:
				item_armor        = player.equipment.belt.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.belt.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.belt.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.belt.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.belt.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.belt.equippable.strength_bonus != None:
				item_strength     = player.equipment.belt.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.belt.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.belt.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.belt.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.belt.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.belt.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.belt.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.belt.item.description != None:
				item_description  = player.equipment.belt.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Belt'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'legs':
		if player.equipment.legs != None:
			item_slot = 'Legs'
			if player.equipment.legs.name != None:
				item_name         = player.equipment.legs.name
			else:
				item_name         = ' '
			if player.equipment.legs.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.legs.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.legs.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.legs.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.legs.equippable.armor_bonus != None:
				item_armor        = player.equipment.legs.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.legs.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.legs.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.legs.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.legs.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.legs.equippable.strength_bonus != None:
				item_strength     = player.equipment.legs.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.legs.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.legs.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.legs.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.legs.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.legs.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.legs.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.legs.item.description != None:
				item_description  = player.equipment.legs.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Legs'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'feet':
		if player.equipment.head != None:
			item_slot = 'Feet'
			if player.equipment.feet.name != None:
				item_name         = player.equipment.feet.name
			else:
				item_name         = ' '
			if player.equipment.feet.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.feet.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.feet.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.feet.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.feet.equippable.armor_bonus != None:
				item_armor        = player.equipment.feet.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.feet.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.feet.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.feet.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.feet.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.feet.equippable.strength_bonus != None:
				item_strength     = player.equipment.feet.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.feet.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.feet.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.feet.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.feet.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.feet.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.feet.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.feet.item.description != None:
				item_description  = player.equipment.feet.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Feet'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'

	elif selection == 'back':
		if player.equipment.back != None:
			item_slot = 'Back'
			if player.equipment.back.name != None:
				item_name         = player.equipment.back.name
			else:
				item_name         = ' '
			if player.equipment.back.equippable.min_damage_bonus != None:
				item_damage_min   = player.equipment.back.equippable.min_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.back.equippable.max_damage_bonus != None:
				item_damage_max   = player.equipment.back.equippable.max_damage_bonus
			else:
				item_damage_min   = '0'
			if player.equipment.back.equippable.armor_bonus != None:
				item_armor        = player.equipment.back.equippable.armor_bonus
			else:
				item_armor        = '0'
			if player.equipment.back.equippable.max_hp_bonus != None:
				item_hp           = player.equipment.back.equippable.max_hp_bonus
			else:
				item_hp           = '0'
			if player.equipment.back.equippable.max_mp_bonus != None:
				item_mp           = player.equipment.back.equippable.max_mp_bonus
			else:
				item_mp           = '0'
			if player.equipment.back.equippable.strength_bonus != None:
				item_strength     = player.equipment.back.equippable.strength_bonus
			else:
				item_strength     = '0'
			if player.equipment.back.equippable.dexterity_bonus != None:
				item_dexterity    = player.equipment.back.equippable.dexterity_bonus
			else:
				item_dexterity    = '0'
			if player.equipment.back.equippable.stamina_bonus != None:
				item_stamina      = player.equipment.back.equippable.stamina_bonus
			else:
				item_stamina      = '0'
			if player.equipment.back.equippable.intelligence_bonus != None:
				item_intelligence = player.equipment.back.equippable.intelligence_bonus
			else:
				item_intelligence = '0'
			if player.equipment.back.item.description != None:
				item_description  = player.equipment.back.item.description
			else:
				item_description  = ' '
		else:
			item_slot         = 'Back'
			item_description  = ' '
			item_name         = ' '
			item_damage_min   = '0'
			item_damage_max   = '0'
			item_armor        = '0'
			item_hp           = '0'
			item_mp           = '0'
			item_strength     = '0'
			item_dexterity    = '0'
			item_stamina      = '0'
			item_intelligence = '0'


	y = 0
	window = libtcod.console_new(equipment_details_screen_width, equipment_details_screen_height)

	libtcod.console_set_default_background(window, libtcod.darkest_blue)
	libtcod.console_set_default_foreground(window, libtcod.white)
	libtcod.console_clear(window)


	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, item_name)

	y += 2

	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, item_slot)

	y += 2


	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Damage: {0}-{1}'.format(item_damage_min, item_damage_max))

	y += 2

	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Armor: {0}'.format(item_armor))

	y += 2

	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'HP: {0}'.format(item_hp))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'MP: {0}'.format(item_mp))

	y += 2

	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Strength:     {0}'.format(item_strength))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Dexterity:    {0}'.format(item_dexterity))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Stamina:      {0}'.format(item_stamina))

	y += 1

	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, 'Intelligence: {0}'.format(item_intelligence))

	y += 2

	libtcod.console_print_rect_ex(window, 0, y, equipment_details_screen_width, equipment_details_screen_height, libtcod.BKGND_NONE,
									libtcod.LEFT, '{0}'.format(item_description))

	x = screen_width // 2 - equipment_details_screen_width // 2
	y = screen_height // 2 - equipment_details_screen_height // 2
	libtcod.console_blit(window, 0, 0, equipment_details_screen_width, equipment_details_screen_height, 0, x, y, 1.0, 1.0)



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
