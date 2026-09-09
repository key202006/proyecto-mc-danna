from flask import Flask
from flask_mysqldb import MySQL
from Config import Config
from dotenv import load_dotenv
from Routes import loadRoutes

load_dotenv()

app = Flask(__name__)
# blueprint
app.config.from_object(Config) 
mysql = MySQL(app)

app.mysql = mysql
loadRoutes(app)

if __name__ == '__main__':
  app.run(debug=True, port=5000, host="0.0.0.0")
