from models import Card

# [{transport_type:str, transport_number:str, departure:str, 
#   destination:str, gate:str, seat:str, baggage:str}]

#func1: сделать массив обьектов класса Card
#func2: сопоставить карточки в правильном порядке
#func3: вывод данных в правильном формате

def get_type(card):
	print(card, card.transport_type)
	msg = ''
	if card.transport_type != '' and card.transport_number != '':
		msg += f'Take {card.transport_type} {card.transport_number}'
	return msg


def get_from_to(card):
	msg = ''
	if card.departure != '' and card.destination != '':
		msg = f'from {card.departure} to {card.destination}.'
	return msg


def get_gate(card):
	msg = ''
	if card.gate != '':
		msg = f'Gate {card.gate}.'
	return msg


def get_seat(card):
	msg = ''
	if card.seat != '':
		msg = f'Seat {card.seat}.'
	return msg


def get_baggage(card):
	msg = ''
	if card.baggage.isdigit(): 
		msg = f'Baggage drop at ticket counter {card.baggage}.'
	elif card.baggage == 'auto':
		msg = f''
	return msg


def send(cards):
	msg = ''
	for card in sorted_cards:
		msg += get_type(card) + get_from_to(card) + get_gate(card) + get_seat(card) + get_baggage(card) + '\n'
	return ''


def validate(cards):
	for card in cards:
		if card[0] not in ALLOWED_TRANSPORTS:
			return False
	return True


def sort_cards(cards):
	for i in range(0, len(cards)):
		for j in range(0, len(cards)):
			if cards[i].destination == cards[j].departure:
				sorted_cards.append(cards[i])
				sorted_cards.append(cards[j])
	return cards

ALLOWED_TRANSPORTS = ['bus', 'train', 'flight']
cards = []
sorted_cards = []

def start(input_cards_list):
	if validate(input_cards_list):
		for input_card in input_cards_list:
			new_card = Card(transport_type=str(input_card[0]),
							transport_number=str(input_card[1]),
							departure=str(input_card[2]),
							destination=str(input_card[3]),
							gate=str(input_card[4]),
							seat=str(input_card[5]),
							baggage=str(input_card[6]))
			cards.append(new_card)
		sort_cards(cards)
		return send(sorted_cards)

# на выходе мы получили полностью провалидированый массив обьектов, которые нам осталось
# только отсортировать и вывести в правильном формате.

print(start([['bus', '', 'Barcelona', 'Gerona Airport', '', '', ''], ['train', '78A', 'Madrid', 'Barcelona', '', '45B', ''], ['flight', 'SK455', 'Gerona Airport', 'Stockholm', '45B', '3A', '344']]))