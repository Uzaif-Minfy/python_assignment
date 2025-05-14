""" Write a function called invert_dictionary that takes a dictionary and returns a new dictionary 
where the keys become values and values become keys. """
def invert_dictionary(d):
    return {value: key for key, value in d.items()}

print(invert_dictionary({"a": 1, "b": 2, "c": 3}))
# Output: {1: 'a', 2: 'b', 3: 'c'}





print("\n")
""" Write a function called merge_dictionaries that takes two dictionaries and merges them. 
If a key exists in both dictionaries, the value from the second dictionary should be used. """
def merge_dictionaries(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))
# Output: {'a': 1, 'b': 3, 'c': 4}





print("\n")
""" Write a function called word_frequencies that takes a string of text and returns a dictionary 
mapping each word to its frequency (count of occurrences). """
def word_frequencies(text):
    words = text.split()
    return {word: words.count(word) for word in set(words)}

text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
# Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}





print("\n")
""" Create a function called add_contact that manages a nested dictionary representing a contact book.
The function should add a new contact with details or update an existing contact. """
def add_contact(contacts, name, **info):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(info)

contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")  # Updates Alice's info

print(contacts)
# Output:
# {
#   "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
#   "Bob": {"phone": "987-654-3210"}
# }
