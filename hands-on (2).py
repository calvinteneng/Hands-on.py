import user



result = user.delete_user(2)
if result == True:
    print("user deleted successfully")
else:
    print("There was an error while deleting the user")