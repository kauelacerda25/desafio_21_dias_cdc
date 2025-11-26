from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Task('{self.id}', '{self.description}')"


# Crud
@app.route('/create', methods=['POST'])
def create_task():
    description = request.form.get('description')
    
    existing_task = Task.query.filter_by(description=description).first()
    if existing_task:
        return 'Error: Task with this description already exists.', 400
    new_task = Task(description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
# cRud
@app.route('/')
def index():
    task = Task.query.all()
    return render_template('index.html', tasks=task)

# crUd
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.description = request.form.get('description')
        db.session.commit()
    return redirect('/')

#cruD
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/')
  

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
