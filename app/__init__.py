from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = "REF42@$$#5ggfI&*TGI%&*F"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app)
login  = LoginManager(app)


cloudinary.config(
    cloud_name = "dqtk7akkz",
    api_key = "175943162423538",
    api_secret = "<your_api_secret>", # Click 'View API Keys' above to copy your API secret
    secure=True
)