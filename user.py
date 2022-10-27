import requests

# print(dir(requests))

API_HOST = 'https://reqres.in'


def get_all_users():
    print("Getting all the users")
    response = requests.get(API_HOST + '/api/users')
    print("Response status code: ", response)
    print("Response: ", response.json())
    return response.json()

# get_all_users()


def create_user(user_data):
    print("Creating a new user with values: ", user_data)
    response = requests.post(API_HOST+ '/api/users', json=user_data)
    print("Response status code: ", response)
    print("Response: ", response.json())
    return response.json()

# create_user({"name": "vamsi", "job":"software engineer"})
# create_user({"name": "elon", "job":"ceo"})


def delete_user(user_id):
    print("Deleting user with id: ", user_id)
    response = requests.delete(API_HOST + "/api/users/"+str(user_id))
    print("Response status code: ", response)    
    return True

# delete_user(5)




