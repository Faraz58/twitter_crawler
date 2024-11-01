from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app import auth, proxy, crawler
from typing import List

app = FastAPI()

# مدیریت احراز هویت
class AuthData(BaseModel):
    username: str
    password: str
    token: str = None

@app.post("/manage_account")
async def manage_account(auth_data: AuthData):
    result = auth.authenticate(auth_data.username, auth_data.password)
    if result:
        return {"message": "Authentication successful."}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed.")

# تنظیم پروکسی
class ProxyData(BaseModel):
    proxies: List[str]

@app.post("/config_proxy")
async def config_proxy(proxy_data: ProxyData):
    proxy.set_proxies(proxy_data.proxies)
    return {"message": "Proxy configuration set."}

# جمع‌آوری اطلاعات از کاربران
class UserRequest(BaseModel):
    usernames: List[str]

@app.post("/search_users")
async def search_users(user_request: UserRequest):
    data = crawler.get_user_tweets(user_request.usernames)
    return data

# جمع‌آوری اطلاعات بر اساس کلمات کلیدی
class KeywordsRequest(BaseModel):
    keywords: List[str]

@app.post("/keywords_search")
async def keywords_search(keywords_request: KeywordsRequest):
    data = crawler.search_by_keywords(keywords_request.keywords)
    return data
