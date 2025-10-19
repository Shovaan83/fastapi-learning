from fastapi import FastAPI

app = FastAPI()

# Declaration of funtion parameter
fake_items_db  = [{"item_name": "Chatpate"}, {"item_name": "Panipuri"}, {"item_name": "Alu Nimki"}]

# Simple query parameter
@app.get("/items/") # Creating url path
def read_items(skip: int = 0, limit: int = 10): 
    return fake_items_db[skip : skip + limit]

# Combining query and path parameter 
@app.get("/items/{item_id}")
def read_item(item_id: str, q:str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# Multi query parameter
@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10, active: bool = True):
    return{
        "skip": skip,
        "limit": limit,
        "active_only": active,
        "messsage": f"Showing {limit} users, skipping {skip}, active: {active}"
    }

## Advance query paramter 
# Required query parameter
@app.get("/search/")
def search_items(q:str): #Required - no default value 
    return {"query": q, "results": []}

# Multiple Type query parameter 
@app.get("/products/")
def get_products( category: str = "all", min_price: float = 0.0, max_price: float = 1000.0, in_stock: bool = True ):
    return{
        "category": category,
        "price": [min_price, max_price],
        "in_stock_only": in_stock
    }

#List Parameters
@app.get("/items/")
def read_items(tags: list[str] = []):
    return {"tags": tags}