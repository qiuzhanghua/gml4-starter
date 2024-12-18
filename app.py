import logging
import logging.config
import os
import subprocess

import click
import yaml

from utils.hf_cache import find_hf_hub_dir, find_hf_home_dir, find_xdg_cache_home


@click.command()
@click.option("--model", "-m", help="Models", type=click.Choice(["glm-4", "glm-4v"], case_sensitive=False),
              default="glm-4v", )
def main(model):
    current_file_path = os.path.abspath(__file__)
    log_dir = os.path.join(os.path.dirname(current_file_path), "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open("config/logging.yaml", "r", encoding="utf8") as f:
        logging_config = yaml.safe_load(f)
        logging.config.dictConfig(logging_config)
        logger = logging.getLogger("app")

    base_dir = find_hf_hub_dir()
    if base_dir is None:
        hf_home = find_hf_home_dir()
        if hf_home is None:
            xdg_cache_home = find_xdg_cache_home()
            if xdg_cache_home is None:
                logger.error("Could not find a suitable cache directory.")
                return
            else:
                base_dir = os.path.join(xdg_cache_home, "huggingface", "hub")
        else:
            base_dir = os.path.join(hf_home, "hub")

    if base_dir is None:
        logger.error("Could not find a suitable cache directory.")
        return

    if model == "glm-4v":
        model = "THUDM/glm-4v-9b"
    elif model == "glm-4":
        model = "THUDM/glm-4-9b-chat"

    model_path = "models--" + model.replace("/", "--")

    model_dir = os.path.join(base_dir, model_path)

    if not os.path.exists(model_dir):
        logger.error(f"Model directory not found: {model_dir}")
        return

    with open(os.path.join(model_dir, "refs", "main"), "r", encoding="utf-8") as f:
        oid = f.read().replace("\n", "")

    lfs_dir = os.path.join(model_dir, "snapshots", oid)
    if not os.path.exists(lfs_dir):
        logger.error(f"Model directory not found: {lfs_dir}")
        return

    if '4v' in model:
        subprocess.run(["python", "glm4v_server.py", lfs_dir])
    else:
        subprocess.run(["python", "glm_server.py", lfs_dir])


if __name__ == '__main__':
    main()
