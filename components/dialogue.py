class Dialogue:
	def __init__(self, character=None, scene=None):
		self.character = character
		self.scene = scene
		self.dialogue = None

		self.choose_character_dialogue()

	def choose_character_dialogue(self):
		characters = {
					'The Story Teller': self.the_story_teller()
		}

		if self.character in characters:
			characters[self.character]

	def choose_character_dialogue_scene(self):
		scenes = {
				'Intro': self.the_story_teller_intro()
		}
		if self.scene in scenes:
			scenes[self.scene]


	def the_story_teller(self):
		self.choose_character_dialogue_scene()

	def the_story_teller_intro(self):
		self.dialogue = ("You see a mysterious old man before you.\n"
						 "He turns towards you.\n\n\n\n"
						 "          He winks!")


