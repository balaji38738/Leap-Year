from itertools import product

class CoinProbabilityCalc:
    perm_of_3_coins = list(product({"H", "T"}, repeat=3))
    total_perms = len(perm_of_3_coins)

    # Given face & its max in min occurence returns probability
    def find_probability(self, face, min, max):
        event_set_len = 0
        for perm in self.perm_of_3_coins:
            if perm.count(face) >= min and perm.count(face) <= max:
                event_set_len += 1
        return event_set_len / self.total_perms

coin_prob_calc = CoinProbabilityCalc()

# Prints probability of exactly 3 heads
print("Probability of exactly 3 heads =", end=" ")
print(f"{coin_prob_calc.find_probability('H', 3, 3):.4f}")

# Prints probability of exactly 1 head
print("Probability of exactly 1 head =", end=" ")
print(f"{coin_prob_calc.find_probability('H', 1, 1):.4f}")

# Prints probability of at least 2 heads
print("Probability of at least 2 heads =", end=" ")
print(f"{coin_prob_calc.find_probability('H', 2, 3):.4f}")