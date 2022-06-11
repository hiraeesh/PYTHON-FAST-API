from fastapi import FastAPI

app=FastAPI()
c="raeesh"
@app.get('/')
async def name1():
    a=5
    b=6
    return f'This is value of a {a} and this is b {b} {c}'