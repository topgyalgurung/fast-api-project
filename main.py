from fastapi import FastAPI
from models import Todo

app = FastAPI()

# benefits:
"""
- built in async 
- built in data validation with pydantic 
- fast api is typed python 
"""

@app.get("/")   # path decorator 
# uses asgi whereas flask uses wsgi which handles synchronously 
async def root():  # built in async 
    return {"message": "Hello World"}

todos=[]

# get all todos 
@app.get("/todos")
async def get_todos():
    return {"todos": todos}



# get single todos using id 
# can pass dynamic parameter 
@app.get("/todos/{todo_id}")
async def get_todos(todo_id: int): #type parameter or python think is string
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "no todos found"}


# To declare a request body, you use Pydantic models with all their power and benefits.
# create a todo 
@app.post("/todos")
async def create_todos(todo:Todo):   # todo of type Todo from model
    todos.append(todo)
    # when you have database, you can  add db functionality like write to db instead of appending
    return {"message": "Todo added"}

# update a todo 

# delete a todo 
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int): #type parameter or python think is string
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been DELETED!"}
    return {"message": "no todos found"}