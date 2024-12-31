from app import db
from datetime import datetime

class SymptomCard(db.Model):
    __tablename__ = 'symptom_cards'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    symptoms = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<SymptomCard {self.id} - {self.symptoms}>"
