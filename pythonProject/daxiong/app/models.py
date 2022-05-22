from app import db
from datetime import datetime

class Course(db.Model):
    productId = db.Column(db.Integer,primary_key=True,nullable=False)
    courseId= db.Column(db.Integer,nullable=False)
    productName = db.Column(db.String(125), nullable=False)
    productType = db.Column(db.Integer, nullable=False)
    provider = db.Column(db.String(125), nullable=False)
    score = db.Column(db.Float(2))
    scoreLevel = db.Column(db.Integer)
    learnerCount = db.Column(db.Integer)
    couponPrice = db.Column(db.Float(2))
    lessonCount = db.Column(db.Integer)
    originalPrice = db.Column(db.Float(2))
    discountPrice = db.Column(db.Float(2))
    vipPrice = db.Column(db.Float(2))
    imgUrl = db.Column(db.String(125))
    bigImgUrl = db.Column(db.String(125))
    description = db.Column(db.Text)

class Sale(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True,nullable=False)
    productId = db.Column(db.Integer,db.ForeignKey('course.productId'))
    productName = db.Column(db.String(125),nullable=False)
    learnerCount = db.Column(db.Integer)
    create_time = db.Column(db.Date,default=datetime.today())
    #关联关系
    course = db.relationship('Course',backref=db.backref('sale',lazy='dynamic'))