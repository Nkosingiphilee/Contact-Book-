import sqlite3
from flask import Flask, render_template, url_for, request, redirect, flash

from forms import AddContact, UpdateContact

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contact
               (id	INTEGER PRIMARY	KEY AUTOINCREMENT,
               name Text,
               number TEXT,
               email TEXT,
               address Text)""")
conn.commit()
conn.close()

app = Flask(__name__)
app.config['SECRET_KEY'] = '52252223556333663'


# app.secret_key = 'some_secret'

@app.route('/')
def home():
    with sqlite3.connect('contacts.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM contact")
    data = cursor.fetchall()
    return render_template('home.html', data=data)


@app.route('/add', methods=['GET', 'POST'])
def addcontact():
    form = AddContact()
    if form.validate_on_submit():
        with sqlite3.connect('contacts.db') as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO contact(name,number, email,address)VALUES (? ,? ,? ,?)",
                           (form.name.data, form.number.data, form.email.data, form.address.data))
        flash('you\'ve added %s' % form.name.data)
        return redirect(url_for('home'))
    return render_template('addcontact.html', form=form)


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    with sqlite3.connect('contacts.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM contact WHERE id=%d" % int(id))
        data = cursor.fetchone()
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        email = request.form['email']
        address = request.form['address']
        with sqlite3.connect('contacts.db') as db:
            cursor = db.cursor()
            cursor.execute("UPDATE contact SET name=?, number=?, email=?, address=? WHERE id=?", (name, number, email, address, id))
            db.commit()
   
        return redirect(url_for('home'))
    return render_template('update.html', id=id, data=data)


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    with sqlite3.connect('contacts.db') as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM contact WHERE id=%d" % int(id))
        data = cursor.fetchone()
    if request.method == 'POST':
        with sqlite3.connect('contacts.db') as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM contact WHERE id=?", (id))
        flash('user has been deleted successfully')
        return redirect(url_for('home'))
    return render_template('delete.html', id=id, data=data)


if __name__ == '__main__':
    app.run(debug=True)
