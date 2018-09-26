import libtcodpy as libtcod

from random_utils import from_dungeon_level

from render_functions import RenderOrder


from components.ai import BasicMonster
from components.combat_classes.fighter import Fighter
from entity import Entity


def get_easy_monsters(dungeon_level):

	monster_chances = {
			'orc': from_dungeon_level([[60,1],[30,3],[10,4],[0,5]], dungeon_level),
			'gnoll': from_dungeon_level([[80,1],[50,2],[30,3],[0,4]], dungeon_level),
			'troll': from_dungeon_level([[15,3],[30,5],[60,7]], dungeon_level)
			}
	return monster_chances


def choose_easy_monster(monster_choice, dungeon_level, x, y):
	if monster_choice == 'gnoll':
		class_component = Fighter(hp=20+(dungeon_level), mp=0, armor=0, min_damage=0,
									max_damage=2+(dungeon_level-1), xp=20+(2*(dungeon_level-1)))
		ai_component = BasicMonster()

		monster = Entity(x, y, 'n', libtcod.desaturated_green, 'Gnoll', alive=True, blocks=True,
						 render_order=RenderOrder.ACTOR, combat_class=class_component, ai=ai_component)

	elif monster_choice == 'orc':
		class_component = Fighter(hp=20+(2*dungeon_level-1), mp=0, armor=0, min_damage=0,
									max_damage=3+(dungeon_level-1), xp=35+(5*(dungeon_level-1)))
		ai_component = BasicMonster()

		monster = Entity(x, y, 'o', libtcod.desaturated_green, 'Orc', alive=True, blocks=True,
						 render_order=RenderOrder.ACTOR, combat_class=class_component, ai=ai_component)
	elif monster_choice == 'troll':
		class_component = Fighter(hp=30+(2*dungeon_level-1), mp=0, armor=3, min_damage=0,
									max_damage=4+(dungeon_level-1), xp=100+(5*(dungeon_level-1)))
		ai_component = BasicMonster()

		monster = Entity(x, y, 'T', libtcod.darker_green, 'Troll', alive=True, blocks=True, combat_class=class_component,
						 render_order=RenderOrder.ACTOR, ai=ai_component)

	return monster