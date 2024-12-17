# Description: Cache utilities for huggingface.

def find_hf_home_dir() -> str | None:
    """
    Find the huggingface home directory.
    """
    import os
    import logging

    logger = logging.getLogger(__name__)

    result = None
    if "HF_HOME" in os.environ:
        result = os.environ["HF_HOME"]
        if os.path.exists(result) and os.path.isdir(result):
            return result
        else:
            logger.warning(f"Invalid HF_HOME directory: {result}")
    result = os.path.join(os.path.expanduser("~"), ".cache", "huggingface")
    if os.path.exists(result) and os.path.isdir(result):
        return result
    else:
        logger.warning(f"Invalid default HuggingFace home directory: {result}")
    return None


def find_hf_hub_dir() -> str | None:
    """
    Find the huggingface hub cache directory.
    """
    import os
    import logging

    logger = logging.getLogger(__name__)

    result = None
    if "HUGGINGFACE_HUB_CACHE" in os.environ:
        result = os.environ["HUGGINGFACE_HUB_CACHE"]
        if os.path.exists(result) and os.path.isdir(result):
            return result
        else:
            logger.warning(f"Invalid HUGGINGFACE_HUB_CACHE directory: {result}")
    if "HF_HOME" in os.environ:
        result = os.path.join(os.environ["HF_HOME"], "hub")
        if os.path.exists(result) and os.path.isdir(result):
            return result
        else:
            logger.warning(f"Invalid HF_HOME directory: {result}")
    result = os.path.join(os.path.expanduser("~"), ".cache", "huggingface", "hub")
    if os.path.exists(result) and os.path.isdir(result):
        return result
    else:
        logger.warning(f"Invalid default HuggingFace Hub directory: {result}")
    return None


def find_hf_datasets_dir() -> str | None:
    """
    Find the huggingface datasets cache directory.
    """
    import os
    import logging

    logger = logging.getLogger(__name__)

    result = None
    if "HF_DATASETS_CACHE" in os.environ:
        result = os.environ["HF_DATASETS_CACHE"]
        if os.path.exists(result) and os.path.isdir(result):
            return result
        else:
            logger.warning(f"Invalid HF_DATASETS_CACHE directory: {result}")
    if "HF_HOME" in os.environ:
        result = os.path.join(os.environ["HF_HOME"], "datasets")
        if os.path.exists(result) and os.path.isdir(result):
            return result
        else:
            logger.warning(f"Invalid HF_HOME directory: {result}")
    result = os.path.join(os.path.expanduser("~"), ".cache", "huggingface", "datasets")
    if os.path.exists(result) and os.path.isdir(result):
        return result
    else:
        logger.warning(f"Invalid default HuggingFace datasets directory: {result}")
    return None


def find_transformers_dir() -> str | None:
    """
    Find the huggingface transformers cache directory.
    """
    import os
    import logging

    logger = logging.getLogger(__name__)

    result = None
    if "TRANSFORMERS_CACHE" in os.environ:
        result = os.environ["TRANSFORMERS_CACHE"]
        if os.path.exists(result) and os.path.isdir(result):
            return result
        else:
            logger.warning(f"Invalid TRANSFORMERS_CACHE directory: {result}")
    if "HF_HOME" in os.environ:
        result = os.path.join(os.environ["HF_HOME"], "transformers")
        if os.path.exists(result) and os.path.isdir(result):
            return result
        else:
            logger.warning(f"Invalid HF_HOME directory: {result}")
    result = os.path.join(os.path.expanduser("~"), ".cache", "huggingface", "transformers")
    if os.path.exists(result) and os.path.isdir(result):
        return result
    else:
        logger.warning(f"Invalid default HuggingFace transformers directory: {result}")
    return None


def find_xdg_cache_home() -> str | None:
    """
    Find the XDG cache directory.
    """
    import os
    import logging

    logger = logging.getLogger(__name__)

    result = None
    if "XDG_CACHE_HOME" in os.environ:
        result = os.environ["XDG_CACHE_HOME"]
        if os.path.exists(result) and os.path.isdir(result):
            return result
        else:
            logger.warning(f"Invalid XDG_CACHE_HOME directory: {result}")
    result = os.path.join(os.path.expanduser("~"), ".cache")
    if os.path.exists(result) and os.path.isdir(result):
        return result
    else:
        logger.warning(f"Invalid default XDG cache directory: {result}")
    return None

# HF_HOME                 ~/.cache/huggingface
# HUGGINGFACE_HUB_CACHE   ~/.cache/huggingface/hub
# HF_DATASETS_CACHE       ~/.cache/huggingface/datasets
# TRANSFORMERS_CACHE      ~/.cache/huggingface/transformers
# XDG_CACHE_HOME          ~/.cache
