# Create the logging_decorator() function 👇
class User:
    def __init__(self, name):
        self.name = name
        self.logged_in = False

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].logged_in == True:
            function(args[0])
        else:
            print("You are not logged in. ")
    return wrapper

# Use the decorator 👇
@logging_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post. ")

new_user = User("Tony")
new_user.logged_in = True
create_blog_post(new_user)
