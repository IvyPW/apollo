#!/bin/bash
cd ~/repos/personal/apollo
# Setup your python virtual environment
python3 -m venv .venv
source .venv/bin/activate


# Install the dependencies
pip3 install -r requirements.txt

python3 src/mocktester.py