# FastAPI 用户管理项目

使用 Docker Compose 部署的 FastAPI + PostgreSQL + Nginx 项目，提供完整的用户管理 API。

## 功能特性

- 创建用户
- 更新用户信息
- 删除用户
- 获取用户列表
- 获取单个用户信息

## 技术栈

- **后端**: FastAPI (Python)
- **数据库**: SQLite (开发) / PostgreSQL (生产)
- **Web服务器**: Nginx
- **容器化**: Docker & Docker Compose
- **监控**: Prometheus + Grafana

## 安装指南

### 开发环境

1. 克隆项目:
   ```
   git clone <项目地址>
   cd fastapi_project
   ```

2. 确保已安装 Docker 和 Docker Compose

3. 构建并启动开发环境:
   ```
   docker-compose up --build
   ```

4. 访问应用: http://localhost:8000 和 http://localhost:8000/docs#

### 生产环境

1. 构建并启动生产环境:
   ```
   docker-compose -f docker-compose.prod.yml up --build
   # 自动构建镜像并启动所有容器服务，特别适合在修改代码或配置后使用
   -d: 后台运行 (detach)
   -remove-orphans: 清理不再使用的容器
   --build： 强制重新构建服务镜像
   ```
   ```bazaar
    # 一些命令说明
    # docker-compose build; 仅构建镜像，不启动容器; 需要提前构建好镜像
    # docker-compose up; 启动所有容器服务,使用现有镜像; 没有代码/配置变更时
    # docker-compose up -d; 构建+启动完整流程; 开发调试中最常见
   ```

2. 应用将通过 Nginx 提供服务，访问端口为 80

## API 接口文档

- 交互式 API 文档: http://localhost:80/docs
- 替代 API 文档: http://localhost:80/redoc

## API 端点

| 方法 | 路径 | 描述 |
|------|------|------|
| POST | `/users/` | 创建新用户 |
| GET | `/users/` | 获取用户列表 |
| GET | `/users/{user_id}` | 获取特定用户 |
| PUT | `/users/{user_id}` | 更新用户信息 |
| DELETE | `/users/{user_id}` | 删除用户 |

## 项目结构

```
.
├── app/                 # FastAPI 应用
│   ├── __init__.py
│   ├── crud.py         # 数据库操作
│   ├── database.py     # 数据库配置
│   ├── main.py         # 应用入口
│   ├── models.py       # 数据库模型
│   ├── schemas.py      # 数据模型
│   └── start.sh
├── nginx/              # Nginx 配置
├── prometheus/         # Prometheus 配置
├── grafana/            # Grafana 配置
├── Dockerfile          # 开发环境 Docker 配置
├── Dockerfile.prod     # 生产环境 Docker 配置
├── docker-compose.yml  # 开发环境编排
└── docker-compose.prod.yml # 生产环境编排
```

## 开发说明

开发模式下启用了热重载功能，修改代码后会自动重启服务。

运行开发服务器的命令:
```
uvicorn app.main:app --reload
```

运行生产服务器的命令:
```
uvicorn app.main:app --host 0.0.0.0 --port 80 --workers 4
```

## 监控

项目集成了 Prometheus 和 Grafana 用于监控:

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## 数据库

项目支持两种数据库配置:
- 开发环境使用 SQLite
- 生产环境使用 PostgreSQL

数据库文件在开发环境中持久化存储在 `app/data` 目录中。