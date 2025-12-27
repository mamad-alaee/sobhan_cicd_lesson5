from fastapi import FastAPI,HTTPException


app = FastAPI()

code = 200

@app.get("/")
def read_root():
    return {"Hello": "World"}

# gozoo 2
@app.get("/book/{book_id}")
def read_book(book_id: int):
    if book_id > 10:
        raise HTTPException(
            status_code=404,
            detail="Book not found")
    return {"book_id": book_id}
