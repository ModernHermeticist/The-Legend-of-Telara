import os

import shelve

def save_game(player, entities, game_map, message_log, game_state, floor_index, entity_index, fov_index):
	with shelve.open('savegame', 'n') as data_file:
		data_file['player_index'] = entities.index(player)
		data_file['entities'] = entities
		data_file['game_map'] = game_map
		data_file['message_log'] = message_log
		data_file['game_state'] = game_state
		data_file['floor_index'] = floor_index
		data_file['entity_index'] = entity_index
		data_file['fov_index'] = fov_index

def load_game():
	if not os.path.isfile('savegame.dat'):
		raise FileNotFoundError

	with shelve.open('savegame', 'r') as data_file:
		player_index = data_file['player_index']
		entities = data_file['entities']
		game_map = data_file['game_map']
		message_log = data_file['message_log']
		game_state = data_file['game_state']
		floor_index = data_file['floor_index']
		entity_index = data_file['entity_index']
		fov_index = data_file['fov_index']

	os.remove('savegame.dat')
	os.remove('savegame.dir')
	os.remove('savegame.bak')

	player = entities[player_index]

	return player, entities, game_map, message_log, game_state, floor_index, entity_index, fov_index
