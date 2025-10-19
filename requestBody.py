from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Request Body without Parameter
@app.post("/items/")
def create_item(item: Item):
    return item

#Request Body with Parameter 
@app.post("/items/{item_id}")
def create_item_with_id(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

# Request body with path and query parameter 
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

# Advance pydantic features 

#Field validation 

# class Item(BaseModel):
    
#     name: str = Field(..., min_legth=1, max_length=100)
#     description: str = FileExistsError(None, max_length=100)
#     price: float = Field(..., gt=0) #gt = greater than
#     tax: float | None = Field(None, ge=0) #ge = greater than or equal

# Nested Model 

# class Image(BaseModel):
#     url: str
#     name: str

# class Item(BaseModel):
#     name: str
#     description: str | None = None 
#     price: float 
#     tax: float | None = None 
#     tags: list[str] = []
#     images: list[Image] | None = None 

# Model Configuration 

class Item(BaseModel):
    name: str
    description: str | None = None 
    price: float 
    tax: float | None = None 

    class config:
        schema_extra = {
            "example": {
                "name" : "Ajazz AK820 Max",
                "description" : "A great keyboard",
                "price" : 8200.0,
                "tax": 13.2
            }
        }
