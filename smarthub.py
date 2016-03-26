# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

from contextlib import closing
# configuration
DATABASE = 'D:/BungBu/Project/Python/smarthub/smarthub.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

# constant
TYPE_DEVICE = ["LED"]

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
'''
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit() 
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_devices'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_devices'))

@app.route('/')
def show_devices():
    cur = g.db.execute('select id, name from devices order by id desc')
    devices = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
    return render_template('show_devices.html', devices=devices)

@app.route('/add', methods=['POST'])
def add_device():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into devices (name) values (?)',
                 [request.form['device']])
    g.db.commit()
    flash('New device was successfully add')
    return redirect(url_for('show_devices'))

@app.route('/detail/<device_id>')
def detail_device(device_id):
    cur = g.db.execute('select id, name from devices where id = (?)', [device_id])
    device = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
    return render_template('detail_device.html', device=device[0])

@app.route('/save', methods=['POST'])
def save_config():
    data = request.form['feature']
    flash('data = ' + data)
    data = data.split('_')
    flash('status = ' + data[0] + ' id = ' + data[1])
    g.db.execute('insert into services (status, device_id) valueS (?,?)', [data[0], data[1]])
    g.db.commit()
    return redirect(url_for('show_devices'))
'''
@app.route('/')
def show_devices():
    return render_template('show_devices.html')


if __name__ == '__main__':
    app.run()

