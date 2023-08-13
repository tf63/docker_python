# syntax=docker/dockerfile:1
# https://fastapi.tiangolo.com/ja/deployment/docker/
FROM python:3.9

WORKDIR /app

# ローカルのrequirements.txtをコンテナの/appフォルダ直下に置く
COPY requirements.txt /app

# コンテナ内でpipをアップグレードした後、pip install -r requirements.txtを実行
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
