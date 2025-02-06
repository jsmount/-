from fastapi import FastAPI

app = FastAPI()

# 경로 매개변수 사용 예제
@app.get("/items/{item_id}")
def read_item(item_id: int): # 기본값이 None인 쿼리 매개변수
    return {"item_id":item_id}

# 쿼리 매개변수 사용 예제
@app.get("/getdata/")
def read_items(data: str = "funcoding"): # 데이터의 기본 값은 'funcoding'
    return {"data": data}
