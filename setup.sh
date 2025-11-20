#!/bin/bash

# Deep Learning Sandbox - Environment Setup Script
# This script creates an isolated conda virtual environment for the project

set -e  # Exit on error

echo "=================================="
echo "Deep Learning Sandbox Setup"
echo "=================================="
echo ""

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "❌ Error: conda is not installed or not in PATH"
    echo ""
    echo "Please install Miniconda or Anaconda:"
    echo "  https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

echo "✓ Conda found: $(conda --version)"
echo ""

# Check if environment already exists
if conda env list | grep -q "^dl-sandbox "; then
    echo "⚠️  Environment 'dl-sandbox' already exists"
    read -p "Do you want to remove and recreate it? (y/N): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing environment..."
        conda env remove -n dl-sandbox -y
    else
        echo "Setup cancelled. To activate existing environment, run:"
        echo "  conda activate dl-sandbox"
        exit 0
    fi
fi

# Create the conda environment
echo "Creating virtual environment 'dl-sandbox' from environment.yml..."
echo "This may take a few minutes..."
echo ""
conda env create -f environment.yml

echo ""
echo "=================================="
echo "✓ Setup Complete!"
echo "=================================="
echo ""
echo "Your isolated virtual environment is ready!"
echo ""
echo "To activate the environment, run:"
echo "  conda activate dl-sandbox"
echo ""
echo "To deactivate when done:"
echo "  conda deactivate"
echo ""
echo "To verify the setup:"
echo "  conda activate dl-sandbox"
echo "  python scripts/verify_setup.py"
echo ""
echo "To start Jupyter Lab:"
echo "  conda activate dl-sandbox"
echo "  jupyter lab"
echo ""
