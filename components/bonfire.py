class Bonfire:
	def __init__(self, floor):
		self.floor = floor


	def reset_entities(self, game_map, original_entity_index, entity_index):

		entity_index = game_map.clear_entities(entity_index)

		return game_map.replace_entities(original_entity_index, entity_index)