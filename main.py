from fastapi import FastAPI, Request, Query


appname = 'borderlands'

app = FastAPI()

# Root
@app.get('/')
async def root(requests: Request):
    return {'Hello': 'WORLD!'}
