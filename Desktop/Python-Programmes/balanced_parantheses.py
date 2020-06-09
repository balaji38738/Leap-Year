class BalancedParanthesesChecker:
    brackets = {"{": "}", "[": "]", "(": ")"}
    brackets_set = set(brackets.keys()).union(set(brackets.values()))

    @classmethod
    def is_valid_expression(cls, expression):
        return set(expression).issubset(cls.brackets_set)

    @classmethod
    def is_balanced(cls, expression):
        stack = []
        for bracket in expression:
            if bracket in cls.brackets.keys():
                stack.append(bracket)
            elif cls.brackets[stack[-1]] == bracket:
                stack.pop()
            else:
                return False
        else:
            return True
    
expression = input("Enter parantheses expression: ")
if BalancedParanthesesChecker.is_valid_expression(expression):
    if BalancedParanthesesChecker.is_balanced(expression):
        print("Balanced parantheses")
    else:
        print("Unbalanced parantheses")
else:
    print("Expression should only contain", BalancedParanthesesChecker.brackets_set)

