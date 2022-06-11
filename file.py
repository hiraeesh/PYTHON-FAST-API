from fastapi import FastAPI


app=FastAPI()

@app.get('/')
async def file_name():
    return {"course":"fast_api"}
