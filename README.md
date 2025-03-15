# CodeSandbox (remote code execution) with docker engine

## <b>Note:</b> This has been made for educational purpose only, and is not intended to be used in Production!

<p>
  This is an isolated Code sandbox engine that allows remote code execution by simply calling a REST API from the web, where user 
  can write code in some programming language and call the api to run the code in an isolated environment (which is to make sure no
  malcious code executes on the server!). The Code is run through a few instances of Docker images running in the background with server
  and each of these instances are running code as per the programming language.
</p>

<div>
  <img height="120" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" alt="docker" />
  <img height="120" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" />
  <img height="120" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg" alt="fastapi" />
</div>

<div>  
  <h1><b>Build instructions</b></h1>
  <ol>
    <li>Make sure to initialize all the dependencies including Docker</li>
    <li>
      run the python script
      ```
        python3 buildscript.py
      ```
      <p>This will initialize all the docker images, so that dependencies will be cached.</p>
    </li>
    <li>
      <p>A server will start after at 8000 PORT, leading to webpage where you can write code through HTML textarea input. You can
        choose programming languages like python, nodejs, C as of now (hoping to add more in future!).
       One submitting, the output will be redirected as JSON, which shows the output of code snippet.
      </p>
    </li>
  </ol>
</div>
