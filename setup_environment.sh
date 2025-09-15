#!/bin/bash
# setup_environment.sh - Setup script to fix pkg_resources issue

echo "Setting up the Multi-Agent Researcher environment..."

# Check if Python3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip and setuptools to ensure pkg_resources is available
echo "Upgrading pip and setuptools..."
pip install --upgrade pip setuptools wheel

# Install project requirements
echo "Installing project requirements..."
pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29

# Install Jupyter if not already installed
pip install jupyter ipykernel

# Register the virtual environment as a Jupyter kernel
python -m ipykernel install --user --name=venv --display-name="Multi-Agent Researcher (venv)"

# Test the installation
echo "Testing the installation..."
python -c "from crewai import Agent, Task, Crew; print('SUCCESS: All packages installed correctly!')"

echo ""
echo "Setup complete! To use the environment:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Start Jupyter: jupyter notebook"
echo "3. In Jupyter, select 'Multi-Agent Researcher (venv)' as the kernel"
echo ""
echo "If you still get pkg_resources errors, run: pip install --upgrade setuptools"