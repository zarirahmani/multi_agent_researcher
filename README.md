# Multi-Agent-Researcher

A multi-agent research system using CrewAI for collaborative research and article writing.

## Quick Setup

### Option 1: Automatic Setup (Recommended)
Run the setup script:
```bash
chmod +x setup_environment.sh
./setup_environment.sh
```

### Option 2: Manual Setup
1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install requirements:
```bash
pip install --upgrade setuptools
pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29
pip install jupyter ipykernel
```

3. Register Jupyter kernel:
```bash
python -m ipykernel install --user --name=venv --display-name="Multi-Agent Researcher (venv)"
```

## Usage
1. Start Jupyter: `jupyter notebook`
2. Open `researcher.ipynb`
3. Select "Multi-Agent Researcher (venv)" kernel
4. Run the cells

## Troubleshooting
If you encounter "No module named 'pkg_resources'" error, see [SETUP_FIX.md](SETUP_FIX.md) for detailed solutions.