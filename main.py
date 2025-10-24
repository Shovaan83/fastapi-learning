from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel, Field

app = FastAPI(
    title="FastAPI Learning Project",
    description="A comprehensive API demonstrating path parameters, query parameters, and request bodies",
    version="1.0.0"
)

# ============= Path Parameter Routes =============
path_router = APIRouter(prefix="/path", tags=["Path Parameters"])

@path_router.get("/users/{user_id}")
async def get_user(user_id: str):
    return {
        "user_id": user_id,
        "message": f"Hello User {user_id}!"
    }

@path_router.get("/products/{product_id}")
async def get_product(product_id: int):
    return {
        "product_id": product_id,
        "name": f"Product #{product_id}",
        "available": True
    }

@path_router.get("/users/{user_id}/posts/{post_id}")
async def get_user_post(user_id: str, post_id: int):
    return{
        "user_id": user_id,
        "post_id": post_id,
        "title": f"Post {post_id} by {user_id}"
    }

# ============= Query Parameter Routes =============
query_router = APIRouter(prefix="/query", tags=["Query Parameters"])

fake_items_db = [{"item_name": "Chatpate"}, {"item_name": "Panipuri"}, {"item_name": "Alu Nimki"}]

@query_router.get("/items/")
def read_items(skip: int = 0, limit: int = 10): 
    return fake_items_db[skip : skip + limit]

@query_router.get("/items/{item_id}")
def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@query_router.get("/users/")
def read_users(skip: int = 0, limit: int = 10, active: bool = True):
    return{
        "skip": skip,
        "limit": limit,
        "active_only": active,
        "message": f"Showing {limit} users, skipping {skip}, active: {active}"
    }

@query_router.get("/search/")
def search_items(q: str):
    return {"query": q, "results": []}

@query_router.get("/products/")
def get_products(
    category: str = "all",
    min_price: float = 0.0,
    max_price: float = 1000.0,
    in_stock: bool = True
):
    return{
        "category": category,
        "price_range": [min_price, max_price],
        "in_stock_only": in_stock
    }

@query_router.get("/filter-items/")
def read_items_with_tags(tags: list[str] = []):
    return {"tags": tags}

# ============= Request Body Routes =============
request_body_router = APIRouter(prefix="/body", tags=["Request Body"])

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Ajazz AK820 Max",
                "description": "A great keyboard",
                "price": 8200.0,
                "tax": 13.2
            }
        }

@request_body_router.post("/items/")
def create_item(item: Item):
    return item

@request_body_router.post("/items/{item_id}")
def create_item_with_id(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

@request_body_router.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

# ============= Include All Routers =============
app.include_router(path_router)
app.include_router(query_router)
app.include_router(request_body_router)

# ============= Root Endpoint =============
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to FastAPI Learning Project!",
        "endpoints": {
            "path_parameters": "/path/*",
            "query_parameters": "/query/*",
            "request_body": "/body/*",
            "documentation": "/docs",
            "alternative_docs": "/redoc"
        }
    }