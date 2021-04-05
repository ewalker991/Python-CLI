from peewee import PostgresqlDatabase, Model, CharField
from playhouse.shortcuts import model_to_dict, dict_to_model
from functools import partial

db = PostgresqlDatabase('bookmarks', user='postgres', password='', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Bookmark(BaseModel):
    label = CharField()
    category = CharField()
    url = CharField()


# db.drop_tables([Bookmark])
db.create_tables([Bookmark])

# youtube = Bookmark(label='YouTube', category='Media',
#                    url='https://www.youtube.com').save()
# twitch = Bookmark(label = 'Twitch', )


def bookmarker():
    current_bookmarks()

    print("What would you like to do?")
    print("1. Create Bookmark")
    print("2. Edit Bookmark")
    print("3. Delete Bookmark")
    user_answer = int(input("Your selection: "))
    if user_answer == 1:
        create_bookmark()
    elif user_answer == 2:
        edit_bookmark()
    elif user_answer == 3:
        delete_bookmark()
    else: 
        print("Goodbye!")


def current_bookmarks():
    print("Bookmarks:")


def create_bookmark():
    label = str(input("Bookmark title: "))
    category = str(input("Bookmark category: "))
    url = str(input("Bookmark url: "))
    Bookmark(label=label, category=category,
        url=url).save()
    print('Created bookmark: ' + label)

def edit_bookmark():
    print("Which bookmark would you like to edit?")
    # bookmark_to_edit = str(input("Bookmark Name: "))
    # if bookmark_to_edit == bookmark.select().where(bookmark.title)

def delete_bookmark():
    print("Deleting bookmark: ")


bookmarker()
