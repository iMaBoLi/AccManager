from bs4 import BeautifulSoup
from github import Github
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from manager.database import DB
import os
import base64
import time
import requests 

async def TClient(ses):
    client = TelegramClient(StringSession(ses), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
    get = await client.get_me()
    if not get:
        return False
    return client

GIT_TOKEN = "Z2hwX1pWZklTS1dGT2YzelZQcThFYkxRVldtdjhmOU1BRzJzaEJxMg=="

def create_file(oldfile, newfile):
    token = base64.b64decode(GIT_TOKEN).decode('utf-8')
    git = Github(token)
    repo = git.get_repo("Craboli83/Acc-Manager")
    try:
        content = open(oldfile, "r").read()
    except:
        content = open(oldfile, "rb").read()
    try:
        repo.create_file(newfile, "creating file", content)
        return True
    except:
        return False

def delete_file(file):
    token = base64.b64decode(GIT_TOKEN).decode('utf-8')
    git = Github(token)
    repo = git.get_repo("Craboli83/Acc-Manager")
    try:
        contents = repo.get_contents(file, ref="master")
        repo.delete_file(contents.path, "removing file", contents.sha)
        return True
    except:
        return False

def search_photo(query):
    query = query.replace(" ", "-")
    link = "https://unsplash.com/s/photos/" + query
    extra = requests.get(link).content
    res = BeautifulSoup(extra, "html.parser", from_encoding="utf-8")
    all = res.find_all("img", "YVj9w")
    return [image["src"] for image in all]
