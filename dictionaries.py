"""
-> Dictonaries store data in key-value pairs
  Properties:
   *Key-Value Pairs
   *Unordered (but insertion is ordered in python 3.7+ only)
   *Mutable (can be changed)
   *Indexed (cannot be accessed using index)
   *Allow duplicate keys but only the last value for each key will be stored
   *No fixed size (can grow and shrink)
   *Can be nested (dictionaries can contain other dictionaries)
   
"""

student_name = {
    "name": "Natasha",
    "age": 18,
    "city": "Nakuru"
}

#ACCESSING

student_name["name"]

#ADDING/UPDATE

student_name["city"] = "Nairobi"

#DELETING

del student_name["age"]

#LOOPING

for key, value in student_name.items():
    print (key, value)

#KEYS & VALUES

student_name.keys()
student_name.values()

#NESTING

students = {
    "student_1": {
        "name": "Natasha",
        "age": 18,
        "city": "Nakuru"
    },
    "student_2": {
        "name": "Jr",
        "age": 17,
        "city": "Nakuru"
    }
}