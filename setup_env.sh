#!/bin/bash

# Define environment name
VENV_NAME="venv"

echo "--- 🚀 Setting up Object Detection Environment ---"

# 1. Check for Python 3.11, fallback to python3
if command -v python3.11 &>/dev/null; then
    PYTHON_CMD="python3.11"
    echo "✅ Python 3.11 found."
else
    PYTHON_CMD="python3"
    echo "⚠️  Python 3.11 not found. Using system 'python3' instead."
fi

# 2. Create Virtual Environment
if [ ! -d "$VENV_NAME" ]; then
    echo "📦 Creating virtual environment '$VENV_NAME'..."
    $PYTHON_CMD -m venv $VENV_NAME
else
    echo "ℹ️  Virtual environment '$VENV_NAME' already exists."
fi

# 3. Activate and Install
echo "🔌 Activating environment..."
source $VENV_NAME/bin/activate

echo "⬇️  Installing dependencies from requirements.txt..."
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Error: requirements.txt not found!"
fi

echo "--- Setup Complete! ---"
echo "To activate manually later, run: source $VENV_NAME/bin/activate"