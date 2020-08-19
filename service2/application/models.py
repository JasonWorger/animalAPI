from application import db
#db is animaldb
#export DATABASE_URI=mysql+pymysql://root:root@35.246.58.237:3306/animaldb
#export SECRET_KEY=afgjkajfbajkbcwabkfhjgakjhfkjahckjabwuhgfbiuawgf

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal = db.Column(db.String(30), nullable=False)
    noise = db.Column(db.String(30), nullable=False)