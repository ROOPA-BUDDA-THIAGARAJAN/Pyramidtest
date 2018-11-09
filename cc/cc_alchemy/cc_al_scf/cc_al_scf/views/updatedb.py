"""from ..models import session_factory
import zope.sqlalchemy

DBSession = session_factory()
zope.sqlalchemy.register(
        DBSession, transaction_manager=transaction_manager)

"""
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))

"""import zope.sqlalchemy

dbsession = session_factory()
zope.sqlalchemy.register(
        dbsession, transaction_manager=transaction_manager)

def adduser(dbsession,user_dict):
    """
    #Add or update models / fixtures in the database.

"""
    # model = models.mymodel.MyModel(name='one', value=1)
    # dbsession.add(model)
    def_dict = {'fname' : 'xxx','lname' : 'yyy',
    'pword': 'dummypwd', 'email' : 'email@dummy.com', 'contact' : 000000000,
    'cname' : 'company_name','curl' : 'www.comp_url.com','al1' : 'addline1',
    'al2' : 'addline2','city' : 'dummy_city','state' :'dummy_state',
    'country' : 'dummy_country','zip' : 999999}
    user_dict = default_dict(def_dict)

    model = models.mymodel.UserInfo(first_name =user_dict['fname'],
                                    last_name = user_dict['name'],
                                    password = user_dict['pword'],
                                    email = user_dict['email'],
                                    contact = user_dict['contact'],
                                    company_name = user_dict['cname'],
                                    company_url = user_dict['curl'],
                                    addline1 = user_dict['al1'],
                                    addline2 = user_dict['al2'],
                                    city = user_dict['city'],
                                    state = user_dict['state'],
                                    country = user_dict['country'],
                                    zipcode = user_dict['zip'],
                                    )
#dbsession.add(model)
"""
