#### **설치 및 실행하기**
---
- 설치
~~~
pip install "fastapi[all]"
~~~
~~~
uvicorn main:app --reload
~~~
- 어떤 경우에는 아래와 같이 실행
    - 나중에 작성바람...
~~~
python -m uvicorn main:app --reload
~~~
- uvicorn main:app 명령은 다음을 의미합니다:
~~~
main: 파일 main.py (파이썬 "모듈").
app: main.py 내부의 app = FastAPI() 줄에서 생성한 오브젝트.
--reload: 코드 변경 후 서버 재시작. 개발에만 사용.
~~~

#### **기본 사용법**
---
- FastAPI 임포트.
- app 인스턴스 생성.
- (@app.get("/")처럼) 경로 동작 데코레이터 작성.
- (위에 있는 def root(): ...처럼) 경로 동작 함수 작성.
- (uvicorn main:app --reload처럼) 개발 서버 실행.
~~~python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
~~~

#### **경로 매개변수**
---
-  "매개변수" 또는 "변수"를 경로에 선언
- 함수에 있는 경로 매개변수의 타입을 선언할 수 있음
~~~python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
~~~

- 순서 문제
    - 경로 동작은 순차적으로 평가되기 때문에 /users/{user_id} 이전에 /users/me를 먼저 선언해야 함
    - 그렇지 않으면 /users/{user_id}는 매개변수 user_id의 값을 "me"라고 "생각하여" /users/me도 연결
~~~python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
~~~
- 사전정의 값
    - 만약 경로 매개변수를 받는 경로 동작이 있지만, 유효하고 미리 정의할 수 있는 경로 매개변수 값을 원한다면 파이썬 표준 Enum을 사용
~~~python
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"} 
~~~

- 경로를 포함하는 경로 매개변수
    - 아래 형식으로 경로 매개변수를 정의하면 선언 가능
~~~
/files/{file_path:path}
~~~
~~~python
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
~~~

#### **쿼리 매개변수**
---
- 경로 매개변수의 일부가 아닌 다른 함수 매개변수를 선언할 때, "쿼리" 매개변수로 자동 해석
- 쿼리 매개변수는 경로에서 고정된 부분이 아니기 때문에 선택적일 수 있고 기본값을 가질 수 있음
    - 아래의 예에서 기본값은 skip=0과 limit=10 
~~~python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
~~~

- 선택적 매개변수
    - 아래 예에서 FastAPI는 q가 = None이므로 선택적이라는 것을 인지
    - FastAPI는 item_id가 경로 매개변수이고 q는 경로 매개변수가 아닌 쿼리 매개변수라는 것을 알 정도로 충분히 똑똑
~~~python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
~~~

- boolean 형태 변환
    - 아래 요청은 모두 동일함

~~~
http://127.0.0.1:8000/items/foo?short=1
http://127.0.0.1:8000/items/foo?short=True
http://127.0.0.1:8000/items/foo?short=true
http://127.0.0.1:8000/items/foo?short=on
http://127.0.0.1:8000/items/foo?short=yes
~~~

~~~python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
~~~

- 여러 경로 매개변수와 쿼리 매개변수를 동시에 선언
~~~python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
~~~

- 필수 쿼리 매개변수
    -  쿼리 매개변수를 필수로 만들려면 기본값을 선언하지 않으면 됨
~~~python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
~~~

#### **Request Body**
---
- request body를 설정하려면 pydantic model을 사용해야 함

~~~python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
~~~

- 경로 매개변수 + request body
    - 경로에 포함된 매개변수는 경로 매개변수가 되고, 경로에 포함되어 있지 않은 pydantic model은 request body가 됨
~~~python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
~~~

- 경로 매개변수 + 쿼리 매개변수 + request body
    - 경로에 포함된 변수는 경로 매개변수
    - 경로에 포함되어 있지 않은 pydantic model은 request body
    - 경로에 포함되어 있지 않은 매개변수는 쿼리 매개변수
~~~python
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
~~~

#### **Cookie 매개변수**
---
- 경로 매개변수, 쿼리 매개변수와 구조는 동일하지만, 쿠키 매개변수를 선언해주어야 함
~~~python
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
~~~

#### **Header 매개변수**
---
- 헤더 매개변수를 Query, Path 그리고 Cookie 매개변수들과 같은 방식으로 정의할 수 있음
~~~python
from typing import Union

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}
~~~
- 자동변환
    - 대부분의 표준 헤더는 "마이너스 기호" (-)라고도 하는 "하이픈" 문자로 구분
    - 그러나 파이썬에서 user-agent와 같은 형태의 변수는 유효하지 않음
    - Header는 기본적으로 매개변수 이름을 언더스코어(_)에서 하이픈(-)으로 변환하여 헤더를 추출하고 기록
    - 만약 언더스코어를 하이픈으로 자동 변환을 비활성화해야 하면, Header의 convert_underscores 매개변수를 False로 설정
~~~python
from typing import Union

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    strange_header: Union[str, None] = Header(default=None, convert_underscores=False)
):
    return {"strange_header": strange_header}
~~~

#### **CORS(Cross-Origin Resource Sharing)**
---
~~~python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
~~~