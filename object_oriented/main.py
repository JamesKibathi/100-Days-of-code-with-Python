from user import User
from post import Post

user_james = User("njenga@gmail.com", "James Njenga", "pwd1", "Senior Software Engineer")
user_james.get_user_info()
user_james.change_job_title("Tech Lead")
user_james.get_user_info()

user_two = User("info@novasavannah.com", "Nova Savannah", "super secret", "CTO and Co-founder")
user_two.get_user_info()

new_post = Post("Starting a new position", user_james.name)
new_post.get_post_info()
