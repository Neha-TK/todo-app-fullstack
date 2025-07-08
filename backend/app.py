from flask import Flask,request
from peewee import *
from flask_cors import CORS


db = SqliteDatabase('todos.db')

class Todo(Model):
    todo_id = AutoField()
    message = CharField()
    is_completed = BooleanField(default = False)

    class Meta:
        database = db

db.connect()
db.create_tables([Todo])

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/todos', methods=['POST', 'GET'])
def get_all_todos():
    if request.method == 'POST':
        message = request.json["todo"]
        Todo(message=message).save()
        return {"message": "Todo Added"}

    if request.method == 'GET':
        query = Todo.select()
        incompleted_todos=[]
        completed_todos =[]
        for todo in query:
            if todo.is_completed:
                todo_to_be_added = {
                    "id" : todo.todo_id,
                    "message" : todo.message
                }
                completed_todos.append(todo_to_be_added)
            else:
                todo_to_be_added={
                    "id": todo.todo_id,
                    "message": todo.message
            }
            incompleted_todos.append(todo_to_be_added)
        return {
            "incompleted_todos": incompleted_todos,
            "completed_todos": completed_todos
        }




@app.route('/todos/complete', methods=['POST'])
def todo_commpleted():
    id = request.json["id"] 
    todo = Todo.get_by_id(id)
    todo.is_completed = True
    todo.save()
    db.close()
    return {'message': "Todo Completed"}


@app.route('/todos/delete', methods=['POST'])
def todo_delete():
    id = request.json["id"] 
    todo = Todo.get_by_id(id)
    todo.delete_instance()
    return {'message': 'Todo deleted'}
    
    
# @app.route('/todo/update/<int:item_id>', methods=['PUT'])
# def update_todo_item(item_id):
#     if 0 <= item_id < len(List_of_todo_items):
#         updated_item = request.json.get('item')
#         List_of_todo_items[item_id] = updated_item
#         return {'message': f'Item updated to "{updated_item}".', 'todo_items': List_of_todo_items}
#     else:
#         return {'error': 'Invalid item ID'}