from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "e738627c08889a6b3d91a0c43acd6a16"
app.config["SQLAlCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from movieblog import routes
