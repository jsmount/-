from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None # 필드가 선택적임을 의미 -> None 값 허용
    price: float
    tax: float = 0.1

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item.dict()}