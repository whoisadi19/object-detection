@echo off
echo --- 🚀 Setting up Object Detection Environment ---


IF NOT EXIST "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
) ELSE (
    echo ℹ️  Virtual environment already exists.
)


echo 🔌 Activating environment...
call venv\Scripts\activate


echo ⬇️  Installing dependencies...
python -m pip install --upgrade pip
if exist requirements.txt (
    pip install -r requirements.txt
    echo ✅ Dependencies installed successfully!
) else (
    echo ❌ Error: requirements.txt not found!
)

echo --- Setup Complete! ---
echo To activate manually later, run: venv\Scripts\activate
pause