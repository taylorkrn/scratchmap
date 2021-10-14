from scratchmap import db, login_manager
from flask import current_app
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

#How we load a user from a user ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#User Model, uniquely defined by the user.id
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #max length is 20
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #relationship is not a cloumn - backref 'adds column' to the Post Model
    posts = db.relationship('Scratched_Map', backref='author', lazy=True)

    #Getting a reset token to reset the users password
    def get_reset_token(self, expires_seconds=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_seconds)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    #Static Method to verify the reset token
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    #Print representation of a user
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


#The Scratch Map model, uniquely defined by map.id
#Each map has a specific User and a specific map_type (Map_Type model still needs to be defined)
class Scratched_Map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map_type = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    #visited = db.Column()
    #wish_list = db.Column()
    #images = db.Column()

    #Notice lower case 'u' in user.id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # map_id = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=False)

    def __repr__(self):
        return f"Scratched_Map('{self.title}', '{self.date_posted}')"




# country_association_table = Table('association', db.Model.metadata,
#     Column('map_id', Integer, ForeignKey('map.id')),
#     Column('country_id', Integer, ForeignKey('country.id'))
# )

# class Map(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     num_instances = db.Column(db.Integer)

#     s_maps = db.relationship('Scratched_Map', backref='map_id', lazy=True)

#     countries = relationship("Country", secondary=country_association_table)

#     def __repr__(self):
#         return f"Map('{self.title}', '{self.id}')"

# class Country(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)



