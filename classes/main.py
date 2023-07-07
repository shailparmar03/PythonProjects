class User:  # PascalCase     camelCase    snake_case
    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user): # self -> it knows the object that called it
        user.followers+=1
        self.following+=1


user_1 = User("001", "Shail")
# user_1.id="001"
# user_1.name="Shail"
user_2=User("002", "Gwen")
user_1.follow(user_2)
print(user_1.following, user_1.followers)
print(user_2.following, user_2.followers)
