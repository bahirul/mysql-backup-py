# mysql-backup-py

Python script for backup mysql databases.

[![mysql-backup-py](https://asciinema.org/a/423581.svg)](https://asciinema.org/a/423581)

## Install

- use virtualenv python3 (recommended) or globaly install require module with `pip`

## with virtualenv

- activate virtualenv python3

    - run `source ./venv/bin/activate`

- required modules install

    - run `pip install -r requirements.txt`

## direclty
- required modules install (globaly)
    - run `pip install -r requirements.txt`

## usage

- run script
    - run `python3 run.py`

- clean folder
    - run `python3 flush.py`

- restore backup
    - run `python3 restore.py`

- restore backup (force/skip errors)
    - run `python3 restore.py --force`

## Scheduler

- run scheduler with nohup
    - run `nohup python3 scheduler.py &`

- see scheduler process PID
    - run `ps ax | grep scheduler.py`

- stop scheduler
    - run `kill PID`
