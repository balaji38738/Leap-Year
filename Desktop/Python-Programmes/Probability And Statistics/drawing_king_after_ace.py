# Returns probability of drawing a king after ace
def find_probability(kings, cards_left):
    return kings / cards_left

TOTAL_CARDS = 52

# Number of cards after drawing an ace
remaining_cards = TOTAL_CARDS - 1
KINGS = 4
print("Probability of drawing a king after ace =", end=" ")
print(f"{find_probability(KINGS, remaining_cards):.4f}")