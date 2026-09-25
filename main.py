from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

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
    
    
## body , headers - request headers, query params   
    
# Different types of HTTP methods

@app.post("/create-product")
def create_product(product : ProductDTO):
    print(product)
    data =  product.model_dump()
    print(data)
    products.append(data)
    return {
        "status": "Product Created",
        "data":products
    }


# pydantic


## How to call different HTTP methods - Any Tools (Postman)


## how to validate data. DTOS

@app.put("/update_product/{product_id}")
def update_product(product_data: ProductDTO, product_id:int):
    
    for i,oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[i]= product_data.model_dump()
            return {
                "status":"Product update successfully..",
                "product" : product_data
            }
            
    return {
            "error":"product not found"
        }
        
    
@app.delete("/update_product/{product_id}")
def delete_product(product_id:int):
    for i,oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            delete_product = products.pop(i)
            
            return {
                        "status":"Product update successfully..",
                        "product" : delete_product
                    }
        return {
                    "error":"product not found"
                }
                