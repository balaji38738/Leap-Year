# Returns probability of drawing an ace after a king
def find_probability(aces, cards_left):
    return aces / cards_left

TOTAL_CARDS = 52

# Number of cards after drawing an ace
remaining_cards = TOTAL_CARDS - 1
ACES = 4
print("Probability of drawing an ace after king =", end=" ")
print(f"{find_probability(ACES, remaining_cards):.4f}")