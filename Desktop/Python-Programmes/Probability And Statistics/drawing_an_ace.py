# Returns probability of drawing an ace from a deck
def find_ace_probability():
    ACSES = 4
    TOTAL_CARDS = 52
    return ACSES / TOTAL_CARDS

print(f"Probability of drawing an ace = {find_ace_probability():.4f}")
