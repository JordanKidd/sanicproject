import peewee
import peewee_async


database = peewee.SqliteDatabase('app.db')


class BaseModel(peewee.Model):

    class Meta:
        database = database


class User(BaseModel):
    username = peewee.CharField(unique=True)


if __name__ == '__main__':
    resp = input('create tables: y/n?')
    if 'y' in resp.lower():
        User.create_table()
