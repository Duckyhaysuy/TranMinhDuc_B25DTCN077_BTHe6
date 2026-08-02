from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
books_db = []       
book_id_counter = 1

class BookCreate(BaseModel):
    title: str      
    author: str     
    price: float    
    pages: int   


class BookResponse(BookCreate):
    id: int 


@app.post("/books", response_model=BookResponse)
def them_sach(book: BookCreate):
    global book_id_counter
    du_lieu_sach = book.model_dump()
    du_lieu_sach["id"] = book_id_counter
    books_db.append(du_lieu_sach)
    book_id_counter += 1
    return du_lieu_sach


@app.get("/books/{id}", response_model=BookResponse)
def lay_chi_tiet_sach(id: int):
    for sach in books_db:
        if sach["id"] == id:
            return sach
    raise HTTPException(status_code=404, detail="Book not found")
