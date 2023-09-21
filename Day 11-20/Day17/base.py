class User:
    def __init__(self, user_id, name, followers):
        print("New user created!!")
        self.id = user_id
        self.username = name
        self.followers = followers

    def follow(self, user):
        user.followers += self.followers
        self.followers += user.followers


user_1 = User("001", "Dharmesh", 100)
user_2 = User("002", "SugarDaddy", 1000)
print(user_1.id)
user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)