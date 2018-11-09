
import transaction

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

#from transaction import commit

from .. import models #import mymodel
from ..models import mymodel
from pyramid.renderers import render_to_response
#from .updatedb import adduser
from pyramid.compat import escape
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError

engine = create_engine('postgresql://postgres:password@localhost:5432/pyramid_db')
mymodel.Base.metadata.create_all(engine)
mymodel.DBSession.configure(bind=engine)


@view_config(route_name = 'login_auth',renderer = 'json')
def login_auth(request):
	data = request.POST
	print("printing login auth data here",data)
	email = data['email']
	pwd = data['pwd']
	auth = mymodel.DBSession.query(models.mymodel.UserInfo).filter(and_(models.mymodel.UserInfo.email.like(email), models.mymodel.UserInfo.password.like(pwd))).first()
	print("length of the query login is ", len(auth))
	#email_exists = mymodel.DBSession.query(models.mymodel.UserInfo).filter(models.mymodel.UserInfo.email == email).all()
	#if(len(auth)>1):
	#	pwd = mymodel.DBSession.query(models.mymodel.UserInfo).filter(models.mymodel.UserInfo.email == email).all()
	exist = (len(auth)!=0)
	print(exists)
	return {
	state: success
	}


@view_config(route_name='login', renderer = '../templates/login.pt')
def login(request):
	
	return {'title' : 'Login Here'}

@view_config(route_name='userlogin')#, renderer = '../templates/home.pt')
def userlogin(request):
	print("printing request here")	
	print(request.POST)
	#print(request.POST['emailid'])
	try:
		if(request.POST['fname']):
			post_data = request.POST	
			fname = post_data['fname']
			lname = post_data['lname']
			email = post_data['email']
			pword = post_data['pword']
			contact = post_data['contact']
			cname = post_data['cname']
			curl = post_data['curl']
			al1 = post_data['al1']
			al2 = post_data['al2']
			city = post_data['city']
			state = post_data['state']
			country = post_data['country']
			zipcode = post_data['zip']
			print("first name is ",fname)
			print("last name is ",lname)
			print("emailid is ",email)
			print("password is ",pword)
			print("printed request")
			# 2 code to check for user in DB goes here
			
			# 1 add data to DB from here --done
			data = models.mymodel.UserInfo(fname,lname,pword,email,contact,cname,curl,al1,al2,city,state,country,zipcode)
			print(dir(data))
			
			with transaction.manager:
				mymodel.DBSession.add(data)
			# Add role data here W.R.T the email id provided domain
			domain = email.split('@')[1]
			print("domain is ",domain)
			if domain == "rapidvaluesolutions.com":
				role = "admin"
			else :
				role = "generic"
			role_data = models.mymodel.UserRoles(email, role)
			print(role_data)

			with transaction.manager:
				mymodel.DBSession.add(role_data)
			

			#transaction.commit()
			#DBSession.commit()
			print("commited data fromouser code goes here!!!")
			#adduser(dbsession, post_data)
			if(role == 'generic'):
				return render_to_response(renderer_name = '../templates/home.pt',
			                          value = {
			                          'first' : "fname",
			                          'last' : "lname"
			                          })
			else:
				return render_to_response(renderer_name = '../templates/admin.pt',
			                          value = {
			                          'first' : "admin",
			                          'last' : "user"
			                          })
		"""else:
			print("data from login page here")
			return {'first' : "fname",'last' : "lname"}"""
	except Exception as e:
		print("printing exception here",e)
		#if('fname' == e):
		print("data from login page here")
		print(request)
		print("printing request .POST")
		print(request.POST)
		email = request.POST['emailid']# exxception here......
		pwd = request.POST['password']
		cred_exists = mymodel.DBSession.query(models.mymodel.UserInfo).filter(and_(models.mymodel.UserInfo.email == email,models.mymodel.UserInfo.password == pwd)).all()
		print(len(cred_exists))
		if(len(cred_exists)>=1):
			# user credentaila exsts here , henc login
			# get data from DB here.
			# print(cred_exists)
			# print(cred_exists[0].first_name)
			# print(cred_exists[0].last_name)
			return { 'first': cred_exists[0].first_name, 'last': cred_exists[0].last_name}
		else:
			print("incorect credentials")
			render_to_response('../templates/login.pt',
                              {'alert': 'credentials invalid',
                              'title' : 'Login Here'},
                              request=request)

			
	

@view_config(route_name = 'checkregistration', renderer = 'json')
def checkregistration(request):
	email = request.POST["email"]
	print(email)
	if(email!= ""):
		# query here
		# db.session.query(db.exists().where(UserInfo.email == email)).scalar()
		# pyramid data query here
		try:
			email_exists = mymodel.DBSession.query(models.mymodel.UserInfo).filter(models.mymodel.UserInfo.email == email).all()
			print(len(email_exists))
			exists = (len(email_exists)!=0)
			print(exists)
			if(exists>=1):
				print("printing error here")
				return {'error' : 'User already exists'}
			else:
				print("printing vald user here")
				return {'state' : 'User name valid'}
			#print("tha new op is ",email_exists)			
		
		except Exception as e:
			print("printing exception here")
			print(e)
			print("Above is the exception")
			
			exists = (len(email_exists)!=0)
			if(exists):
				print("tha new op is ",email_exists)
				return {'error' : 'User already exists'}
			else:
				return {'state' : 'User name valid'}


@view_config(route_name = 'signup',renderer = '../templates/register.pt')
def register(request):	
	return {'page' : 'Registration Page'}
"""
@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'cc_al_scf'}

"""
db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
@view_config(route_name='logout', renderer = '../templates/login.pt')
def logout(request):
	# create alert for signout
	# 
	return {'title' : 'Login Here'}

