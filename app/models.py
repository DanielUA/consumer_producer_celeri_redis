from mongoengine import *

connect(
    db="web16", 
    host = "mongodb+srv://userweb16:example@cluster0.q1gz4ma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )

class Task(Document):
    completed = BooleanField(default=False)
    consumer = StringField(max_length=150)

 