#!/usr/bin/env bash

set -e

virtual_env_name=".$(basename $(pwd))"

which python3
if [ $? -ne 0 ]; then
  echo "INFO: Installing python 3"
  brew install python3
fi

if [ ! -d $virtual_env_name ]; then
  echo "INFO: Creating virtual env folder in current directory"
  python3 -m venv $virtual_env_name
fi

echo "Activating virtual environment"
source $virtual_env_name/bin/activate

pip3 install -r requirements.txt

# python -m ipykernel install --user --name=${virtual_env_name}

echo "Done!"