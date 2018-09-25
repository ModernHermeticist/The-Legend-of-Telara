import libtcodpy as libtcod

from components.ai import ConfusedMonster

from game_messages import Message

def heal(owner, targeting_range, area_of_effect, damage, heal_amount, entities, fov_map, target_x, target_y):

	results = []

	if owner.combat_class.hp == owner.combat_class.max_hp:
		results.append({'consumed': False, 'message': Message('You are already at full health!', libtcod.yellow)})

	else:
		owner.combat_class.heal(heal_amount)
		results.append({'consumed': True, 'message': Message('Your wounds begin to heal!', libtcod.green)})

	return results

def cast_lightning(caster, targeting_range, area_of_effect, damage, heal_amount, maximum_range, entities, fov_map, target_x, target_y):

	results = []

	target = None
	closest_distance = maximum_range + 1

	for entity in entities:
		if entity.alive and entity.combat_class and entity != caster and libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
			distance = caster.distance_to(entity)

			if distance < closest_distance:
				target = entity
				closest_distance = distance

	if target:
		results.append({'consumed': True, 'target': target, 'message': \
		 Message('A lightning bolt strikes the {0} with a loud crack! The damage is {1}.'.format(target.name, damage))})
		results.extend(target.combat_class.take_damage(damage))
	else:
		results.append({'consumed': False, 'target': None, 'message': Message('No enemy is close enough to strike.', libtcod.red)})

	return results

def cast_fireball(caster, targeting_range, area_of_effect, damage, heal_amount, maximum_range, entities, fov_map, target_x, target_y):

	results = []

	targeting_range_offset = int(targeting_range / 2)


	area_of_effect_offset = int(area_of_effect / 2)


	if caster.distance(target_x, target_y) > targeting_range_offset:
		results.append({'consumed': False, 'message': Message('You cannot target a tile outside your casting range.', libtcod.yellow)})
		return results
	elif not libtcod.map_is_in_fov(fov_map, target_x, target_y):
		results.append({'consumed': False, 'message': Message('You cannot see your target.', libtcod.yellow)})
		return results

	results.append({'consumed': True, 'message': Message('The fireball explodes, burning everything within {0} tiles!'.format(
					area_of_effect_offset), libtcod.orange)})

	for entity in entities:
		if entity.distance(target_x, target_y) <= area_of_effect_offset+1 and entity.combat_class:
			results.append({'message': Message('The {0} gets burned for {1} damage.'.format(entity.name, damage), libtcod.orange)})
			results.extend(entity.combat_class.take_damage(damage))

	return results

def cast_confuse(caster, targeting_range, area_of_effect, damage, heal_amount, entities, fov_map, target_x, target_y):

	results = []

	targeting_range_offset = int(targeting_range / 2)


	area_of_effect_offset = int(area_of_effect / 2)


	if caster.distance(target_x, target_y) > targeting_range_offset+1:
		results.append({'consumed': False, 'message': Message('You cannot target a tile outside your casting range.', libtcod.yellow)})
		return results

	for entity in entities:
		if entity.x == target_x and entity.y == target_y and entity.ai:
			confused_ai = ConfusedMonster(entity.ai, 10)

			confused_ai.owner = entity
			entity.ai = confused_ai

			results.append({'consumed': True, 'message': Message('The eyes of the {0} look vacant and it starts to stumble around!'.format(entity.name), libtcod.light_green)})

			break

	else:
		results.append({'consumed': False, 'message': Message('There is no targetable enemy at that location.', libtcod.yellow)})

	return results
