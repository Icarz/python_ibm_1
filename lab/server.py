from flask import Flask #importing flask
app = Flask(__name__) #creating route



@app.route('/') #using the route for home page

#creating a message in the home page ti see if it's working!!
def home():
      return "Hello World"