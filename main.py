from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from fastapi.params import Body
from random import randrange
#Basemodel sets what the default data should look like and what it should contain, prevents users from entering the wrong
#type of data and makes sure the specific data is being sent

app = FastAPI()

class Post(BaseModel):
    title: str 
    content: str 
    published: bool = True
    rating: Optional[int] = None


    

    
# app.get sets the where fromt the webpage the get request is going to pull from
# if it has the same name it will prioritize the first .get it sees 

my_post = [{"title": " title of post 1", "content": "content of post 1", "id": 1 },{"title": "Favorite foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_post):
        if p['id'] == id:
            return i

@app.get("/")
async def root():
    return {"message": "Hello World junghwan"}

# specify where where you want to access /posts will allow me to specify where I want to perfrom the API request

@app.get("/posts")
def get_posts():
    return{"data": my_post}

# this is an example of creating a post request,
@app.post("/createposts")
#assign the body from the post request as a dictionary to a variable labled payload 
def create_posts(new_post: Post ):
    print(new_post.dict())
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_post.append(post_dict)
    return {"data": post_dict}

    #once assigned I am able to print payload 
    #print(payload)
    #able to return a post request fString is used here essentially just a constant 
    #can think of payload[] as a function of an object  so I am able to call the title and the content of the push request
    #return{"new_post" : f"title {payload['title']} content: {payload['content']}"}
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id: {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'message': f"post with id: {id} was not found"}
    return {"post_detail" : post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_index_post(id)
    my_post.pop(index)
    return{'message' : 'post was successfully deleted '}
    #delete Post 
    
@app.put("/post/{id}")
def update_post(id: int, post: Post):
    return{'message' : "updated post"}


#we want a title str, and a content str and these only 

