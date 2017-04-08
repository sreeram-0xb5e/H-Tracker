from flask import Flask, redirect, url_for, request
app = Flask(__name__)
import mysql.connector as mariadb
import datetime


app = Flask(__name__)



# UTILITY FUNCTIONS

def decode(var):
        if isinstance(var,bytearray):
                return var.decode('utf-8')
        if isinstance(var,datetime.date):
                return str(var)
        if isinstance(var,int):
                return var
        if isinstance(var,str):
                return var
        return

def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], map(decode,row)))
            for row in cursor.fetchall()]


# MAIN FUNCTIONS
@app.route('/')
def index():
	return "Index Page"


@app.route('/update',methods = ['POST'])
def add_into_db():

	#Database Connection

	mariadb_connection = mariadb.connect(host="localhost",user='root', password='lugia', database='t1')
	cursor = mariadb_connection.cursor(prepared = True)
	cursor.execute("SELECT COUNT(id) FROM t1")
	cp = dictfetchall(cursor)
	cursor.close()
	n = str((cp[0]['COUNT(id)']))

	#getting post requests
	print(request.form)
	print("ADFAD")
	url = str(request.form['url'])
	time = (request.form['time'])
	tabid = (request.form['tabid'])
	return str(url)


if __name__ == '__main__':
	app.run(debug = True )
