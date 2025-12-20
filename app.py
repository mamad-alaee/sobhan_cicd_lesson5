from fastapi import FastAPI,HTTPException


app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/book/{book_id}")
def read_book(book_id: int):
    if book_id > 10:
        raise HTTPException(
            status_code=403,
            detail="Book not found")
    return {"book_id": book_id}
