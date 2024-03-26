############################################################################################################
# Task Nr.1 :

# Instructions:

# Connect to a MongoDB server running on localhost.
# Create a new database named 'exercise_db' and a collection named 'exercise_collection'.
# Define the following JSON schema validation rules for the collection:
# The document must be an object.
# The 'name' field is required and must be a string.
# The 'age' field is required and must be an integer between 18 and 99.
# The 'email' field is required and must be a string containing a valid email address.
# Insert three documents into the collection, one that satisfies the validation rules and two that violate the validation rules.
# Print all the documents in the collection.
# Clean up by dropping the collection and closing the MongoDB connection.

# from pymongo import MongoClient
# from pymongo.errors import OperationFailure

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")
# db = client["exercise_db"]
# collection = db["exercise_collection"]

# # Define the validation rules as a dictionary
# validation_rules = {
#     "validator": {
#         "$jsonSchema": {
#             "bsonType": "object",
#             "required": ["name", "age", "email"],
#             "properties": {
#                 "name": {"bsonType": "string", "description": "Name must be a string."},
#                 "age": {
#                     "bsonType": "int",
#                     "minimum": 18,
#                     "maximum": 99,
#                     "description": "Age must be an integer between 18 and 99.",
#                 },
#                 "email": {
#                     "bsonType": "string",
#                     "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
#                     "description": "Email must be a valid email address.",
#                 },
#             },
#         }
#     }
# }

# # Set the validation rules for the collection
# # try:
# #     db.command("collMod", collection.name, **validation_rules)
# #     print("Schema validation enabled.")
# #     document = {
# #         "name": "Albert",
# #         "age": 19,
# #         "email": "albert@gmail.com",
# #     }
# #     result = collection.insert_one(document)
# # except OperationFailure as e:
# #     print(f"Failed to enable schema validation: {e.details['errmsg']}")


# result = collection.find({}, {"_id": 0})
# for x in result:
#     print(x)

# # Clean up (optional)
# collection.drop()
# client.close()

##################################################################################################

# Task Nr.2:

# Instructions:

# Connect to a MongoDB server running on localhost.
# Create a new database named 'shopping_db' and a collection named 'shopping_collection'.
# Define the following JSON schema validation rules for the collection:
# The document must be an object.
# The 'name' field is required and must be a string.
# The 'age' field is required and must be an integer between 18 and 99.
# The 'email' field is required and must be a string containing a valid email address.
# The 'address' field is required and must be an object.
# The 'address' object must have the 'street', 'city', and 'postal_code' fields, each being a required string.
# Insert three documents into the collection, one that satisfies the validation rules and two that violate the validation rules.
# Print all the documents in the collection.
# Clean up by dropping the collection and closing the MongoDB connection.


# from pymongo import MongoClient
# from pymongo.errors import OperationFailure

# client = MongoClient("mongodb://localhost:27017/")
# db = client["shopping_db"]
# collection = db["shopping_collection"]

# # Check if the collection exists, create it if it doesn't
# if collection.name not in db.list_collection_names():
#     db.create_collection(collection.name)

# validation_rules = {
#     "validator": {
#         "$jsonSchema": {
#             "bsonType": "object",
#             "required": ["name", "age", "email", "address"],
#             "properties": {
#                 "name": {"bsonType": "string", "description": "Name must be a string."},
#                 "age": {"bsonType": "int", "minimum": 18, "maximum": 99, "description": "Age must be an integer between 18 and 99."},
#                 "email": {"bsonType": "string", "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", "description": "Email must be a valid email address."},
#                 'address': {
#                     "bsonType": "object",
#                     "required": ["street", "city", "postal_code"],
#                     "properties": {
#                         "street": {"bsonType": "string"},
#                         "city": {"bsonType": "string"},
#                         "postal_code": {"bsonType": "string"}
#                     }
#                 }
#             }
#         }
#     }
# }

# try:
#     db.command("collMod", collection.name, **validation_rules)
#     print("Schema validation enabled.")
#     document = {
#         "name": "Albert",
#         "age": 19,
#         "email": "albert@gmail.com",
#         "address": {
#             "street": "123 Main St",
#             "city": "Anytown",
#             "postal_code": "12345"
#         }
#     }
#     result = collection.insert_one(document)
# except OperationFailure as e:
#     print(f"Failed to enable schema validation: {e.details['errmsg']}")

# result = collection.find({}, {"_id": 0})
# for x in result:
#     print(x)

# client.close()

################################## Sauliaus ########################################################## biski Bito pakoregavo, nes neveike

# from random import randint
# from typing import Optional
# from faker import Faker
# from pymongo import MongoClient
# from pymongo.errors import OperationFailure, PyMongoError

# client = MongoClient("mongodb://localhost:27017/")
# db = client["shopping_db"]
# collection = db["shopping_collection"]

# def create_random_person() -> Optional[str]:
#     fake = Faker()
#     name = fake.first_name()
#     age = randint(18, 99)
#     email = f"{name}@{fake.last_name()}.com"
#     document = {
#         "name": name,
#         "age": age,
#         "email": email,
#         "address": {
#             "street": "Koks skirtumas",
#             "city": "Kaunas",
#             "postal_code": "12345",
#         },
#     }
#     result = collection.insert_one(document)
#     return str(result.inserted_id)

# def generate_data_base(numb_of_documents):
#     for _ in range(numb_of_documents):
#         create_random_person()

# # Define the validation rules as a dictionary
# validation_rules = {
#     "validator": {
#         "$jsonSchema": {
#             "bsonType": "object",
#             "required": ["name", "age", "email"],
#             "properties": {
#                 "name": {"bsonType": "string"},
#                 "age": {"bsonType": "int", "minimum": 18, "maximum": 99},
#                 "email": {
#                     "bsonType": "string",
#                     "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
#                 },
#                 "address": {
#                     "bsonType": "object",
#                     "required": ["street", "city", "postal_code"],
#                     "properties": {
#                         "street": {"bsonType": "string"},
#                         "city": {"bsonType": "string"},
#                         "postal_code": {"bsonType": "string"},
#                     },
#                 },
#             },
#         }
#     }
# }

# # Set the validation rules for the existing collection
# try:
#     db.command("collMod", collection.name, **validation_rules)
#     print("Schema validation enabled.")
#     generate_data_base(3)
# except OperationFailure as e:
#     print(f"Failed to enable schema validation: {e.details['errmsg']}")

# # Clean up (optional)
# client.close()


