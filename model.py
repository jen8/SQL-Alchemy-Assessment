"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Car model."""

    __tablename__ = 'models'
    # id = db.Column(SERIAL PRIMARY KEY)
    # foreign key established to brand table to link tables together
    # if a table that has a single matching row in the second table, 
    # the first table has foreign key
    id = db.Column(autoincrement=True, 
                   primary_key=True)
    year = db.Column(db.INTEGER, nullable=False)
    # brand_name doesn't need type, it uses the type from brands.name?
    brand_name = db.Column(db.ForeignKey('brands.name'),nullable=False)
    # nullable = False should be place as last item in parentheses
    name = db.Column(db.VARCHAR(50), nullable=False)
    # establish relationship between models and brands table 
    brand = db.relationship('Brand', backref='models')

    def __repr__(self):
        """Show info about car model."""

        return '<Model id=%s year=%s brand_name=%s name=%s>' % (
            self.id, self.year, self.brand_name, self.name)



class Brand(db.Model):
    """Car brand."""

    __tablename__ = 'brands'
    # id = db.Column(SERIAL PRIMARY KEY)
    id = db.Column(autoincrement=True,
                   primary_key=True)
    name = db.Column(db.VARCHAR(50), nullable=False)
    founded = db.Column(db.INTEGER)
    headquarters = db.Column(db.VARCHAR(50))
    discontinued = db.Column(db.INTEGER)

    # establish relationship between models and brands table 
    model = db.relationship('Model', backref='brands')

    def __repr__(self):
        """Show info about car brand."""

        return '<Brand id=%s name=%s founded=%s headquarters=%s, discontinued=%s>' % (self.id, self.name, self.founded, self.headquarters, self.discontinued)


# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
