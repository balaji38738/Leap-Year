import json

student = {"Name": "Balaji", "Branch": "E&Tc", "Subjects": ["Electromagnetics", "LARV", "Digital Electronics"]}
print(json.dumps(student, indent=4, separators=(".", ": ")))