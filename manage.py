from flask_script import Manager
from bookstore import app, db, Author, Book

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    jane = Author(name='Jane Austen', intro='Jane Austen was an English novelist known primarily for her six major novels, got the British landed gentry at the end of the 18th century.')
    jk = Author(name='J. K. Rowling', intro='J. K. Rowling is a British novelist and screenwriter who wrote the Harry Potter fantasy series. ')
    book1=Book(name='Pride and Prejudice', year='1813', author_id=1, summary='Pride and Prejudice is a romance novel by Jane Austen, first published in 1813. The story charts the emotional development of the protagonist, Elizabeth Bennet, who learns the error of making hasty judgments and comes to appreciate the difference between the superficial and the essential. The comedy of the writing lies in the depiction of manners, education, marriage, and money in the British Regency.')
    book2=Book(name='Harry Potter and the Chamber of Secrets', year='1998', author_id=2, summary='Harry Potter and the Chamber of Secrets is a fantasy novel written by British author J. K. Rowling and the second novel in the Harry Potter series. The plot follows his second year at Hogwarts School of Witchcraft and Wizardry, during which a series of messages on the walls of the school corridors warn that the "Chamber of Secrets" has been opened and that the "heir of Slytherin" would kill all pupils who do not come from all-magical families. These threats are found after attacks which leave residents of the school "petrified" (frozen like stone). Throughout the year, Harry and his friends Ron and Hermione investigate the attacks.')
    book3=Book(name='Harry Potter and the Goblet of Fire', year='2001', author_id=2, summary='Harry Potter and the Goblet of Fire is a fantasy novel written by British author J. K. Rowling and the fourth novel in the Harry Potter series. It follows Harry Potter, a wizard in his fourth year at Hogwarts School of Witchcraft and Wizardry and the mystery surrounding the entry of his name into the Triwizard Tournament, in which he is forced to compete.')
    book4=Book(name='Harry Potter and the Half-Blood Prince', year='2005', author_id=2, summary='Harry Potter and the Half-Blood Prince is a fantasy novel written by British author J. K. Rowling and the sixth and penultimate novel in the Harry Potter series. Set during protagonist his sixth year at Hogwarts, the novel explores the past of his nemesis, Lord Voldemort, and his preparations for the final battle against Voldemort alongside his headmaster and mentor Albus Dumbledore.')


    db.session.add(jane)
    db.session.add(jk)
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.add(book4)


    db.session.commit()


if __name__ == "__main__":
    manager.run()
