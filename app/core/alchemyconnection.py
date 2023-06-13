from _typeshed import Incomplete
from flask_sqlalchemy import SQLAlchemy

class ALCHCONN(SQLAlchemy):
    
    def __init__(self, app: Incomplete | None = None, use_native_unicode: bool = True, session_options: Incomplete | None = None, metadata: Incomplete | None = None, query_class=..., model_class=..., engine_options: Incomplete | None = None) -> None:
        super().__init__(app, use_native_unicode, session_options, metadata, query_class, model_class, engine_options)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()