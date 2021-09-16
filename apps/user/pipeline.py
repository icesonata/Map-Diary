# Custom from: https://stackoverflow.com/a/65417707/11806074
def get_img_url(backend, user, response, is_new=False, *args, **kwargs):
    if backend.name == "facebook":
        # The main part is how to get the profile picture URL and then do what you need to do
        imageUrl='https://graph.facebook.com/{0}/picture/?type=large&access_token={1}'.format(response['id'],response['access_token'])