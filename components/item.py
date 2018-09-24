class Item:
	def __init__(self, description=None, use_function=None, targeting=False, targeting_message=None, targeting_range=None, **kwargs):
		self.description = description
		self.use_function = use_function
		self.targeting = targeting
		self.targeting_message = targeting_message
		self.targeting_range = targeting_range
		self.function_kwargs = kwargs