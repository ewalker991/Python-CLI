from peewee import PostgresqlDatabase, Model, CharField
from playhouse.shortcuts import model_to_dict, dict_to_model
from functools import partial

db = PostgresqlDatabase('bookmarks', user='postgres', password='', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Bookmark(BaseModel):
    name = CharField()
    category = CharField()
    url = CharField()


# db.drop_tables([Bookmark])
db.create_tables([Bookmark])

# youtube = Bookmark(name='YouTube', category='Media',
#                    url='https://www.youtube.com').save()
# twitch = Bookmark(name = 'Twitch', )


def bookmarker():
    current_bookmarks()

    print("What would you like to do?")
    print("1. Create Bookmark")
    print("2. Edit Bookmark")
    print("3. Delete Bookmark")
    print("4. Get Bookmark details")
    print("5. Exit")
    user_answer = int(input("Your selection: "))
    if user_answer == 1:
        create_bookmark()
    elif user_answer == 2:
        edit_bookmark()
    elif user_answer == 3:
        delete_bookmark()
    elif user_answer == 4: 
        read_bookmark()
    elif user_answer == 5:
        print("Goodbye!")


def current_bookmarks():
    print("Existing bookmarks:")
    bookmarks = Bookmark.select()
    for bookmark in bookmarks:
        print(f'{bookmark.name}')
        # print(f'Category: {bookmark.category}')
        # print(f'Url: {bookmark.url}')
        


def create_bookmark():
    name = str(input("Bookmark name: ")).lower()
    category = str(input("Bookmark category: ")).lower()
    url = str(input("Bookmark url: ")).lower()
    Bookmark(name=name, category=category,
        url=url).save()
    print('Created bookmark: ' + name)
    bookmarker()

def edit_bookmark():
    # print("Which bookmark would you like to edit?")
    bookmark_to_edit = str(input("Which bookmark would you like to edit?: "))
    name = str(input("Bookmark name: ")).lower()
    category = str(input("Bookmark category: ")).lower()
    url = str(input("Bookmark url: ")).lower()
    edited = Bookmark.update(name = name, category = category, url = url).where(Bookmark.name == bookmark_to_edit).execute()
    for bookmarks in Bookmark:
        print("Result of edited bookmark: ")
        print(f'Bookmark name: {bookmarks.name}, Category: {bookmarks.category}, url: {bookmarks.url}')
    bookmarker()
    # bookmark_to_edit = str(input("Bookmark Name: "))
    # if bookmark_to_edit == bookmark.select().where(bookmark.title)

def delete_bookmark():
    bookmark_to_delete = str(input("Which bookmark would you like to delete?: "))
    deleted = Bookmark.delete().where(Bookmark.name == bookmark_to_delete).execute()
    print(f'{bookmark_to_delete} deleted.')
    bookmarker()

def read_bookmark():
    search_bookmark = str(input("What is the name of the bookmark?: ")).lower()
    bookmark_found = Bookmark.select().where(Bookmark.name == search_bookmark)
    for bookmark in bookmark_found:
        print(f'Bookmark name: {bookmark.name}, Category: {bookmark.category}, url: {bookmark.url}')
    bookmarker()



bookmarker()
