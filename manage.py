from flask_script import Manager
from bookstore import app, db, Author, Book

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    jane = Author(name='Jane Austen', intro='Jane Austen was an English novelist known primarily for her six major novels, which interpret, critique and comment upon the British landed gentry at the end of the 18th century.')
    jk = Author(name='J. K. Rowling', intro='Joanne Rowling, who writes under the pen names J. K. Rowling and Robert Galbraith, is a British novelist and screenwriter who wrote the Harry Potter fantasy series. ')
    book1=Book(name='Pride and Prejudice', year='1813', author_id=1, summary='Pride and Prejudice is a romance novel by Jane Austen, first published in 1813. The story charts the emotional development of the protagonist, Elizabeth Bennet, who learns the error of making hasty judgments and comes to appreciate the difference between the superficial and the essential. The comedy of the writing lies in the depiction of manners, education, marriage, and money in the British Regency.')
    db.session.add(jane)
    db.session.add(jk)
    db.session.add(book1)

    db.session.commit()


if __name__ == "__main__":
    manager.run()
