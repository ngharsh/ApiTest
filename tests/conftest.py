import pytest 

import utils.post_api as posts

@pytest.fixture(scope="session")
def post_api():
    return posts.Post_Api()