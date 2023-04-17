from peewee import *

db = MySQLDatabase(
    'easyTemplate', 
    user='root',
    password='root1234',
    host='mysql',
    port=3306)
    


class User (Model):
    name=TextField()
    age=IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        database=db
        db_table='User'

#User.create_table()
#rec1=User(name="Rajesh", age=21)
#rec1.save()
    
