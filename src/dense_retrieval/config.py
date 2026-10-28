from pathlib import Path 
from typing import Any
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "configs" / "train.yaml"

def load_config(
        config_path: str | Path = DEFAULT_CONFIG_PATH
) -> dict[str, Any]:
    """Loads the configuration from the project YAML file"""

    config_path = Path(config_path)

    if not config_path.is_file():
        raise FileNotFoundError(
            f"Config File not found at {config_path}"
        )

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError(
            f"Not a YAML mapping in config file: {config_path}"
        )

    return config