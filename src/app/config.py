# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/5/4 15:57

# 系统配置
from datetime import timedelta

APP_NAME = 'XXX服务'

# 数据库配置

# sqlite
# DB_URI = 'sqlite:///../flask_api.db'

# mysql
USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
DB_NAME = 'flask_api'
DB_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}?charset=utf8'

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Swagger

SWAGGER_CONFIG = {
    "title": f"{APP_NAME} API",
    "description": f"欢迎使用 {APP_NAME}",
    "termsOfService": "",
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'api',
            "route": '/api.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "securityDefinitions": {
        "api_key": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization"
        }
    },
}

# JWT
SECRET_KEY = "\x17wQ;\x0b\xbc4lj\xc2;$\xfc\x96$\xbc\x9e<\x07\x93\x97\x85S\x89G&\xfe\x97\xf8\x85Ip"
JWT_SECRET_KEY = SECRET_KEY
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # 过期时间
