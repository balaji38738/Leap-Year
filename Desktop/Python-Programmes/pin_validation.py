import re
print("PIN validation programme")

class PINValidator:
    pattern = r"^[0-9]{3}(\s)*[0-9]{3}$"

    @staticmethod
    def validate_pin(pin):
        return re.match(__class__.pattern, pin)

pin = input("Enter PIN: ")
if PINValidator.validate_pin(pin):
    print("Valid PIN")
else:
    print("Invalid PIN")
