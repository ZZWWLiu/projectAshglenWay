import re
from signup.models import User

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{8,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

def exist_username(username):
	try:
		u = User.objects.get(username = username)
	except User.DoesNotExist:
		return False
	else:
		return True
