import logging
import logging.config
import os
import subprocess

import click
import yaml

from utils.hf_cache import find_hf_hub_dir, find_hf_home_dir, find_model_dir, find_xdg_cache_home


@click.command()
@click.option("--model", "-m", help="Model Name", type=click.Choice(["glm4", "glm4v"], case_sensitive=False),
              default="glm4v", 
              show_default=True)
@click.option("--port", "-p", help="Port Number", type=int, default=8000, show_default=True)
def main(model, port):
    current_file_path = os.path.abspath(__file__)
    log_dir = os.path.join(os.path.dirname(current_file_path), "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open("config/logging.yaml", "r", encoding="utf8") as f:
        logging_config = yaml.safe_load(f)
        logging.config.dictConfig(logging_config)
        logger = logging.getLogger("app")


    if model == "glm4v":
        model = "THUDM/glm-4v-9b"
    elif model == "glm4":
        model = "THUDM/glm-4-9b-chat"

    lfs_dir = find_model_dir(model)

    if '4v' in model:
        subprocess.run(["python", "glm4v_server.py", lfs_dir, str(port)])
    else:
        subprocess.run(["python", "glm_server.py", lfs_dir, str(port)])


if __name__ == '__main__':
    main()
