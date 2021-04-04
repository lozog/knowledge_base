# Personal Knowledge Base

A Personal Knowledge Base is a place to store one's personal knowledge for later reference.

## Pre-Requisites

- mongodb running on port 27017
  ```bash
  brew install mongodb-community
  brew services start mongodb-community
  ```

## Installation

```bash
python3 -m pip install --upgrade pip
python3 -m venv kb-venv
source kb-venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Usage

```
export FLASK_APP=api/app.py
export FLASK_DEBUG=1
python -m flask run
```
