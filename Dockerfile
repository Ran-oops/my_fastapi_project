FROM python:3.9

WORKDIR /app

RUN chmod a+rwx /app
COPY . .
# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt


# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]