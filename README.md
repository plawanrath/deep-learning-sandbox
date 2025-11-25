# Deep Learning Sandbox 🧪

A hands-on playground for learning deep learning concepts from fundamentals to building an LLM/SLM from scratch.

## 🎯 Learning Path

1. **Classifiers** → Basic classification algorithms
2. **Neural Networks** → Feed-forward NNs, CNNs
3. **RNNs & LSTMs** → Sequential models, time series
4. **Transformers** → Attention mechanisms, modern architectures
5. **LLM from Scratch** → Build a language model end-to-end

## 📁 Repository Structure

```
deep-learning-sandbox/
├── classifiers/          # Basic ML classifiers
├── neural-networks/      # FFNNs, CNNs
├── rnns-lstm/           # RNNs, LSTMs, GRUs
├── transformers/        # Attention, Transformers
├── llm-from-scratch/    # Final project - LLM/SLM
├── notebooks/           # Jupyter notebooks for exploration
├── scripts/             # Reusable Python scripts
├── utils/               # Helper functions
├── data/                # Datasets (gitignored)
└── models/              # Saved models (gitignored)
```

## 🚀 Quick Start

### Prerequisites

- **Conda** (Miniconda or Anaconda)
- macOS (Apple Silicon or Intel)

### Installing Conda (If Not Already Installed)

If you don't have conda installed, follow these steps:

**For Apple Silicon (M1/M2/M3) Macs:**
```bash
# Download Miniconda installer
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh

# Run the installer
bash Miniconda3-latest-MacOSX-arm64.sh

# Follow the prompts:
# - Press Enter to read license
# - Type 'yes' to accept
# - Press Enter for default location (~/miniconda3)
# - Type 'yes' to initialize conda

# Initialize conda for your shell
~/miniconda3/bin/conda init zsh

# Reload shell configuration
source ~/.zshrc

# Verify installation
conda --version
```

**For Intel Macs:**
```bash
# Download Miniconda installer
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

# Run the installer
bash Miniconda3-latest-MacOSX-x86_64.sh

# Follow the same prompts as above
~/miniconda3/bin/conda init zsh
source ~/.zshrc
conda --version
```

You should see `(base)` appear in your terminal prompt when conda is active.

### Setup (First Time)

**Important:** This project uses an **isolated virtual environment** to keep all dependencies separate from your system Python.

1. **Clone the repository**
   ```bash
   git clone git@github.com:plawanrath/deep-learning-sandbox.git
   cd deep-learning-sandbox
   ```

2. **Run the setup script**
   ```bash
   ./setup.sh
   ```

   This creates a conda virtual environment named `dl-sandbox` with all dependencies.

3. **Activate the environment**
   ```bash
   conda activate dl-sandbox
   ```

   ⚠️ **Always activate this environment before working on the project!**

4. **Verify the setup**
   ```bash
   python scripts/verify_setup.py
   ```

### Daily Usage

Every time you work on this project:

```bash
# 1. Activate the virtual environment
conda activate dl-sandbox

# 2. Start Jupyter Lab (for notebooks)
jupyter lab

# OR run scripts directly
python scripts/your_script.py

# 3. When done, deactivate
conda deactivate
```

## 🔧 Environment Management

### Check if environment is active
Your terminal prompt should show `(dl-sandbox)` when the environment is active.

### Recreate environment
```bash
conda env remove -n dl-sandbox
./setup.sh
```

### Update dependencies
After modifying `environment.yml`:
```bash
conda activate dl-sandbox
conda env update -f environment.yml --prune
```

### Export environment for sharing
```bash
conda env export > environment.yml
```

## 📦 Included Libraries

- **PyTorch** (with MPS support for Apple Silicon)
- **NumPy, Pandas** (data manipulation)
- **Matplotlib, Seaborn, Plotly** (visualization)
- **Jupyter Lab** (interactive notebooks)
- **scikit-learn** (ML utilities)
- **Hugging Face Transformers** (pre-trained models, tokenizers)
- **TensorBoard** (training visualization)
- **wandb** (experiment tracking)

## 🎓 Getting Started with Learning

1. Start with the getting started notebook:
   ```bash
   conda activate dl-sandbox
   jupyter lab notebooks/00-getting-started.ipynb
   ```

2. Follow the learning path in order (classifiers → neural-networks → RNNs → transformers → LLM)

3. Mix notebooks (exploration) and scripts (reproducible experiments)

## 💡 Tips

- **Always work in the virtual environment** - run `conda activate dl-sandbox` first
- Keep large datasets in `data/` (gitignored)
- Save models in `models/` (gitignored)
- Use notebooks for learning and visualization
- Use scripts for reusable code and experiments
- Commit your code regularly, but not data/models

## 🖥️ Hardware Acceleration

This setup is configured for **Mac with MPS** (Metal Performance Shaders):
- Apple Silicon: Full MPS acceleration
- Intel Mac: CPU-only (still works, just slower)

PyTorch will automatically use MPS when available.

## 📚 Resources

- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Hugging Face Course](https://huggingface.co/course)
- [Dive into Deep Learning](https://d2l.ai/)
- [Neural Networks: Zero to Hero (Karpathy)](https://karpathy.ai/zero-to-hero.html)

## 🔄 Cloning to a New Machine

```bash
git clone git@github.com:plawanrath/deep-learning-sandbox.git
cd deep-learning-sandbox
./setup.sh
conda activate dl-sandbox
```

That's it! The `environment.yml` ensures identical dependencies everywhere.

---

**Remember:** Always `conda activate dl-sandbox` before working! 🎯
