import utils.api as utility
import config.settings as config

class Post_Api:

    base_url = config.url
    endpoint = config.post_url 

    api_utility = utility.Api(base_url)

    def get_posts(self):
        return self.api_utility.get(self.endpoint)
    
    def add_posts(self, userId, title, body):
        data = {
        "userId" : userId,
        "title" : title,
        "body" : body }

        return self.api_utility.post(self.endpoint, data)
    
    def update_posts(self, post_id, userId, title, body):
        data = {
        "userId" : userId,
        "title" : title,
        "body" : body }

        endpoint = self.endpoint + "/" + str(post_id)
        return self.api_utility.update(endpoint, data)
    
    def delete_posts(self, post_id):
        return self.api_utility.delete(self.endpoint, post_id)


