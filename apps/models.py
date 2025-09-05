
from apps.app import db 

class domestic_publication(db.Model):
    __tablename__ = "domestic_publications"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False)
    authors = db.Column(db.String(500), nullable = False)
    reference = db.Column(db.String(500), nullable = False)



class aboard_publication(db.Model):
    __tablename__ = "aboard_publications"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False)
    authors = db.Column(db.String(500), nullable = False)
    reference = db.Column(db.String(500), nullable = False)


class domestic_conference(db.Model):
    __tablename__ = "domestic_conference"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False)
    conference_name = db.Column(db.String(500), nullable = False)
    date = db.Column(db.String(500), nullable = False)


class aboard_conference(db.Model):
    __tablename__ = "aboard_conference"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False)
    conference_name = db.Column(db.String(500), nullable = False)
    date = db.Column(db.String(500), nullable = False)


class member_spec(db.Model):
     __tablename__ = "memberspec"
     id = db.Column(db.Integer, primary_key = True)
     member = db.Column(db.String(500), nullable = False)
     people = db.Column(db.String(500), nullable = False)
     title = db.Column(db.String(500), nullable = False)
     organi = db.Column(db.String(500), nullable = False)
     date = db.Column(db.String(500), nullable = False)
     price = db.Column(db.String(500), nullable = True)


class present_member(db.Model):
    __tablename__ = "present_member"
    id = db.Column(db.Integer, primary_key = True)
    member = db.Column(db.String(500), nullable = False)
    profile_image = db.Column(db.String(255), nullable=False, default='default.jpg')
    degree = db.Column(db.String(500), nullable = False)
    department = db.Column(db.String(500), nullable = False)
    email = db.Column(db.String(500), nullable = False)
    interest_part = db.Column(db.String(500), nullable = False)


class past_member(db.Model):
    __tablename__ = "past_member"
    id = db.Column(db.Integer, primary_key = True)
    member = db.Column(db.String(500), nullable = False)
    profile_image = db.Column(db.String(255), nullable=False, default='default.jpg')
    degree = db.Column(db.String(500), nullable = False)
    department = db.Column(db.String(500), nullable = False)
    email = db.Column(db.String(500), nullable = False)
    affiliation = db.Column(db.String(500), nullable = False)

class home_content(db.Model):
    __tablename__ = "home_content"
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(500), nullable = False)
    title = db.Column(db.String(500), nullable = False)
    content = db.Column(db.String(500), nullable = False)

class activity_photo(db.Model):
    __tablename__ = "activity_photo"    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False)
    date = db.Column(db.String(500), nullable = False)
    activity_image = db.Column(db.String(255), nullable=False, default='default.jpg')
    people = db.Column(db.String(500), nullable = False)
    venue = db.Column(db.String(500), nullable = False)