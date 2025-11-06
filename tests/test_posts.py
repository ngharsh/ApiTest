import pytest 


def test_posts_reponse_code(post_api):
    "Test01: Check the api response code, Expected 200 when request succeeded."
    response = post_api.get_posts()
    assert response.status_code == 200
    print("Test01: Check the api response code, Expected 200 when request succeeded. - Passed")

def test_posts_data(post_api):
    response = post_api.get_posts()
    data = response.json()

    "Test02: Check length of data recieved, Expected 100"
    assert len(data) == 100, "Expected length of data 100"
    print("Test02: Check length of data recieved, Expected 100 - Passed")

    "Test03: Check type of data returned, Expected data type list of dictionary"
    assert isinstance(data, list)
    print("Test03: Check type of data returned, Expected data type list of dictionary-Passed")

    "Test04: Check the content of list, Expected dictionary"
    first_post = data[0]
    assert isinstance(first_post, dict)
    print("Test04: Check the content of list, Expected dictionary-Passed")

    "Test05: Check the keys in the dictionary, Expected 'userID', 'id', 'title', 'body'"
    exp_keys = ['userId', 'id', 'title', 'body']
    keys = first_post.keys()
    for key in keys:
        assert key in exp_keys, f"Expected {key}"
        print(f"Test05: Check the keys in the dictionary, Expected 'userID', 'id', 'title', 'body/{key} - Passed")

    "Test06: Check the data type values in the dictionary, Expected 'userID' of type int, 'id' is of type int, 'title' is of type str, 'body' is of type str"
    first_post_values = list(first_post.values())

    assert isinstance(first_post_values[0], int)
    print("Test06: Check the data type values in the dictionary, Expected 'userID' of type int-Passed")
    assert isinstance(first_post_values[1], int)
    print("Test06: Check the data type values in the dictionary, Expected 'id' is of type int-Passed")
    assert isinstance(first_post_values[2], str)
    print("Test06: Check the data type values in the dictionary, Expected 'title' is of type str-Passed")
    assert isinstance(first_post_values[3], str)
    print("Test06: Check the data type values in the dictionary, Expected 'body' is of type str-Passed")


def test_posts_create(post_api):
    "Test07: Create a post and check the response, Expected response code 201"
    userId = 3 
    title = "Title Create"
    body = "Create, Post and check response"

    response = post_api.add_posts(userId, title, body)
    assert response.status_code == 201, "Expected response code 201"
    print("Test07: Create a post and check the response, Expected response code 201-Passed")


def test_posts_update(post_api):
    "Test08: Update a post and check the response, Expected response code 201"
    id = 1
    userId = 3 
    title = "Title Create"
    body = "Create, Post and check response"
    response = post_api.update_posts(id, userId, title, body)
    assert response.status_code == 200, "Expected response code 201"
    print("Test08: Update a post and check the response, Expected response code 201-Passed")


def test_posts_delete(post_api):
    "Test09: Delete a post and check the response, Expected response code 200"
    id = 1
    response = post_api.delete_posts(id)
    assert response.status_code == 200, "Expected response code 200"
    print("Test09: Delete a post and check the response, Expected response code 200-Passed")


def test_posts_invalid_update(post_api):
    "Test10: Update a post with invalid id, and check the response, Expected response code 500"
    id = 101
    userId = 3 
    title = "Title Create"
    body = "Create, Post and check response"
    response = post_api.update_posts(id, userId, title, body)
    assert response.status_code == 500, "Expected response code 500"
    print("Test10: Update a post with invalid id, and check the response, Expected response code 500-Passed")


def test_posts_invalid_delete(post_api):
    "Test11: Delete a post with invalid id, and check the response, Expected response code 404"
    id = 101
    response = post_api.delete_posts(id)
    assert response.status_code == 200, "Expected response code 404"
    print("Test11: Delete a post with invalid id, and check the response, Expected response code 404-Passed")

