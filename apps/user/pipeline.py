from .models import UserProfile

# Custom from: https://stackoverflow.com/a/65417707/11806074
# https://developers.facebook.com/docs/graph-api/reference/user/
def get_img_url(backend, user, response, details, is_new=False, *args, **kwargs):
    if backend.name == "facebook":
        # Get the profile picture URL
        imageUrl='https://graph.facebook.com/{0}/picture/?type=large&access_token={1}'.format(response['id'],response['access_token'])
        # Update user profile
        profile = UserProfile.objects.get(user=user)
        profile.firstname = user.first_name
        profile.lastname = user.last_name
        profile.profile_url = imageUrl
        profile.save()

        # https://stackoverflow.com/a/50364673/11806074
        user.email = response.get('email', None)
        user.save()
    detail = backend.get_user_details(response)
    # print(response.get('email', None))