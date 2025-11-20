#!/usr/bin/env python3
"""
Deep Learning Sandbox - Setup Verification Script

Run this script to verify that your conda environment is set up correctly
and all dependencies are working.

Usage:
    conda activate dl-sandbox
    python scripts/verify_setup.py
"""

import sys
import warnings
warnings.filterwarnings('ignore')

def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_success(text):
    """Print success message."""
    print(f"✓ {text}")

def print_error(text):
    """Print error message."""
    print(f"✗ {text}")

def print_info(text):
    """Print info message."""
    print(f"  {text}")

def check_python():
    """Check Python version and virtual environment."""
    print_header("Python Environment")

    # Check Python version
    version = sys.version_info
    print_info(f"Python {version.major}.{version.minor}.{version.micro}")
    print_info(f"Executable: {sys.executable}")

    # Check if in virtual environment
    if 'dl-sandbox' in sys.executable or 'dl-sandbox' in sys.prefix:
        print_success("Running in dl-sandbox virtual environment")
        return True
    else:
        print_error("NOT running in dl-sandbox environment!")
        print_info("Please activate: conda activate dl-sandbox")
        return False

def check_core_libraries():
    """Check core data science libraries."""
    print_header("Core Libraries")

    try:
        import numpy as np
        print_success(f"NumPy {np.__version__}")
    except ImportError:
        print_error("NumPy not installed")
        return False

    try:
        import pandas as pd
        print_success(f"Pandas {pd.__version__}")
    except ImportError:
        print_error("Pandas not installed")
        return False

    try:
        import matplotlib
        print_success(f"Matplotlib {matplotlib.__version__}")
    except ImportError:
        print_error("Matplotlib not installed")
        return False

    try:
        import seaborn
        print_success(f"Seaborn {seaborn.__version__}")
    except ImportError:
        print_error("Seaborn not installed")
        return False

    return True

def check_pytorch():
    """Check PyTorch installation and device availability."""
    print_header("PyTorch & Hardware Acceleration")

    try:
        import torch
        print_success(f"PyTorch {torch.__version__}")
    except ImportError:
        print_error("PyTorch not installed")
        return False

    # Check available devices
    print_info("\nAvailable devices:")
    print_info("  CPU: Yes")

    cuda_available = torch.cuda.is_available()
    mps_available = torch.backends.mps.is_available()

    print_info(f"  CUDA (NVIDIA GPU): {'Yes' if cuda_available else 'No'}")
    print_info(f"  MPS (Apple Silicon): {'Yes' if mps_available else 'No'}")

    # Determine and test best device
    if cuda_available:
        device = 'cuda'
        gpu_name = torch.cuda.get_device_name(0)
        print_success(f"Using CUDA GPU: {gpu_name}")
    elif mps_available:
        device = 'mps'
        print_success("Using Apple Silicon MPS acceleration")
    else:
        device = 'cpu'
        print_info("Using CPU (no GPU acceleration)")

    # Test tensor operations
    try:
        x = torch.randn(100, 100, device=device)
        y = torch.matmul(x, x)
        print_success(f"Tensor operations working on {device}")
    except Exception as e:
        print_error(f"Tensor operations failed: {e}")
        return False

    return True

def check_ml_libraries():
    """Check machine learning libraries."""
    print_header("Machine Learning Libraries")

    try:
        import sklearn
        print_success(f"scikit-learn {sklearn.__version__}")
    except ImportError:
        print_error("scikit-learn not installed")
        return False

    try:
        import transformers
        print_success(f"Transformers {transformers.__version__}")
    except ImportError:
        print_error("Transformers not installed")
        return False

    try:
        import tokenizers
        print_success(f"Tokenizers {tokenizers.__version__}")
    except ImportError:
        print_error("Tokenizers not installed")
        return False

    try:
        import datasets
        print_success(f"Datasets {datasets.__version__}")
    except ImportError:
        print_error("Datasets not installed")
        return False

    return True

def check_jupyter():
    """Check Jupyter installation."""
    print_header("Jupyter Environment")

    try:
        import jupyter
        print_success("Jupyter installed")
    except ImportError:
        print_error("Jupyter not installed")
        return False

    try:
        import jupyterlab
        print_success("JupyterLab installed")
    except ImportError:
        print_error("JupyterLab not installed")
        return False

    try:
        import notebook
        print_success("Jupyter Notebook installed")
    except ImportError:
        print_error("Jupyter Notebook not installed")
        return False

    return True

def check_utilities():
    """Check utility libraries."""
    print_header("Utility Libraries")

    try:
        import tqdm
        print_success("tqdm (progress bars)")
    except ImportError:
        print_error("tqdm not installed")
        return False

    try:
        import tensorboard
        print_success("TensorBoard")
    except ImportError:
        print_error("TensorBoard not installed")
        return False

    try:
        import einops
        print_success("einops (tensor operations)")
    except ImportError:
        print_error("einops not installed")
        return False

    return True

def main():
    """Run all verification checks."""
    print("\n" + "=" * 60)
    print("  Deep Learning Sandbox - Setup Verification")
    print("=" * 60)

    all_passed = True

    # Run all checks
    all_passed &= check_python()
    all_passed &= check_core_libraries()
    all_passed &= check_pytorch()
    all_passed &= check_ml_libraries()
    all_passed &= check_jupyter()
    all_passed &= check_utilities()

    # Final summary
    print_header("Verification Summary")

    if all_passed:
        print_success("All checks passed! Your environment is ready.")
        print_info("\nNext steps:")
        print_info("  1. Start Jupyter Lab: jupyter lab")
        print_info("  2. Open: notebooks/00-getting-started.ipynb")
        print_info("  3. Start learning!")
        return 0
    else:
        print_error("Some checks failed!")
        print_info("\nTry recreating the environment:")
        print_info("  conda env remove -n dl-sandbox")
        print_info("  ./setup.sh")
        return 1

if __name__ == "__main__":
    sys.exit(main())
