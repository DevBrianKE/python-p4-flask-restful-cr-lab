#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():
    Plant.query.delete()

    aloe = Plant(name="Aloe", image="https://example.com/aloe.jpg", price=11.50)
    zz = Plant(name="ZZ Plant", image="https://example.com/zz-plant.jpg", price=25.98)

    db.session.add_all([aloe, zz])
    db.session.commit()
