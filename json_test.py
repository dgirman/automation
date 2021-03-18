##
#
#

import json
import requests

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]




with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)

json_string = json.dumps(data, indent=4)
print(json_string) 

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)  #json to data
decoded_hand = json.loads(encoded_hand)    #data to json

print(blackjack_hand == decoded_hand)

print(type(blackjack_hand))

print(type(decoded_hand))

print(blackjack_hand == tuple(decoded_hand))

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)


json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(data)

print('')
print('')

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


print(type(todos))
print(todos[:10])
#print(todos)

# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

# Define a function to filter out completed TODOs 
# of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)





# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

elf = Elf(level=4)
#json.dumps(elf)

z = 3 + 8j
print(type(z))

#json.dumps(z)

print(z.real)
print(z.imag)

print (complex(3, 8) == z)

def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

json.dumps(9 + 5j, default=encode_complex)

json.dumps(elf, default=encode_complex)


