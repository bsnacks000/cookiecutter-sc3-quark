#!/usr/bin/env python
import os
import pathlib


if __name__ == '__main__':
    project_dirpath = pathlib.Path(os.path.realpath(os.path.curdir))

    if '{{ cookiecutter.git_init}}'.lower() == 'y': 
        os.chdir(project_dirpath)
        os.system('git init')

