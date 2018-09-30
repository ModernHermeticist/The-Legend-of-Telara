import libtcodpy as libtcod
from random import randint

from components.stairs import Stairs
from components.dialogue import Dialogue
from components.bonfire import Bonfire

from entity import Entity

from components.equipment import EquipmentSlots
from components.equippable import Equippable
from components.item import Item
from components.item_functions import *

from render_functions import RenderOrder

from game_messages import Message


from map_objects.rectangle import Rect
from map_objects.tile import Tile


from random_utils import random_choice_from_dict, from_dungeon_level

from monster_lists.monsters_one import get_easy_monsters, choose_easy_monster

from item_lists.items_one import get_early_items, choose_early_item


class GameMap:
	def __init__(self, width, height, dungeon_level=1):
		self.width = width
		self.height = height
		self.tiles = self.initialize_tiles()

		self.stairs_down_x = None
		self.stairs_down_y = None

		self.stairs_up_x = None
		self.stairs_up_y = None

		self.room_list = []


		self.dungeon_level = dungeon_level

	def initialize_tiles(self):
		tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

		return tiles

	def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities):
		stairs_up          =  260
		stairs_down        =  261
		mysterious_old_man =  284
		generic_bow        =  277


		rooms = []
		num_rooms = 0

		center_of_last_room_x = None
		center_of_last_room_y = None

		for r in range(max_rooms):
			# random width and height
			w = randint(room_min_size, room_max_size)
			h = randint(room_min_size, room_max_size)
			# random position without going out of the boundaries of the map
			x = randint(0, map_width - w - 1)
			y = randint(0, map_height - h - 1)

			# "Rect" class makes rectangles easier to work with
			new_room = Rect(x, y, w, h)

			# run through the other rooms and see if they intersect with this one
			for other_room in rooms:
				if new_room.intersect(other_room):
					break
			else:
				# this means there are no intersections, so this room is valid

				# "paint" it to the map's tiles
				self.create_room(new_room)

				# center coordinates of new room, will be useful later
				(new_x, new_y) = new_room.center()

				center_of_last_room_x = new_x
				center_of_last_room_y = new_y

				if num_rooms == 0:
					# this is the first room, where the player starts at
					player.x = new_x
					player.y = new_y
				else:
					# all rooms after the first:
					# connect it to the previous room with a tunnel

					# center coordinates of previous room
					(prev_x, prev_y) = rooms[num_rooms - 1].center()

					# flip a coin (random number that is either 0 or 1)
					if randint(0, 1) == 1:
						# first move horizontally, then vertically
						self.create_h_tunnel(prev_x, new_x, prev_y)
						self.create_v_tunnel(prev_y, new_y, new_x)
					else:
						# first move vertically, then horizontally
						self.create_v_tunnel(prev_y, new_y, prev_x)
						self.create_h_tunnel(prev_x, new_x, new_y)

				self.place_entities(new_room, entities)

				# finally, append the new room to the list
				rooms.append(new_room)
				num_rooms += 1

		self.room_list.append(rooms)

		self.stairs_down_x = center_of_last_room_x
		self.stairs_down_y = center_of_last_room_y

		#self.stairs_down_x = player.x + 2
		#self.stairs_down_y = player.y + 2

		self.stairs_up_x = player.x
		self.stairs_up_y = player.y

		stairs_component = Stairs(self.dungeon_level + 1)
		down_stairs = Entity(self.stairs_down_x, self.stairs_down_y, stairs_down, libtcod.white, 'Stairs Down', 
							render_order=RenderOrder.STAIRS, stairs=stairs_component)
		entities.append(down_stairs)

		if self.dungeon_level > 1:
			stairs_component = Stairs(self.dungeon_level - 1)
			up_stairs = Entity(self.stairs_up_x, self.stairs_up_y, stairs_up, libtcod.white, 'Stairs Up', 
								render_order=RenderOrder.STAIRS, stairs=stairs_component)
			entities.append(up_stairs)

		"""

		if self.dungeon_level > 1:
			bonfire_component = Bonfire(self.dungeon_level)
			up_stairs = Entity(self.stairs_up_x+1, self.stairs_up_y-1, '*', libtcod.dark_red, 'Mysterious Bonfire', 
								blocks=True, render_order=RenderOrder.BONFIRE, invulnerable=True, bonfire=bonfire_component)
			entities.append(up_stairs)


		if self.dungeon_level == 1:
			item_description = ("A simple scroll with otherwise unintelligible glyphs scrawled across it.\n"
									"You are capable of interpreting the word \"Fire\", though what exactly that\n"
									"means remains to be seen.")
			item_component = Item(description=item_description, use_function=cast_fireball, targeting=True, targeting_message=Message(
				'Left-click a target tile for the fireball,\nor right-click to cancel.', libtcod.light_cyan),
								  targeting_range=7, area_of_effect=3, damage=25)
			item = Entity(player.x+1, player.y, '#', libtcod.red, 'Fireball Scroll', render_order=RenderOrder.ITEM,
						  item=item_component)
			entities.append(item)

		if self.dungeon_level == 1:
			item_description = ("The longer you attempt to understand the words on this scroll the more\n"
									"you feel like you've been tricked.")
			item_component = Item(description=item_description, use_function=cast_confuse, targeting=True, targeting_message=Message(
				'Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan),
								 targeting_range=9, area_of_effect=1)
			item = Entity(player.x+2, player.y, '#', libtcod.light_pink, 'Confusion Scroll', render_order=RenderOrder.ITEM,
						  item=item_component)
			entities.append(item)

		if self.dungeon_level == 1:
			item_description = ("A simple scroll with otherwise unintelligible glyphs scrawled across it.\n"
									"You feel a jolt of energy when you hold it.\n"
									"The word \"Lightning\" is scarred into the top of the paper.")
			item_component = Item(description=item_description, use_function=cast_lightning, damage=40, maximum_range=5)
			item = Entity(player.x+3, player.y, '#', libtcod.yellow, 'Lightning Scroll', render_order=RenderOrder.ITEM,
						  item=item_component)
			entities.append(item)
		"""

		if self.dungeon_level == 1:
			dialogue_component = Dialogue(character='The Story Teller', scene='Intro')
			story_teller = Entity(center_of_last_room_x - 1, center_of_last_room_y - 1, mysterious_old_man, libtcod.orange, 
				'The Story Teller', blocks=True, render_order=RenderOrder.ACTOR, dialogue=dialogue_component, invulnerable=True)
			entities.append(story_teller)


		"""

		if self.dungeon_level == 1:
			equippable_component = Equippable(EquipmentSlots.MAIN_HAND, ranged=False, min_damage_bonus=1, max_damage_bonus=2)
			item = Entity(player.x-1, player.y-1, '/', libtcod.cyan, 'Broken Iron Sword', render_order=RenderOrder.ITEM,
						  equippable=equippable_component)
			item.item.description = ("Long ago a knight stood atop the battlements of lost Fort Grey Mount.\n"
									 "He looked wistfully to the fields in the distance.\n\n"
								 	 "\"Such a waste..\" He thought, as he threw his sword to the ground.")
			entities.append(item)
		"""

		if self.dungeon_level == 1:
			equippable_component = Equippable(EquipmentSlots.MAIN_HAND, ranged=True, min_damage_bonus=1, max_damage_bonus=2)
			item = Entity(player.x-1, player.y-1, generic_bow, libtcod.sepia, 'Flimsy Wooden Bow', render_order=RenderOrder.ITEM,
						  equippable=equippable_component)
			item.item.targeting_range = 9
			item.item.area_of_effect = 1
			item.item.description = ("Legends tell of a woman who made wielding a bow an art form."
									"You probably wont get much accomplished with this thing though.")
			entities.append(item)
		


	def create_room(self, room):
		# go through the tiles in the rectangle and make them passable
		for x in range(room.x1 + 1, room.x2):
			for y in range(room.y1 + 1, room.y2):
				self.tiles[x][y].blocked = False
				self.tiles[x][y].block_sight = False

	def create_h_tunnel(self, x1, x2, y):
		for x in range(min(x1, x2), max(x1, x2) + 1):
			self.tiles[x][y].blocked = False
			self.tiles[x][y].block_sight = False

	def create_v_tunnel(self, y1, y2, x):
		for y in range(min(y1, y2), max(y1, y2) + 1):
			self.tiles[x][y].blocked = False
			self.tiles[x][y].block_sight = False

	def place_entities(self, room, entities):
		max_monsters_per_room = from_dungeon_level([[3,1],[5,3],[8,5]], self.dungeon_level)
		max_items_per_room = from_dungeon_level([[1,1],[2,4]], self.dungeon_level)
		# Get a random number of monsters
		number_of_monsters = randint(0, max_monsters_per_room)

		# Get a random number of items
		number_of_items = randint(0, max_items_per_room)

		monster_chances = get_easy_monsters(self.dungeon_level)

		item_chances = get_early_items(self.dungeon_level)

		for i in range(number_of_monsters):
			# Choose a random location in the room
			x = randint(room.x1 + 1, room.x2 - 1)
			y = randint(room.y1 + 1, room.y2 - 1)

			# Check if an entity is already in that location
			if not any([entity for entity in entities if entity.x == x and entity.y == y]):
				monster_choice = random_choice_from_dict(monster_chances)

				monster = choose_easy_monster(monster_choice, self.dungeon_level, x, y)

				entities.append(monster)

		for i in range(number_of_items):
			x = randint(room.x1 + 1, room.x2 - 1)
			y = randint(room.y1 + 1, room.y2 - 1)

			if not any([entity for entity in entities if entity.x == x and entity.y == y]):
				item_choice = random_choice_from_dict(item_chances)

				item = choose_early_item(item_choice, x, y)

				entities.append(item)

	def is_blocked(self, x, y):
		if self.tiles[x][y].blocked:
			return True

		return False

	def new_floor(self, player, message_log, constants):
		self.dungeon_level += 1
		entities = [player]

		self.tiles = self.initialize_tiles()
		self.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
					  constants['map_width'], constants['map_height'], player, entities)

		player.combat_class.heal(player.combat_class.max_hp // 2)

		message_log.add_message(Message('You take a moment to rest, and recover your strength.', libtcod.light_violet))

		return entities

	def previous_floor(self, player, entity_index, floor_index, fov_index, message_log, constants):
		self.dungeon_level -= 1

		self.tiles = self.initialize_tiles()
		self.tiles = floor_index[self.dungeon_level-1]
		fov_map = fov_index[self.dungeon_level-1]
		entities = [player]
		entities.extend(entity_index[self.dungeon_level-1])


		# Place the player on top of the stairs to the floor one down
		for entity in entities:
			if entity.name == 'Stairs Down':
				player.x = entity.x
				player.y = entity.y

				break
		message_log.add_message(Message('You climb up familiar stairs.', libtcod.light_violet))		

		return entities, player, fov_map

	def next_floor(self, player, entity_index, floor_index, fov_index, message_log, constants):

		self.dungeon_level += 1

		self.tiles = self.initialize_tiles()
		self.tiles = floor_index[self.dungeon_level-1]
		fov_map = fov_index[self.dungeon_level-1]
		entities = [player]
		entities.extend(entity_index[self.dungeon_level-1])

		# Place the player on top of the stairs to the floor one up
		for entity in entities:
			if entity.name == 'Stairs Up':
				player.x = entity.x
				player.y = entity.y

				break
		message_log.add_message(Message('You climb down familiar stairs.', libtcod.light_violet))		

		return entities, player, fov_map

	def clear_entities(self, entity_index):

		for entities in entity_index:
			for entity in entities:
				#if not entity.stairs and entity.blocks and not entity.bonfire and not entity.player and entity.alive:
				if not (entity.stairs and entity.bonfire) and entity.blocks and entity.alive:
					entities.remove(entity)

		return entity_index

	def replace_entities(self, original_entity_index, entity_index):

		for x in range(len(original_entity_index)-1):
			entity_index[x] = original_entity_index[x]
		return entity_index
