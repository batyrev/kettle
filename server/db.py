from app import app
from flask_sqlalchemy import SQLAlchemy
from kettle import ElectricKettle
from datetime import datetime

db = SQLAlchemy(app)

class States(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    boiling_time = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    max_water_amount = db.Column(db.Float, nullable=False)
    min_water_amount = db.Column(db.Float, nullable=False)
    water_amount = db.Column(db.Float, nullable=False)
    is_on = db.Column(db.Boolean, nullable=False)

def create_state(kettle: ElectricKettle):
    state =  States(date=datetime.now(),
                    boiling_time=kettle.boiling_time,
                    temperature=kettle.temperature,
                    max_water_amount=kettle.max_water_amount,
                    min_water_amount=kettle.min_water_amount,
                    water_amount=kettle.water_amount,
                    is_on=kettle.is_on)
    with app.app_context():
        db.session.add(state)
        db.session.commit()

def get_last_state():
    with app.app_context():
        return States.query.order_by(States.id.desc()).first()

def get_all_states():
    with app.app_context():
        return States.query.all()