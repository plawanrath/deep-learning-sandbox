# Deep Learning Sandbox

## Project Overview
This is a hands-on deep learning playground designed for learning and experimenting with deep learning concepts, ranging from basic classifiers to building Large Language Models (LLMs) from scratch.

The project is structured as a progressive learning path:
1.  **Classifiers:** Basic classification algorithms.
2.  **Neural Networks:** Feed-forward NNs and CNNs.
3.  **RNNs & LSTMs:** Sequential models and time series.
4.  **Transformers:** Attention mechanisms and modern architectures.
5.  **LLM from Scratch:** End-to-end language model implementation.

## Technologies & Architecture
*   **Language:** Python 3.11
*   **Framework:** PyTorch >= 2.0.0 (supports MPS for Apple Silicon and CUDA for NVIDIA GPUs)
*   **Environment Management:** Conda
*   **Core Libraries:** NumPy, Pandas, Scikit-learn, SciPy
*   **Visualization:** Matplotlib, Seaborn, Plotly, TensorBoard
*   **NLP/LLM Ecosystem:** Hugging Face Transformers, Tokenizers, Datasets, Accelerate, Tiktoken, SentencePiece, Einops

## Directory Structure
*   `classifiers/`: Basic ML classifiers.
*   `neural-networks/`: Feed-forward NNs and CNNs.
*   `rnns-lstm/`: RNNs, LSTMs, and GRUs.
*   `transformers/`: Transformer architectures and attention mechanisms.
*   `llm-from-scratch/`: Final project - LLM implementation.
*   `notebooks/`: Jupyter notebooks for interactive exploration and learning.
*   `scripts/`: Reusable Python scripts and reproducible experiments.
*   `utils/`: Shared helper functions.
*   `data/`: Datasets (gitignored).
*   `models/`: Saved model weights (gitignored).
*   `setup.sh`: Automated environment setup script.
*   `environment.yml`: Conda environment specification.

## Building and Running

### Prerequisites
*   **Conda:** Miniconda or Anaconda installed.
*   **OS:** macOS (Apple Silicon or Intel) or Linux/Windows (with appropriate Conda setup).

### Environment Setup
1.  **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd deep-learning-sandbox
    ```
2.  **Run the setup script:**
    ```bash
    ./setup.sh
    ```
    This script creates a Conda environment named `dl-sandbox`.

3.  **Verify installation:**
    ```bash
    conda activate dl-sandbox
    python scripts/verify_setup.py
    ```

### Daily Workflow
**Always activate the environment first:**
```bash
conda activate dl-sandbox
```

**Running Notebooks:**
```bash
jupyter lab
```
(Then open `notebooks/00-getting-started.ipynb` to begin).

**Running Scripts:**
```bash
python scripts/<script_name>.py
```

**Managing Dependencies:**
*   **Update:** If `environment.yml` changes, run `conda env update -f environment.yml --prune`.
*   **Recreate:** Run `conda env remove -n dl-sandbox` followed by `./setup.sh`.

## Development Conventions

*   **Environment:** All development **must** happen inside the `dl-sandbox` environment.
*   **File Organization:**
    *   Use **notebooks** for exploration, visualization, and step-by-step learning.
    *   Use **scripts** for production-ready code, training loops, and reusable logic.
    *   Use **utils** for common functions shared across modules.
*   **Data & Models:** Large files (datasets, model checkpoints) go in `data/` and `models/`. These are ignored by git. **Do not commit them.**
*   **Code Style:**
    *   **Formatting:** Uses `black`.
    *   **Linting:** Uses `pylint`.
*   **Hardware Acceleration:** The project is optimized for Apple Silicon (MPS) but supports CUDA and CPU. Use `torch.backends.mps.is_available()` or `torch.cuda.is_available()` to check for hardware acceleration.
