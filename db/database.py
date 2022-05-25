import os
import datetime
import pymongo

client = pymongo.MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client['test']

pets = db['pets']
owners = db['owners']
owns = db['owns']

results = pets.find({'name': 'Fluffy'})
for result in results: print(result)

# Necessary attributes: pet_id, pet_name, species, owner_id (foreign key)
# Additional attributes: sex, dob, breed, color, location
# TODO: Fix date added syntax error
def add_pet(pet_id, pet_name, species, owner_id, sex, dob, breed, color, location):
    document = {
        'Pet ID': pet_id,
        'Pet Name': pet_name,
        'Species (Cat/Dog)': species,
        'Owner ID': owner_id,
        'Date Added': date_added,
        'Sex (M/F)': sex,
        'Date of Birth': dob,
        'Breed': breed,
        'Color/Pattern': color,
        'Location': location
        #'Date Added': datetime.datetime.now()
    }

# TODO: Fix date added syntax error
def add_owner(owner_id, first_name, last_name, dob): 
    document = {
        'Owner ID': owner_id,
        'First Name': first_name,
        'Last Name': last_name,
        'Date of Birth': dob
        #'Date Added': datetime.datetime.now()
    }

# add_ownership: sets relationship between pets and owners
# -- multi_owner bool indicates whether the pet has more than one owner_id
# -- Owner to pets: One to Many, Owner to Pets with multi_owner = True: Many to Many
# TODO: Fix date added syntax error
# TODO: add bool multi_owner
def add_ownership(pet_id, owner_id):
    document = {
        'Pet ID': pet_id,
        'Owner ID': owner_id
        #'Date Added': datetime.datetime.now()
    }
   
    # TODO: Frontend option to add multiple owners
    # False by default
    # multi_owner = False

# Pet ID format - P0000
# Owner ID format - U0000
pet = add_pet('P0001', 'Marco', 'cat', 'U0001')