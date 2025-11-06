import pytest 

import utils.api as utility
from utils.post_api import Post_Api
import config.settings as config

post_api = Post_Api()

response = post_api.get_posts()
data = response.json()

print("Post Response:", response)

print("Post length:", len(data))

print("First Post:", data[0])

print("Post Type:", type(data))

print("Type First data:", type(data[0]))

print("Keys in data:", data[0].keys())

print("Values in data", data[0].values())

print("Values in data", type(data[0].values()))

for value in data[0].values():
    print(f"Dict Item {value} Type: {type(value)}")

#create post
post_response = post_api.add_posts(1,"markus", "unt aut facere repellat provident occaecati excepturi")
print("Post Response:", post_response)
data = post_response.json()
print("New Data:", data)

#update
post_response = post_api.update_posts(101, 1, 3, "unt aut facere repellat provident occaecati excepturi")
print("Post Response:", post_response)
print(post_response.text)
# data = post_response.json()
# print("Updated Data:", data)

#delete
post_response = post_api.delete_posts(1)
print("Delete Response:", post_response)
print(post_response.text)
data = post_response.json()
print("Deleted Data:", data)

#Invalid
base_url = config.url
test_api = utility.Api(base_url)
test_response = test_api.get("testing")

print("Base URL:", base_url)
test_response_post = test_api.get("posts")
print("Test API response:", test_response)
print("Test API response post:", test_response_post)

test_z_t = "posts?_start=900&_limit=1000"
test_response_z = test_api.get(test_z_t)
print("Length of data:", len(test_response_z.json()))


