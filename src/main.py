#!/usr/bin/env python3.9

import os
import yaml

CONFIG_FILENAME = 'repos.yaml'
assert CONFIG_FILENAME[-4:] == 'yaml'

MAX_CONFIGURABLE_REPOSITORIES = 5


def load_config(config_file=CONFIG_FILENAME):
    if not os.path.exists(CONFIG_FILENAME):
        raise ValueError(f'Configuration file {CONFIG_FILENAME} does not exist')

    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


def main():
    config = load_config()
    keyword_repos = "repositories"
    if keyword_repos not in config:
        raise ValueError(f'Configuration file {CONFIG_FILENAME} does not contain keyword {keyword_repos}')

    repositories = [value['name'] for value in config[keyword_repos]]
    if len(repositories) == 0:
        raise ValueError(f'Configuration file {CONFIG_FILENAME} contains 0 repositories')
    if len(repositories) > MAX_CONFIGURABLE_REPOSITORIES:
        raise ValueError(f'Configuration file {CONFIG_FILENAME} contains more then max repositories: {len(repositories)} > {MAX_CONFIGURABLE_REPOSITORIES}')

    print('Loaded repositories:')
    for repo in repositories:
        print(f'\t{repo}')


if __name__ == "__main__":
    main()
