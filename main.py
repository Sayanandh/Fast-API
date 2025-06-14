from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data":{"Name":"SAyu"}}

@app.get('/baka')
def about():
    return "hellohello"

