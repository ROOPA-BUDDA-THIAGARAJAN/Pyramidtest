def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login','/login')
    config.add_route('signup', '/signup')    
    config.add_route('userlogin', '/userlogin')
    config.add_route('checkregistration', '/checkregistration')
    config.add_route('login_auth','/login_auth')
    config.add_route('logout','/logout')
