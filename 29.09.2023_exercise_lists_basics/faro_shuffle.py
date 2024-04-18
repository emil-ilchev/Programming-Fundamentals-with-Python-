deck_of_cards = input().split()
count_of_shuffles = int(input())
for num in range(count_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    final_deck = []
    for shuffles in range(middle_of_deck):
        final_deck.append(left_part[shuffles])
        final_deck.append(right_part[shuffles])
        deck_of_cards = final_deck
print(final_deck)
