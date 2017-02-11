learn from /flask/README.md
          /flask/project5.py
          /flask/templates/login.html

Add some security to the applicaiton and publish it on the internet.
Use Google+ and Facebook Sign_in

Knowledge required:
Python, Flask web development framework, JavaScript,
using JQuery to make Ajax calls

**Web Security**

Difference of authentication and authorization

flow of information for security.

Google's OAuth features (in Google OAuth2 playground)

Implement logins and logouts

Secure menu pages

Create a local permission system

Protect the data of each user


Auth Flow: client, server, OAuth provider

Google has changed the user interface for obtaining OAuth credentials since this video was created. The functionality is the same, but the appearance is somewhat different from what's depicted here.

Go to your app's page in the Google APIs Console — https://console.developers.google.com/apis
Choose Credentials from the menu on the left.
Create an OAuth Client ID.
This will require you to configure the consent screen, with the same choices as in the video.
When you're presented with a list of application types, choose Web application.
You can then set the authorized JavaScript origins, with the same settings as in the video.
You will then be able to get the client ID and client secret.

**Remember to type in your original URI and redirect URIs**
