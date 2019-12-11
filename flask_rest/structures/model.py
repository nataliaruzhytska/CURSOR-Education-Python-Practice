from db import db


staff_rooms = db.Table(
    'staff_rooms',
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.staff_id')),
    db.Column('room_id', db.Integer, db.ForeignKey('room.room_id'))
)


class Room(db.Model):
    __tablename__ = 'room'

    room_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    number = db.Column(db.Integer)
    level = db.Column(db.String)
    status = db.Column(db.String)
    price = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.tenant_id'))


class Tenant(db.Model):
    __tablename__ = 'tenant'

    tenant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    passport_id = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.String)
    rooms = db.relationship('Room', backref='tenant')


class Staff(db.Model):
    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    passport_id = db.Column(db.String)
    position = db.Column(db.String)
    salary = db.Column(db.Integer)
    rooms = db.relationship('Room', secondary=staff_rooms, backref=db.backref('staff'))
