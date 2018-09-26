class Bonfire:
	def __init__(self, floor):
		self.floor = floor


	def reset_entities(self, game_map, floor_index, entity_index):

		return game_map.clear_entities(floor_index, entity_index)