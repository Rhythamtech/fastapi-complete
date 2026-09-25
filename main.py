from fastapi import FastAPI, Request
from mockData import products

app =  FastAPI()


@app.get("/")
def home():
    return "Welcome to fastapi."

@app.get("/contact-us")
def contact():
    return  "You can connect us any time."  

@app.get("/products")
def get_products():
    return products


# Path Params..

@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    
    # if product available with id, return product , else return error message
    
    for oneProduct in products:
        if oneProduct.get("id") ==  product_id:
            return oneProduct
    
    return {
        "error":"product not found"
    }
    
# query params
# @app.get("/greet")
# def greet_user(name:str, age : int):
#     return {"greet":f"Hello {name} how are you? Your age is {age}"}

@app.get("/greet")
def greet_user(request:Request):
    params = dict(request.query_params)
    
    return {
        "greet": params
    }