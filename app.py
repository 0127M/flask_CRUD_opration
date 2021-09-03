from myapp import create_app#here we have to import create app
from flask import Flask, render_template# below we will create the route
import os


config_name=os.getenv('FLASK_CONFIG','development')
app=create_app(config_name)




if __name__=="__main__":
    app.run(debug=True,port=5001)