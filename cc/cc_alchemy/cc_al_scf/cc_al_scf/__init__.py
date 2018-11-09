from sqlalchemy import engine_from_config

#from .models import DBSession
#from cc_al_scf.models import initialize_sql
from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_chameleon')
        config.include('pyramid_bootstrap')
        config.include('.models')
        config.include('.routes')
        config.scan()
    #engine = engine_from_config(settings, 'sqlalchemy.')
    #initialize_sql(engine)
    return config.make_wsgi_app()
