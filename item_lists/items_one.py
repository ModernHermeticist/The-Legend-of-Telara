import libtcodpy as libtcod

from random_utils import from_dungeon_level

from render_functions import RenderOrder

from game_messages import Message

from components.equipment import EquipmentSlots
from components.equippable import Equippable
from components.item import Item
from entity import Entity
from components.item_functions import cast_confuse, cast_fireball, cast_lightning, heal


def get_early_items(dungeon_level):

	item_chances = {
		'healing_potion':            from_dungeon_level([[55,1]], dungeon_level),


		'broken_iron_sword':         from_dungeon_level([[15,2]], dungeon_level),


		'flimsy_wooden_bow':         from_dungeon_level([[15,2]], dungeon_level),


		'cracked_wooden_board':      from_dungeon_level([[15,2]], dungeon_level),


		'dirty_leather_tunic':       from_dungeon_level([[15,1]], dungeon_level),


		'dirty_leather_pants':       from_dungeon_level([[15,1]], dungeon_level),


		'lightning_scroll':          from_dungeon_level([[15,3]], dungeon_level), 
		'fireball_scroll':           from_dungeon_level([[15,3]], dungeon_level), 
		'confusion_scroll':          from_dungeon_level([[10,2]], dungeon_level)
		}

	return item_chances


def choose_early_item(item_choice, x, y):
	if item_choice == 'healing_potion':
		item_description = ("Clearly brewed by an individual with little alchemical training,"
							"this simple healing potion will mildly soothe the pain of battle.")
		item_component = Item(description=item_description, use_function=heal, heal_amount=40)
		item = Entity(x, y, '!', libtcod.violet, 'Healing Potion', render_order=RenderOrder.ITEM,
					  item=item_component)




	elif item_choice == 'broken_iron_sword':
		equippable_component = Equippable(EquipmentSlots.MAIN_HAND, min_damage_bonus=1, max_damage_bonus=3)
		item = Entity(x, y, '/', libtcod.brass, 'Broken Iron Sword', render_order=RenderOrder.ITEM,
					  equippable=equippable_component)
		item.item.description = ("Long ago a knight stood atop the battlements of lost Fort Grey Mount.\n"
								 "He looked wistfully to the fields in the distance.\n\n"
								 "\"Such a waste..\" He thought, as he threw his sword to the ground.")





	elif item_choice == 'flimsy_wooden_bow':
		equippable_component = Equippable(EquipmentSlots.MAIN_HAND, ranged=True, min_damage_bonus=1, max_damage_bonus=2)
		item = Entity(x, y, 'D', libtcod.sepia, 'Flimsy Wooden Bow', render_order=RenderOrder.ITEM,
					  equippable=equippable_component)
		item.item.targeting_range = 9
		item.item.area_of_effect = 1
		item.item.description = ("Legends tell of a woman who made wielding a bow an art form."
								"You probably wont get much accomplished with this thing though.")




	elif item_choice == 'cracked_wooden_board':
		equippable_component = Equippable(EquipmentSlots.OFF_HAND, armor_bonus=1)
		item = Entity(x, y, '[', libtcod.darker_orange, 'Cracked Wooden Board', render_order=RenderOrder.ITEM,
					  equippable=equippable_component)
		item.item.description = ("In moments of crises even this might be useful.")





	elif item_choice == 'dirty_leather_tunic':
		equippable_component = Equippable(EquipmentSlots.CHEST, armor_bonus=1)
		item = Entity(x, y, 'T', libtcod.darker_sepia, 'Dirty Leather Tunic', render_order=RenderOrder.ITEM,
					  equippable=equippable_component)
		item.item.description = ("It smells something awful and provides next to no protection.")






	elif item_choice == 'dirty_leather_pants':
		equippable_component = Equippable(EquipmentSlots.LEGS, armor_bonus=1)
		item = Entity(x, y, 'M', libtcod.darker_sepia, 'Dirty Leather Pants', render_order=RenderOrder.ITEM,
					  equippable=equippable_component)
		item.item.description = ("It smells something awful and provides next to no protection.")









	elif item_choice == 'fireball_scroll':
		item_description = ("A simple scroll with otherwise unintelligible glyphs scrawled across it.\n"
								"You are capable of interpreting the word \"Fire\", though what exactly that\n"
								"means remains to be seen.")
		item_component = Item(description=item_description, use_function=cast_fireball, targeting=True, targeting_message=Message(
			'Left-click a target tile for the fireball,\nor right-click to cancel.', libtcod.light_cyan),
							  targeting_range=9, area_of_effect=3, damage=25)
		item = Entity(x, y, '#', libtcod.red, 'Fireball Scroll', render_order=RenderOrder.ITEM,
					  item=item_component)

	elif item_choice == 'confusion_scroll':
		item_description = ("The longer you attempt to understand the words on this scroll the more\n"
								"you feel like you've been tricked.")
		item_component = Item(description=item_description, use_function=cast_confuse, targeting=True, targeting_message=Message(
			'Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan),
							 targeting_range=9, area_of_effect=1)
		item = Entity(x, y, '#', libtcod.light_pink, 'Confusion Scroll', render_order=RenderOrder.ITEM,
					  item=item_component)

	elif item_choice == 'lightning_scroll':
		item_description = ("A simple scroll with otherwise unintelligible glyphs scrawled across it.\n"
								"You feel a jolt of energy when you hold it.\n"
								"The word \"Lightning\" is scarred into the top of the paper.")
		item_component = Item(description=item_description, use_function=cast_lightning, damage=40, maximum_range=5)
		item = Entity(x, y, '#', libtcod.yellow, 'Lightning Scroll', render_order=RenderOrder.ITEM,
					  item=item_component)

	return item