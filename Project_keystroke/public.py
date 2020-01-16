from flask import *
from db import *

public=Blueprint("public",__name__)
@public.route('/',methods=['post','get'])
def home():
	return render_template("publichome.html")
@public.route('/login',methods=['post','get'])
def login():
	if 'submit'in request.form:
		uname=request.form['Username']
		pwd=request.form['Password']
		q="select * from login where username='%s' and password='%s'"%(uname,pwd)
		print(q)
		res=select(q)
		if res:
			if res[0]['type']=="admin":
				return redirect(url_for('admin.adminhome'))
	return render_template("login.html")