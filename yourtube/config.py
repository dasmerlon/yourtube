"""Config values for pollbot."""
import logging
import os
import sys

import toml

default_config = {
    "youtube": {"api_key": "Your api key here"},
    "database": {
        "sql_uri": "sqlite:///yourtube.db",
    },
    "logging": {
        "sentry_enabled": False,
        "sentry_token": "",
        "log_level": logging.INFO,
        "debug": False,
    },
}

config_path = os.path.expanduser("./config.toml")

if not os.path.exists(config_path):
    with open(config_path, "w") as file_descriptor:
        toml.dump(default_config, file_descriptor)
    print(f"Please adjust the configuration file at '{config_path}'")
    sys.exit(1)
else:
    config = toml.load(config_path)

    # Set default values for any missing keys in the loaded config
    for key, category in default_config.items():
        for option, value in category.items():
            if option not in config[key]:
                config[key][option] = value
