import importlib.resources
import json

with open('input.json') as user_file:
  parsed_json = json.load(user_file)

# print("The original JSON data:\n{0}".format(parsed_json))
print("the first entry:\n{0}".format(parsed_json[0]))

 # ONLY LINE TO ADAPT FOR WHAT YOU WANT TO SORT (!fieldname for reverse)
sorting_fields = ["!price", "sell"]

def reverse_sort(parsed_json, field):
    field = field.replace("!", "")
    parsed_json = sorted(parsed_json, key=lambda x: x[field], reverse=True)
    return parsed_json

def sort_json(parsed_json):
    for field in sorting_fields:
        if field.startswith("!"):
            field = field.replace("!", "")
            parsed_json = sorted(parsed_json, key=lambda x: x[field], reverse=True)
            return parsed_json

        parsed_json = sorted(parsed_json, key=lambda x: x[field])
    return parsed_json

sorted_json = sort_json(parsed_json)
# print("The sorted JSON data based on the value of the brand:\n{0}".format(sorted_json))
print("the first entry:\n{0}".format(sorted_json[0]))

with open('output.json', 'w') as outfile:
  outfile.write(json.dumps(sorted_json, indent=2))
