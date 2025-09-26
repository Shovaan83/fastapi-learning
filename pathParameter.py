from fastapi import FastAPI

app = FastAPI()

# @app.get("/users/{user_id}") #{user_id} is the path which defines the parameter
# def get_user(user_id): # function which captures the value
#     return {"user_id": user_id}

# # Type hints for the validation
# @app.get("/users/{username}")
# def get_username(username: str): #for string validation
#     return {"username": username}

# @app.get("/users/{item_id}")
# def get_itemId(itemId: int): #for int validation
#     return {"item_id": itemId}

# @app.get("/prices/{price}")
# def get_price(price: float): #for float
#     return {"price": price}

#Making User Profile Endpoints 
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {
        "user_id": user_id,
        "message": f"Hello User {user_id}!"
    }

# Making Product with Interger ID
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {
        "product_id": product_id,
        "name": f"Product #{product_id}",
        "available": True
    }

# Making Multi Path Parameter 
@app.get("/users/{user_id}/posts/{post_id}")
async def get_user_post(user_id: str, post_id: int):
    return{
        "user_id": user_id,
        "post_id": post_id,
        "title": f"Post {post_id} by {user_id}"
    }