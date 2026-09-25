from fastapi import FastAPI

app =  FastAPI()


@app.get("/")
def home():
    return "Welcome to fastapi."

@app.get("/contact-us")
def contact():
    return  "You can connect us any time."