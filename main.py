from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {"id": 1, 
     "author": "Alice",
     "title": "First Post", 
     "content": "This is the first post.",
     "date_posted": "2024-01-01"
     },
    {"id": 2, 
     "author": "Bob",
     "title": "Second Post", 
     "content": "This is the second post.",
     "date_posted": "2024-01-02"
     }
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/post", include_in_schema=False, name="post")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "posts": posts, "title": "Home"})

@app.get("/posts")
def get_posts():
    return {"posts": posts}