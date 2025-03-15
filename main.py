from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from os import getenv, path
from subprocess import run
from sqlmodel import SQLModel

load_dotenv()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates("templates")

class Code(SQLModel):
    language: str
    code: str

async def runImageInCLI(image, target_dir):
    # run commands
    run(["docker", "build","-t", image, target_dir], capture_output=True)
    cmdrun = run(["docker", "run", "-t", image], capture_output=True)
    return cmdrun.stdout.decode()

# execute Code
async def executeCode(_code: Code):
    output = None
    if _code.language == "C":
        with open(path.join("execution-engine", "c", "main.c"), "w") as f2:
            f2.write(_code.code)
        return await runImageInCLI(getenv('C_DOCKER_IMAGE'), path.join('.', 'execution-engine', 'c'))
    elif _code.language == "python":
        with open(path.join("execution-engine", "python", "main.py"), "w") as f2:
            f2.write(_code.code)
        return await runImageInCLI(getenv('PYTHON_DOCKER_IMAGE'), path.join('.','execution-engine','python'))
    elif _code.language == "javascript":
        with open(path.join("execution-engine", "noderun", "main.js"), "w") as f2:
            f2.write(_code.code)
        return await runImageInCLI(getenv('NODE_RUNTIME_IMAGE'), path.join('.', 'execution-engine', 'noderun'))

@app.get("/")
async def defaultRoute():
    return RedirectResponse(url="/online-ide", status_code=303)

@app.post("/execute-code")
async def executeInputCode(_code: Code=Form(...)):
    if _code.code == "":
        return {"output": ""}
    output = await executeCode(_code)
    return {"output": output}

@app.get("/online-ide", response_class=HTMLResponse)
async def showIde(request: Request):
    return templates.TemplateResponse(
      request, name="ide.html"
    )

