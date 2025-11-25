# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A hands-on deep learning playground for learning from fundamentals to building an LLM/SLM from scratch. The project uses PyTorch with MPS (Metal Performance Shaders) support for Apple Silicon acceleration.

Learning path: Classifiers → Neural Networks → RNNs/LSTMs → Transformers → LLM from Scratch

## Environment Setup

This project uses an **isolated conda virtual environment** named `dl-sandbox`. All development must occur within this environment.

### Initial Setup
```bash
./setup.sh                          # Create environment from environment.yml
conda activate dl-sandbox           # Activate environment
python scripts/verify_setup.py      # Verify installation
```

### Daily Workflow
```bash
conda activate dl-sandbox           # Always activate first
jupyter lab                         # Start Jupyter for notebooks
# OR
python scripts/your_script.py       # Run scripts directly
```

### Environment Management
```bash
conda activate dl-sandbox                    # Activate environment
conda deactivate                             # Deactivate when done
conda env update -f environment.yml --prune  # Update after modifying environment.yml
conda env remove -n dl-sandbox               # Remove environment
```

## Directory Structure

```
deep-learning-sandbox/
├── classifiers/          # Basic ML classifiers (currently empty, planned)
├── neural-networks/      # FFNNs, CNNs (currently empty, planned)
├── rnns-lstm/           # RNNs, LSTMs, GRUs (currently empty, planned)
├── transformers/        # Attention, Transformers (currently empty, planned)
├── llm-from-scratch/    # Final project - LLM/SLM (currently empty, planned)
├── notebooks/           # Jupyter notebooks for exploration
├── scripts/             # Reusable Python scripts and utilities
├── utils/               # Helper functions (currently empty, planned)
├── data/                # Datasets (gitignored)
└── models/              # Saved models (gitignored)
```

## Key Commands

### Verification and Testing
```bash
python scripts/verify_setup.py      # Comprehensive setup verification
```

The verify_setup.py script checks:
- Python environment (confirms dl-sandbox activation)
- Core libraries (NumPy, Pandas, Matplotlib, Seaborn)
- PyTorch installation and device availability (CPU/CUDA/MPS)
- ML libraries (scikit-learn, Transformers, Tokenizers, Datasets)
- Jupyter environment
- Utility libraries (tqdm, TensorBoard, einops)

### Jupyter Notebooks
```bash
jupyter lab                                    # Start JupyterLab
jupyter lab notebooks/00-getting-started.ipynb # Open specific notebook
```

## Key Technologies

### Core Stack
- **Python 3.11**: Base language
- **PyTorch >=2.0.0**: Deep learning framework with MPS support
- **NumPy, Pandas, SciPy**: Data manipulation
- **Matplotlib, Seaborn, Plotly**: Visualization
- **JupyterLab**: Interactive development

### ML/DL Libraries
- **scikit-learn**: Traditional ML utilities
- **Hugging Face Transformers**: Pre-trained models and tokenizers
- **Hugging Face Datasets**: Dataset utilities
- **Hugging Face Tokenizers**: Fast tokenization
- **accelerate**: Distributed training utilities

### Tokenization
- **sentencepiece**: Subword tokenization
- **tiktoken**: OpenAI's tokenizer
- **einops**: Elegant tensor operations

### Utilities
- **tqdm**: Progress bars
- **TensorBoard**: Training visualization
- **wandb**: Experiment tracking (optional)
- **black**: Code formatting
- **pylint**: Linting

## Hardware Acceleration

The project is configured for Mac with MPS (Metal Performance Shaders):
- **Apple Silicon**: Full MPS acceleration available
- **Intel Mac**: CPU-only (slower but functional)

PyTorch automatically detects and uses MPS when available. To determine the device in code:

```python
import torch

if torch.cuda.is_available():
    device = torch.device('cuda')
elif torch.backends.mps.is_available():
    device = torch.device('mps')
else:
    device = torch.device('cpu')
```

## Development Guidelines

### File Organization
- Use **notebooks/** for exploration and visualization
- Use **scripts/** for reusable code and reproducible experiments
- Store large datasets in **data/** (gitignored)
- Save trained models in **models/** (gitignored)
- Create utility functions in **utils/** for shared code

### Code Style
- Format with `black` (available in environment)
- Lint with `pylint` (available in environment)

### Git Workflow
- Commit code regularly
- **Never commit** datasets (data/) or models (models/)
- Keep .gitignore updated for large files
- **Use SSH for git operations** (not HTTPS) - the remote is configured as `git@github.com:plawanrath/deep-learning-sandbox.git`

## Important Notes

- **Always work in the virtual environment**: The prompt should show `(dl-sandbox)` when active
- **Environment isolation**: All dependencies are isolated from system Python
- **Setup verification**: Run `python scripts/verify_setup.py` after any environment changes
- **Progressive learning**: The codebase is structured for sequential learning from classifiers through to LLM development

## Getting Started Notebook

The repository includes `notebooks/00-getting-started.ipynb` which:
1. Verifies environment setup
2. Tests PyTorch and device availability
3. Demonstrates basic neural network operations
4. Validates visualization libraries
5. Confirms Hugging Face libraries installation

This notebook should run successfully before beginning any development work.
