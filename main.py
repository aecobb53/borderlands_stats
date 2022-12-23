from fastapi import FastAPI, Request, Query


appname = 'borderlands'

app = FastAPI()

# Root
@app.get('/')
async def root(requests: Request):
    return {'Hello': 'WORLD!'}

@app.get('/current-builds')
async def current_builds(requests: Request):
    with open('old_class_builds.html', 'r') as hf:
        builds = hf.read()
    return builds

