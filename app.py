from flask import Flask
from flask_mysqldb import MySQL
from Config import Config
from Routes import loadRouters
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# blueprint
app.config.from_object(Config) 
mysql = MySQL(app)

app.mysql = mysql    
loadRouters(app)

# app.run(debug=True, port=5000, host="0.0.0.0")
