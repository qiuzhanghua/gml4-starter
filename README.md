# GLM4 Starter

## Requirement
- Python 3.10
- pytorch 2.5.0

## Copy files from github.com/thudm/glm-4/basic_demo
- glm_server.py
- glm4v_server.py

## Install dependencies
```bash
pip install click uvicorn requests fastapi pydantic peft pathlib vllm sse_starlette
## maybe more
```

## Run

```bash
# for glm-4v
python app.py
# for glm-4
python app.py -m glm-4
```
