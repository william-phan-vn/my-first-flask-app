import sys
from unittest.result import failfast
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vietplh1:123@localhost:5432/todo-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate  = Migrate(app, db)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    # Create useful debugging statement when printing the object
    def __repr__(self):
        return f'<Todo {self.id} {self.description} {self.completed}>'


# db.create_all()


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.order_by('id').all())


@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['completed'] = todo.completed
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    
    if not error:
        return jsonify(body)


@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        print(completed)
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except: 
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
