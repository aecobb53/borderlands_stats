from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse


appname = 'borderlands'

app = FastAPI()

# Root
@app.get('/')
async def root(requests: Request):
    return {'Hello': 'WORLD!'}

@app.get('/current-builds', response_class=HTMLResponse)
async def current_builds(requests: Request):
    with open('old_class_builds.html', 'r') as hf:
        html_content = hf.read()
    return HTMLResponse(content=html_content, status_code=200)

"""
More website sto look at
https://borderlands.fandom.com/wiki/Borderlands_3_Weapons
https://borderlands.fandom.com/wiki/Borderlands_3_Gear
"""
