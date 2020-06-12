import json

student = {"Name": "Balaji", "Branch": "E&Tc", "Subjects": ["Electromagnetics", "LARV", "Digital Electronics"],
             "Roll No": 21}
print(json.dumps(student, indent=4, separators=(",", ": ")))
print(json.dumps(student, indent=4, sort_keys=True))