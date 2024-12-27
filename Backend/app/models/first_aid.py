from app.db import db

class FirstAidGuide(db.Model):
    """Model to store first aid guide information"""
    __tablename__ = 'first_aid_guide'

    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    treatment = db.Column(db.Text, nullable=True)

    def __init__(self, query, description=None, treatment=None):
        self.query = query
        self.description = description
        self.treatment = treatment

    def __repr__(self):
        return f"<FirstAidGuide {self.query}>"
