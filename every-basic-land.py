import scrython
import time

has_more = True
page = 0
while has_more:
	page += 1
	search = scrython.cards.Search(
		q = "t:basic",
		unique = "art",
		order = "released",
		dir = "desc",
		page = page
	)

	print('\n'.join(map(lambda card: f"1 {card['name']} ({card['set']}) {card['collector_number']}", search.data())))

	has_more = search.has_more()
	time.sleep(0.1)
