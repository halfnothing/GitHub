from flask import Flask, render_template
import sqlite3

db = sqlite3.connect('db.sqlite3')
db.row_factory = sqlite3.Row

app = Flask('MyApp')

@app.route('/')
def index():
    td = []
    cur = db.cursor()
    cur.execute("Select Group_Number as id, Group_Number as col1 FROM Group_")
    rows = cur.fetchall()
    for r in rows:
        td.append(dict(r))
    return render_template('index.html',table_data=td)

app.run()