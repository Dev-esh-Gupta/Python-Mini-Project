class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.user = username
        self.followers = 0
        self.following = 0
        # print("New user created !...")

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Devesh")
# user_1.id = "001"
# user_1.username = "Devesh"

print(user_1.id)
print(user_1.user)
print(user_1.followers)

user_2 = User("002","Pranjal")
print(user_2.user)

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)

print(user_2.followers)
print(user_2.following)


