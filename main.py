# https://github.com/CodeAcademy-Online/python-new-material-level2/wiki/Mongo-DB-lesson-6:-Schema-Validation.
# https://pymongo.readthedocs.io/en/stable/api/bson/index.html


# Mongo DB lesson 6: Schema Validation.
# Mindaugeliseth edited this page on Jun 14, 2023 · 10 revisions

# Introduction
# MongoDB Schema Validation is a feature that allows you to enforce structure and integrity rules on the documents stored in a MongoDB collection. It enables you to define a set of validation rules that govern the structure and content of your data, ensuring that only valid and consistent documents are inserted or updated in the database.

# With schema validation, you can specify rules for fields such as data types, value ranges, required fields, and more. It helps maintain the data quality and consistency of your MongoDB collections, reducing the chances of storing invalid or inconsistent data.

# The validation rules are defined using the JSON schema format, which is a standardized way of describing the structure and constraints of JSON documents. You can define these rules when creating or updating a collection, and MongoDB will automatically enforce them when performing write operations on the collection.

# Schema validation in MongoDB can be used to enforce a wide range of constraints, including simple checks like data type validation, as well as complex rules involving relationships between fields and cross-field validation. This allows you to define custom rules that suit your specific data requirements.

# By enforcing schema validation, you can improve the reliability and quality of your data, making it easier to work with and ensuring that it adheres to the desired structure. It provides an additional layer of data integrity within your MongoDB deployments and helps prevent data inconsistencies and errors.

# It's worth noting that schema validation is an optional feature in MongoDB, and you can choose whether or not to enable it for your collections. When used appropriately, schema validation can be a powerful tool for maintaining the integrity and consistency of your MongoDB data.

# MongoDB Schema Validation Rules
# Validator: The validator defines the rules that documents must adhere to. It is specified as a dictionary within the validation_rules dictionary.

# $jsonSchema: The $jsonSchema key specifies the JSON schema syntax for defining the validation rules. It contains the main body of the validation rules.

# bsonType: The bsonType key specifies the expected data type for a field. It can be set to values such as string, int, double, array, object, and more.

# required: The required key specifies an array of field names that must be present in the document.

# properties: The properties key defines the individual field validations within the document. Each field is specified as a key-value pair, where the key is the field name and the value is the validation rule for that field.

# Additional Validation Rules: Within the properties key, you can define additional validation rules for each field. For example, minimum and maximum can be used to specify the range of values for a numeric field, and pattern can be used to enforce a specific format using regular expressions.

# To enable schema validation for a collection, you can use the collection.command('collMod', collection.name, validator=validation_rules) method in pymongo. This command modifies the collection's options and sets the validation rules.

# It's important to note that when using pymongo, if there is an error during the validation rule setup, an exception will be raised, and you should handle it appropriately.

# Remember to adjust the validation rules, database, and collection names according to your specific requirements.

# Example:

# from pymongo import MongoClient
# from pymongo.errors import OperationFailure

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['mydatabase']
# collection = db['mycollection']

# # Define the validation rules as a dictionary
# validation_rules = {
#     'validator': {
#         '$jsonSchema': {
#             'bsonType': 'object',
#             'required': ['name', 'age', 'email'],
#             'properties': {
#                 'name': {'bsonType': 'string'},
#                 'age': {'bsonType': 'int', 'minimum': 0},
#                 'email': {'bsonType': 'string', 'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'}
#             }
#         }
#     }
# }

# # Set the validation rules for the collection
# try:
#     db.command('collMod', collection.name, **validation_rules)
#     print("Schema validation enabled.")
# except OperationFailure as e:
#     print(f"Failed to enable schema validation: {e.details['errmsg']}")

# # Clean up (optional)
# client.close()
# In this example, we first connect to the MongoDB server and select a database and collection. The validation rules are defined as a dictionary using the JSON schema syntax.

# We then set the validation rules for the collection using the command method and the collMod command. The validator parameter is used to specify the validation rules dictionary. If an error occurs during the command execution, an OperationFailure exception is raised, and we extract and print the error message.

# Finally, we close the MongoDB client connection. It's important to close the connection to release resources properly.

# Make sure to replace mongodb://localhost:27017/ with the appropriate MongoDB connection string for your environment, and adjust the database and collection names accordingly.

# Another example:

# from pymongo import MongoClient

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['mydatabase']
# collection = db['mycollection']

