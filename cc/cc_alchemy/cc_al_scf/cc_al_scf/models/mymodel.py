from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    ForeignKey
)

from .meta import Base
  
import zope.sqlalchemy

from sqlalchemy import engine_from_config
from sqlalchemy.orm import configure_mappers
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

# import or define all models here to ensure they are attached to the
# Base.metadata prior to any initialization routines

# from .mymodel import MyModel  # flake8: noqa
# from .mymodel import UserInfo

# run configure_mappers after defining all of the models to ensure
# all relationships can be setup
configure_mappers()


def get_engine(settings, prefix='sqlalchemy.'):
    return engine_from_config(settings, prefix)


def get_session_factory(engine):
    factory = sessionmaker()
    factory.configure(bind=engine)
    return factory


def get_tm_session(session_factory, transaction_manager):
    """
    Get a ``sqlalchemy.orm.Session`` instance backed by a transaction.

    This function will hook the session to the transaction manager which
    will take care of committing any changes.

    - When using pyramid_tm it will automatically be committed or aborted
      depending on whether an exception is raised.

    - When using scripts you should wrap the session in a manager yourself.
      For example::

          import transaction

          engine = get_engine(settings)
          session_factory = get_session_factory(engine)
          with transaction.manager:
              dbsession = get_tm_session(session_factory, transaction.manager)

    """
    dbsession = session_factory()
    zope.sqlalchemy.register(
        dbsession, transaction_manager=transaction_manager)
    return dbsession


def includeme(config):
    """
    Initialize the model for a Pyramid app.

    Activate this setup using ``config.include('cc_al_scf.models')``.

    """
    settings = config.get_settings()
    settings['tm.manager_hook'] = 'pyramid_tm.explicit_manager'

    # use pyramid_tm to hook the transaction lifecycle to the request
    config.include('pyramid_tm')

    # use pyramid_retry to retry a request when transient exceptions occur
    config.include('pyramid_retry')

    session_factory = get_session_factory(get_engine(settings))
    config.registry['dbsession_factory'] = session_factory

    # make request.dbsession available for use in Pyramid
    config.add_request_method(
        # r.tm is the transaction manager used by pyramid_tm
        lambda r: get_tm_session(session_factory, r.tm),
        'dbsession',
        reify=True
    )
  
"""
class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


Index('my_index', MyModel.name, unique=True, mysql_length=255)
"""
class UserInfo(Base):
    __tablename__ = 'user_info'  
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)    
    email = Column(Text, primary_key = True)
    contact = Column(Integer)
    company_name = Column(Text)
    company_url = Column(Text)
    addline1 = Column(Text)
    addline2 = Column(Text)
    city = Column(Text)
    state = Column(Text)
    country = Column(Text)
    zipcode = Column(Integer)

    def __init__(self,first_name,last_name,password,email,
                 contact = 000000000,
                 company_name = 'company_name',
                 company_url = 'www.comp_url.com',
                 addline1 = 'addline1',
                 addline2 = 'addline2',
                 city = 'dummy_city',
                 state = 'dummy_state',
                 country = 'dummy_country',
                 zipcode = 999999):

        self.first_name = first_name ,
        self.last_name = last_name ,
        self.password = password ,
        self.email = email ,
        self.contact = contact ,
        self.company_name = company_name ,
        self.company_url = company_url ,
        self.addline1 = addline1 ,
        self.addline2 = addline2 ,
        self.city = city ,
        self.state = state ,
        self.country = country ,
        self.zipcode = zipcode
        
     
class UserRoles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)  
    email = Column(ForeignKey('user_info.email',ondelete='CASCADE'),nullable=False)
    role = Column(Text, nullable=False)  
    user = relationship('UserInfo') 

    def __init__(self, email, role):
        self.email = email
        self.role = role

