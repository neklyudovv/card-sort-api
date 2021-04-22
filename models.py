class Card():
	def __init__(self, transport_type,transport_number, departure, destination, gate, seat, baggage):
		self.transport_type = transport_type
		self.transport_number = transport_number
		self.departure = departure
		self.destination = destination
		self.gate = gate
		self.seat = seat
		self.baggage = baggage

	def get_type(self):
		msg = ''
		if self.transport_type != '':
			msg += f'Take {self.transport_type}'
		if self.transport_number != '':
			msg += f' {self.transport_number}'
		return msg


	def get_from_to(self):
		msg = ''
		if self.departure != '' and self.destination != '':
			msg = f'from {self.departure} to {self.destination}.'
		return msg


	def get_gate(self):
		msg = ''
		if self.gate != '':
			msg = f'Gate {self.gate}.'
		return msg


	def get_seat(self):
		msg = ''
		if self.seat != '':
			msg = f'Seat {self.seat}.'
		return msg


	def get_baggage(self):
		msg = ''
		if self.baggage.isdigit(): 
			msg = f'Baggage drop at ticket counter {self.baggage}.'
		if self.baggage == 'auto':
			msg = f'Baggage will be automatically dropped from your last leg.'
		return msg