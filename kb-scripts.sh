#!/usr/bin/env bash

set -e # stop execution on errors

_load-venv() {
  # shellcheck disable=SC1091
  . kb-venv/bin/activate
}

init() {
  python3 -m pip install --upgrade pip
  python3 -m venv kb-venv
  _load-venv
  pip3 install --upgrade pip
  pip3 install -r requirements.txt
}

serve() {
  export FLASK_APP=api/app.py
  export FLASK_DEBUG=1
  _load-venv
  python3 api/app.py
}

# Allow running tasks from commandline, e.g. `./kb serve`
"$@" || error_code=$?
