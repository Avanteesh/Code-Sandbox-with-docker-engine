from subprocess import run
from dotenv import load_dotenv
from os import path,getenv

PYTHON_IMAGE_PATH = path.join(".", "execution-engine","python")
C_IMAGE_PATH = path.join(".", "execution-engine", "c")
NODE_IMAGE_PATH = path.join(".", "execution-engine", "noderun")

load_dotenv()
if __name__ == "__main__":
    run(["docker","build","-t",getenv('C_DOCKER_IMAGE'),C_IMAGE_PATH])
    run(["docker", "build", "-t", getenv('PYTHON_DOCKER_IMAGE'), PYTHON_IMAGE_PATH])
    run(["docker", "build", "-t", getenv('NODE_RUNTIME_IMAGE'), NODE_IMAGE_PATH])            
    run(["fastapi", "dev", "main.py"])
