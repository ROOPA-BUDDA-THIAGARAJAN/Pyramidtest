from pyramid.view import view_config


@view_config(route_name='login', renderer = 'templates/login.pt')
def login(request):
	return {}

@view_config(route_name = 'userlogin', renderer = 'templates/userlogin.pt')
def userlogin(request):
	# write code to check if user exists
	return {}

@view_config(route_name = 'signup', renderer = 'templates/register.pt')
def signup(request):
	return {}
