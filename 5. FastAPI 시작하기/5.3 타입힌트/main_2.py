from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()

# List 데이터 타입을 쿼리 매개변수로 받는 라우트 예제
@app.get("/items/")
def read_items(q: List[int] = Query([])): # 빈 리스트를 기본값으로 설정
    return {"q": q}

# Dict 데이터 타입을 요청 바디로 받는 라우트 예제
@app.post("/create-item/")
def create_item(item: Dict[str, int]):
    return item