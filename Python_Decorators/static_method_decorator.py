class User:
    @staticmethod
    def length_username(username):
        return len(username) < 10 and username.endswith('man')

print(User.length_username("superman"))
print(User.length_username("superboy"))
print(User.length_username("super-superboy"))