# # Define the schema validation rules
# validation_rules = {
#     '$jsonSchema': {
#         'bsonType': 'object',
#         'required': ['name', 'age', 'email'],
#         'properties': {
#             'name': {
#                 'bsonType': 'string',
#                 'description': 'Name must be a string.'
#             },
#             'age': {
#                 'bsonType': 'int',
#                 'minimum': 0,
#                 'maximum': 120,
#                 'description': 'Age must be an integer between 0 and 120.'
#             },
#             'email': {
#                 'bsonType': 'string',
#                 'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$',
#                 'description': 'Email must be a valid email address.'
#             }
#         }
#     }
# }

# # Create the collection with schema validation
# db.create_index([('name', 1)], unique=True)  # Optional: Add unique index
# db.create_index(validation_rules, {'validator': {'$jsonSchema': validation_rules}})

# # Insert a document that satisfies the validation rules
# valid_doc = {
#     'name': 'John Doe',
#     'age': 30,
#     'email': 'johndoe@example.com'
# }
# collection.insert_one(valid_doc)

# # Insert a document that violates the validation rules
# invalid_doc = {
#     'name': 'Jane Smith',
#     'age': '25',  # Invalid data type
#     'email': 'janesmith'  # Invalid email format
# }
# try:
#     collection.insert_one(invalid_doc)
# except Exception as e:
#     print(f"Failed to insert document: {e}")

# # Retrieve all documents from the collection
# documents = collection.find()
# for doc in documents:
#     print(doc)

# # Clean up (optional)
# collection.drop()
# In this example, we first connect to the MongoDB server and create a database and a collection. We then define the schema validation rules using the $jsonSchema syntax. The validation rules specify that the document must have name, age, and email fields, with specific data types and constraints.

# Next, we create the collection and specify the validation rules using the create_index method. We also add an optional unique index on the name field to enforce uniqueness.

# We demonstrate the validation by inserting a valid document that satisfies the rules and an invalid document that violates the rules. When inserting the invalid document, an exception will be raised, and we catch and print the error message.

# Finally, we retrieve and print all the documents from the collection. At the end, we drop the collection as a cleanup step.

# Make sure to replace 'mongodb://localhost:27017/' with the appropriate MongoDB connection string for your environment.

# Multilevel document
# Here's an example of setting validation rules for a MongoDB collection with multi-level documents using pymongo, including type returns and following good code practices:

# from pymongo import MongoClient
# from pymongo.errors import OperationFailure

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['mydatabase']
# collection = db['mycollection']

# # Define the validation rules as a dictionary
# validation_rules = {
#     'validator': {
#         '$jsonSchema': {
#             'bsonType': 'object',
#             'required': ['name', 'age', 'contact'],
#             'properties': {
#                 'name': {'bsonType': 'string'},
#                 'age': {'bsonType': 'int', 'minimum': 0},
#                 'contact': {
#                     'bsonType': 'object',
#                     'required': ['email', 'phone'],
#                     'properties': {
#                         'email': {'bsonType': 'string'},
#                         'phone': {'bsonType': 'string', 'pattern': '^[0-9]{10}$'}
#                     }
#                 }
#             }
#         }
#     }
# }

# # Set the validation rules for the collection
# try:
#     db.command('collMod', collection.name, **validation_rules)
#     print("Schema validation enabled.")
# except OperationFailure as e:
#     print(f"Failed to enable schema validation: {e.details['errmsg']}")

# # Clean up (optional)
# client.close()
# In this example, we connect to the MongoDB server and select a database and collection. The validation rules are defined as a dictionary using the JSON schema syntax.

# The properties key within the validation rules dictionary is used to define the validation rules for each field. For a multi-level document, like in this example, you can nest additional properties dictionaries to define the validation rules for the nested fields.

# In the given example, the validation rules expect that the document has a name, age, and contact field. The contact field is further specified to have an email and phone field, each with its own validation rules.

# The rest of the code, including setting the validation rules and error handling, follows the same structure as the previous examples.

# Make sure to replace mongodb://localhost:27017/ with the appropriate MongoDB connection string for your environment, and adjust the database and collection names as needed.


############################################################################################################
# schema = {
#         "$jsonSchema": {
#             "bsonType": "object",
#             "required": ["name", "age", "email"],
#             "properties": {
#                 "name": {"bsonType": "string"},
#                 "age": {"bsonType": "int", "minimum": 18},
#                 "email": {
#                     "bsonType": "string",
#                     "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
#                 },
#             },
#         }
#     }

#     # Enable schema validation for the collection
#     try:
#         collection = db.create_collection(
#             collection_name,
#             validator=schema,
#         )
#         print("Schema validation enabled for collection:")
#     except PyMongoError as e:
#         print(f"Error enabling schema validation: {e}")

#     data = {"name": "John", "age": 30, "email": "john@gmail.com"}
#     collection.insert_one(data)