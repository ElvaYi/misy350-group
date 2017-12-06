import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    intro = db.Column(db.Text)
    books = db.relationship('Book', backref='author', cascade="delete")


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    summary = db.Column(db.String(256))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))


@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/authors')
def show_all_authors():
    authors = Author.query.all()
    return render_template('author-all.html', authors=authors)


@app.route('/author/add', methods=['GET', 'POST'])
def add_authors():
    if request.method == 'GET':
        return render_template('author-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        intro = request.form['intro']

        # insert the data into the database
        author = Author(name=name, intro=intro)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('show_all_authors'))


@app.route('/author/edit/<int:id>', methods=['GET', 'POST'])
def edit_author(id):
    author = Author.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('author-edit.html', author=author)
    if request.method == 'POST':
        # update data based on the form data
        author.name = request.form['name']
        author.intro = request.form['intro']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_authors'))


@app.route('/author/delete/<int:id>', methods=['GET', 'POST'])
def delete_author(id):
    author = Author.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('author-delete.html', author=author)
    if request.method == 'POST':
        # delete the author by id
        # all related books are deleted as well
        db.session.delete(author)
        db.session.commit()
        return redirect(url_for('show_all_authors'))


# book-all.html adds song id to the edit button using a hidden input
@app.route('/books')
def show_all_books():
    books = Book.query.all()
    return render_template('book-all.html', books=books)


@app.route('/book/add', methods=['GET', 'POST'])
def add_books():
    if request.method == 'GET':
        authors = Author.query.all()
        return render_template('book-add.html', authors=authors)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        year = request.form['year']
        summary = request.form['summary']
        author_name = request.form['author']
        author = Author.query.filter_by(name=author_name).first()
        book = Book(name=name, year=year, summary=summary, author=author)

        # insert the data into the database
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('show_all_books'))


@app.route('/book/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.filter_by(id=id).first()
    authors = Author.query.all()
    if request.method == 'GET':
        return render_template('book-edit.html', book=book, authors=authors)
    if request.method == 'POST':
        # update data based on the form data
        book.name = request.form['name']
        book.year = request.form['year']
        book.summary = request.form['summary']
        author_name = request.form['author']
        author = Author.query.filter_by(name=author_name).first()
        book.author = author
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_books'))


@app.route('/book/delete/<int:id>', methods=['GET', 'POST'])
def delete_book(id):
    book = Book.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('book-delete.html', book=book)
    if request.method == 'POST':
        # delete the artist by id
        # all related songs are deleted as well
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('show_all_books'))


@app.route('/members')
def members():
    return render_template('members.html')




# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
