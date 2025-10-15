#!/bin/bash

echo "Setting up blog platform project..."

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

echo "Setup complete! Activate virtual environment with:"
echo "source venv/bin/activate  # On Windows: venv\Scripts\activate"