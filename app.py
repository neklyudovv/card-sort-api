from models import Card

ALLOWED_TRANSPORTS = ['bus', 'train', 'flight']
cards = []

def send(cards):
	msg = ''
	for card in cards:
		msg += card.get_type() + ' ' + card.get_from_to() +  ' ' + card.get_gate() + ' ' + card.get_seat() + ' ' + card.get_baggage() + '\n'
	return msg.replace('  ', ' ')


def validate(cards):
	for card in cards:
		if card[0] not in ALLOWED_TRANSPORTS:
			return False
	return True


def sort_cards(cards):
	sorted_cards = []

	for i in range(0, len(cards)):
		count = 0
		for j in range(0, len(cards)):
			if cards[i].departure == cards[j].destination:
				count += 1
		if count == 0:
			sorted_cards.append(cards[i])

	for i in range(1, len(cards)):
		for j in range(0, len(cards)):
			if cards[j].departure == sorted_cards[i-1].destination:
				sorted_cards.append(cards[j])

	return sorted_cards


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
		return send(sort_cards(cards))
	return 'Некорректные данные'

# на выходе мы получили полностью провалидированый массив обьектов, которые нам осталось
# только отсортировать и вывести в правильном формате.

print(start([['bus', '', 'Moscow', 'Madrid', '', '', ''], ['train', 'AW412', 'Madrid', 'Stanbul', '', '', ''], ['bus', '', 'Barcelona', 'Gerona Airport', '', '', ''], ['train', '78A', 'Stanbul', 'Barcelona', '', '45B', 'auto'], ['flight', 'SK455', 'Gerona Airport', 'Stockholm', '45B', '3A', '344']]))