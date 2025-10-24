from fastapi import FastAPI
from fastapi import Query

app = FastAPI()

fake_items_db = [{"item_name": "Chatpate"}, {"item_name": "Panipuri"}, {"item_name": "Alu Nimki"}]

# # Basic Approach

@app.get("/items/")
def read_items(q: str | None = None):
    return {"q": q}


# # Advanced approach with Query 

@app.get("/items/")
def read_items(q: str | None = Query(default=None, max_length=50)):
    return {"q": q}


# The query function 

# Basic usage of Query
@app.get("/items/")
def read_items(q: str | None = Query(default=None, max_length=50)):
    results = []
    if q: 
        #Filter the items based on query 
        results = [item for item in fake_items_db if q.lower() in item["item_name"].lower()]
    else:
        results = fake_items_db 
    return {"results": results}

# # String Validation Cosntraints
@app.get("/items/")
def read_items(q: str | None = Query(
    default = None,
    min_length = 3,
    max_length= 50,
    regex="^[a-zA-Z0-9 ]*$"
)):
    return {"q": q}

# # Numeric Validation Constraints
@app.get("/items/")
def read_items( skip: int = Query(default=0, ge=0),
               limit: int = Query(default=10, ge=1, le=100)):
    return {"skip": skip, "limit": limit}


# Practise: Basic Query Validation 
@app.get("/items/")
def read_items(q: str | None = Query(default= None, max_length=50)):
    result = []
    if q: 
        results = [{"item_name": "Hoo", "description": "WHOOOOOOO"}]
        return {"q": q, "results": results}
    

# Practise 2: Required Query Parameter 
@app.get("/items/")
def read_items(q: str = Query(min_length=3)):
    return {"q": q}

# Practise 3: Query with Multiple Constraints 
@app.get("/items/")
def read_items( q: str = Query(min_length=3, max_length=100, regex="^fixedquery$", description="Hello from the Database", deprecated=False)):
    return {"q": q}


# Practise 4: With Full MetaData
@app.get("/item/")
def read_items(
    q: str | None = Query(
        default=None,
        title="Query String",
        description="Query string database ma khojna ko lagi",
        min_length=3,
        max_length=50,
        example="Shovan"
    )):
    return {"q": q}

# Practise 5: List Query Parameters
@app.get("/items/")
def read_items(
    q: list[str] | None = Query(
        default=None
    )
):
    return {"q": q}

# with validation 

@app.get("/items/")
def read_items(
    q: list[str] = Query(
        default = ["foo", "bar"],
        title="Query Strings",
        description="Multiple query strings as a list to search in the database",
        min_length=3,
    )
):
    return {"q": q}