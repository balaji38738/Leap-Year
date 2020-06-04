import re
print("PIN validation programme")

class PINValidator:
    pin_pattern = r"^[0-9]{3}(\s)?[0-9]{3}$"

    @staticmethod
    def validate_pin(pin):
        return re.match(__class__.pin_pattern, pin)

pin = input("Enter PIN: ")
if PINValidator.validate_pin(pin):
    print("Valid PIN")
else:
    print("Invalid PIN")
