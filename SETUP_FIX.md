# Fix for "No module named 'pkg_resources'" Error

## Problem
When running the Jupyter notebook, you may encounter the error:
```
ModuleNotFoundError: No module named 'pkg_resources'
```

This error occurs because the CrewAI library uses the deprecated `pkg_resources` module, which is being phased out in newer Python versions.

## Solutions

### Solution 1: Install/Upgrade setuptools (Recommended)
```bash
# Activate your virtual environment first
source venv/bin/activate

# Upgrade setuptools to ensure pkg_resources is available
pip install --upgrade setuptools

# If that doesn't work, try installing setuptools directly
pip install setuptools>=68.0.0
```

### Solution 2: Install setuptools explicitly
```bash
# If you're not using a virtual environment
pip install --user setuptools>=68.0.0

# Or system-wide (requires admin privileges)
sudo pip install setuptools>=68.0.0
```

### Solution 3: Use conda (if using Anaconda/Miniconda)
```bash
conda install setuptools
```

### Solution 4: Reinstall Python packages
Sometimes the virtual environment gets corrupted. Try recreating it:
```bash
# Remove existing virtual environment
rm -rf venv

# Create new virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Upgrade pip and setuptools first
pip install --upgrade pip setuptools wheel

# Install project requirements
pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29
```

## Alternative: Use importlib.metadata (For Advanced Users)
If you want to patch the CrewAI library to use the modern alternative, you can modify the telemetry file:

1. Find the file: `venv/lib/python3.12/site-packages/crewai/telemetry/telemetry.py`
2. Replace line 7: `import pkg_resources` with:
   ```python
   try:
       import pkg_resources
   except ImportError:
       # Fallback for newer Python versions
       import importlib.metadata as pkg_resources
   ```

## Verification
After applying any of these solutions, test the import:
```python
# In Python shell or Jupyter notebook
from crewai import Agent, Task, Crew
print("CrewAI imported successfully!")
```