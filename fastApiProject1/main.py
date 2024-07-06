from fastapi import FastAPI
from data import movies_list
from movie import MovieBaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{rollno}")
async def say_hello(rollno: int):
    return {"message": f"Hello {rollno}"}

@app.get("/movies")
async def get_movies():
    return list(movies_list.values())

@app.get("/movies/{name}")
async def get_movie(name: str):
    return movies_list[name]

@app.get("/movies")
async def get_all_movies(limit: int=5):
    all_movies = list(movies_list.values())
    return all_movies[:limit]

@app.get("/movies/{name}")
async def get_movie(offset: int, limit: int=5):
    all_movies=list(movies_list.values())
    movies_count = len(all_movies)
    start_index =(offset-1)*limit
    end_index =start_index +limit
    if start_index >= movies_count:
        return None
    return all_movies[start_index:end_index]

@app.post("/movies")
async def create_movie(movie: MovieBaseModel):
    movies_list[movie.name]=movie.dict()
    return{"message":f"Movie {movie.name} created"}
