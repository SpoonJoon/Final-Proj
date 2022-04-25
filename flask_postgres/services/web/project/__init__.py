from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
CORS(app)

# email


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cs445meetthedockers@gmail.com'
app.config['MAIL_PASSWORD'] = 'cs445pass!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    user_name = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, email, user_name, **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.active = 1
        self.user_name = user_name
        self.password = "placeholder" 


class Articles(db.Model):
    __tablename__ = "articles"
    
    id = db.Column(db.Integer, primary_key=True)
    article_name = db.Column(db.String(256), unique=True, nullable=False)
    article_link = db.Column(db.String(256), unique=True, nullable=False)
    pattern_id = db.Column(db.Integer, db.ForeignKey("patterns.id"))

    def __init__(self, article_name, article_link, pattern_id):
        self.article_name = article_name
        self.article_link = article_link
        self.pattern_id = pattern_id


class Patterns(db.Model):
    __tablename__ = "patterns"
    id = db.Column(db.Integer, primary_key=True)
    pattern_name = db.Column(db.String(64), unique=True, nullable=False)
    # children = db.relationship("Articles", "Problems")
    # How to inherit from multiple tables?

    def __init__(self, pattern_name):
        self.pattern_name = pattern_name


class Problems(db.Model):
    __tablename__ = "problems"
    id = db.Column(db.Integer, primary_key=True)
    problem_name = db.Column(db.String(128), unique=True, nullable=False)
    problem_link = db.Column(db.String(256), unique=True, nullable=False)
    pattern_id = db.Column(db.Integer, db.ForeignKey("patterns.id"))
    difficulty_level = db.Column(db.Integer, nullable=False)

    def __init(self, problem_name, problem_link, pattern_id, difficulty_level):
        self.problem_name = problem_name
        self.problem_link = problem_link
        self.pattern_id = pattern_id
        self.difficulty_level = difficulty_level


@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route("/make_user", methods=['GET','POST'])
def make_user():
    if request.method == 'GET':
        return render_template("make_user.html", users=User.query.all())
    if request.method == 'POST': 
        data = request.form
        new_user = User(email=data["email"],user_name=data["name"])
        db.session.add(new_user)
        db.session.commit()
        return {"message": f"user {new_user.email} has been added!"}



@app.route("/email", methods=['GET'])
def email():
    msg = Message("test email subject",
            sender="cs445meetthedockers@gmail.com",
            recipients=["cs445meetthedockers@gmail.com"])
    msg.body = "test email body"
    mail.send(msg)
    return "Message Sent!"
