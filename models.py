# from email.policy import default
# from tkinter import Y
# from zlib import DEF_BUF_SIZE
from flask_sqlalchemy import SQLAlchemy





db =  SQLAlchemy()


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    artists = db.relationship('Artist', secondary='shows')
    shows = db.relationship('Show', backref=('venues'))

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.city,
            'state':self.state,
            'address':self.address,
            'phone':self.phone,
            'image_link':self.image_link,
            'facebook_link': self.facebook_link,
            'website_link': self.website_link,
            'seeking_venue':self.seeking_venue,
            'seeking_description':self.seeking_description,

        }

    def __repr__(self):
        return f'<Venue {self.id} {self.name}>'


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description =db.Column(db.String(500))
    venue = db.relationship('Venue', secondary='shows')
    shows = db.relationship('Show', backref=('artist'))

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.city,
            'state':self.state,
            'address':self.address,
            'phone':self.phone,
            'image_link':self.image_link,
            'facebook_link': self.facebook_link,
            'website_link': self.website_link,
            'seeking_venue':self.seeking_venue,
            'seeking_description':self.seeking_description,

        }

    def __repr__(self):
        return f'<Artist {self.id} {self.name}>'


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    venue_id =db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    start_time =db.Column(db.DateTime, nullable=False)

    venue = db.relationship('Venue')
    artist = db.relationship('Artist')

    def show_artist(self):
        return {
            'artist_id':self.artist_id,
            'artist_name':self.artist.name,
            'artist_image_link': self.artist.image_link,
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M:%S')
        }

    def show_venue(self):
        return{
            'venue_id':self.venue_id,
            'venue_name': self.venue_name,
            'venue_image_link': self.venue.image_link,
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M:%S')

        }


db.create_all()

    



