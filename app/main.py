from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

# 创建数据库表
models.Base.metadata.create_all(bind=engine)
"""
当类继承Base时：
    1.sqlalchemy自动检测类属性
    2.将这些属性转换为数据库列定义
    3.将表信息注册到Base.metadata中
"""
"""
create_all(bind=engine) - 表创建命令
    1.扫描Base.metadata中的所有注册表信息
    2.根据数据库类型生成对应的DDL(data definition language)语句
    3.通过指定的engine连接到数据库
    4.执行create table语句
    5.只创建不存在的表，已存在的表不受影响
"""

app = FastAPI()

@app.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id=user_id, user_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if not crud.delete_user(db, user_id=user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}

# dev运行命令：uvicorn app.main:app --reload
# prod运行命令：uvicorn app.main:app --host 0.0.0.0 --port 80 --workers 4
"""
app.main表示的是app包， main表示module名，即文件名。 :app表示的是main.py中的app = FastAPI()

 --reload
作用：启用开发模式的热重载功能

行为：
    监视项目文件变动（.py, .env 等）
    检测到修改时自动重启服务器
    极大提升开发效率
"""














































































































































