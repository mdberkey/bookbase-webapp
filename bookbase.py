import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(project_dir, 'bookdatabase.db')
database_file = f'sqlite://{db_dir}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False,
                      primary_keyA=True)

    def __repr__(self):
        return f'<Title: {self.title}>'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form:
        book = Book(title=request.form.get('title'))
        db.session.add(book)
        db.session.commit()
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
