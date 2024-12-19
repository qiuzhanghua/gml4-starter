# GLM4 Starter

## Requirement
- Python 3.10
- pytorch 2.5.0

## Dowload models
```bash
huggingface-cli download THUDM/glm-4-9b-chat
huggingface-cli download THUDM/glm-4v-9b
```

## Copy files from github.com/thudm/glm-4/basic_demo
- glm_server.py
- glm4v_server.py
and add Network Port logic.

## Install dependencies
```bash
pip install click uvicorn requests fastapi pydantic peft pathlib vllm sse_starlette
## maybe more
```

## Run

```bash
# for glm-4v
python app.py -p 8001
# for glm-4
python app.py -m glm4 -p 8002
```
