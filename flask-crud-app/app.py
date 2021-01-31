from flask import Flask, render_template, request,redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qwertyuiop098@localhost/crud1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    designation = db.Column(db.String(100))
    role = db.Column(db.String(100))
    updatedby = db.Column(db.String(100))
    
 
 
    def __init__(self, name, designation, role,updatedby):
 
        self.name = name
        self.designation = designation
        self.role = role
        self.updatedby = updatedby


@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template('index.html',employees=all_data)

@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
        designation = request.form['designation']
        role = request.form['role']
        updatedby = request.form['updatedby']
 
 
        my_data = Data(name, designation, role,updatedby)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")
 
        
        return redirect(url_for('Index'))

@app.route('/update',methods=['GET,POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.designation = request.form['designation']
        my_data.role = request.form['role']
        my_data.updatedby = request.form['updatedby']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index'))

@app.route('/delete/<id>',methods = ['GET','POST'])
def delete():
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)