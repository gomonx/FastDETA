# Fast DETA { Example project }
### Make Eazy API. Power By FastAPI & Deta Cloud
### สร้าง API ง่ายๆ ด้วย FastAPI(Python) และ Deta Cloud

## Alert! DETA Change to Space!
---

## How to Install
- clone this git 
    - if you use VSCode. run command below
```terminal
$ git clone https://github.com/gomonx/FastDETA
```

- this project dev in [pycham IDE](https://www.jetbrains.com/pycharm/) Recommend!
  - edit python Interpreter. if you use pycham & has interpreter error
-  in your terminal. run commands below

```terminal
pip install -r requirements.txt
```
#### OR
```terminal
pip install fastapi
pip install "uvicorn[standard]"
```

## Serve
```terminal
uvicorn main:app --reload
```

## Deploy on Deta cloud {super Eazy}
- for new user. go to [DETA](https://www.deta.sh) > sing up & create default project first
- Read [How to Deploy..](https://fastapi.tiangolo.com/deployment/deta) or use code below

### Use DETA CLI {DETA Change to SPACE}

#### Install Deta SPACE CLI (windows)
```terminal
iwr https://get.deta.dev/space-cli.ps1 -useb | iex

// legacy version
iwr https://get.deta.dev/cli.ps1 -useb | iex
```

#### Login
```terminal
space login

// legacy version
deta login
```

#### Create new micro (app)
```terminal
space new

// legacy version
deta new
```

#### You will see a JSON message similar to:
```code
{
  "name": "fastapideta",
  "runtime": "python3.7",
  "endpoint": "https://fast.deta.dev/",
  "visor": "enabled",
  "http_auth": "enabled"
}
```
Now open your browser in your endpoint URL. In the example above it was https://fast.deta.dev/, but yours will be different

#### Pushing Changes
```code
space push

// legacy version
deta push
```
---

### Deta CLI Reference [read more..](https://docs.deta.sh/docs/cli/commands/)


## Have a good days

