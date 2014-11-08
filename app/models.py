from app import db

class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    chosen = db.Column(db.Boolean())
    has_chosen = db.Column(db.Boolean())

    @classmethod
    def member_exists(cls, name):
        if cls.query.filter(cls.name == name).first() is None:
            return False
        else:
            return True

    @classmethod
    def check_has_chosen(cls, name):
        member = cls.query.filter(cls.name == name).first()
        if member.has_chosen:
            return True
        else:
            return False

    @classmethod
    def get_all_not_chosen(cls):
        return cls.query.filter(cls.has_chosen == False).all()

    @classmethod
    def get_all_members(cls):
        return cls.query.all()

    @classmethod
    def get_all_available_members(cls, name):
        return (cls.query
                .filter(cls.chosen == False)
                .filter(cls.name != name)
                .all())

    @classmethod
    def get_member_by_name(cls, name):
        return cls.query.filter(cls.name == name).first()

    @classmethod
    def get_count(cls):
        return cls.query.count()
