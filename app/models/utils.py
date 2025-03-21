from app import db


class ModelMixin(object):
    """Class Mixin"""
    def save(self):
        """Function to save object"""
        db.session.add(self)
        db.session.commit()
        return self
