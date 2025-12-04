# create_tables.py
import os
from app import app, db  # ensure 'app.py' exports app and db correctly
from sqlalchemy import inspect

with app.app_context():
    # ensure instance directory exists (defensive)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    instance_dir = os.path.join(base_dir, "instance")
    os.makedirs(instance_dir, exist_ok=True)

    db.create_all()
    db.session.commit()
    print("Tables created successfully!")

    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print("Tables in the database:", tables)
