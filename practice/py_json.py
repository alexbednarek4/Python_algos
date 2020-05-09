# Parsing JSON into Python dictionary

import json

#Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

#Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

#Make dictionary JSON
car = {'make': "Tesla", "Model": 3}
carJSON = json.dumps(car)
print(carJSON)