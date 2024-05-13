#!/bin/bash

# Activate the Anaconda environment
source ~/anaconda3/bin/activate

# Create and activate a new environment named "stm32_sim"
conda create -n stm32_sim python=3.11
conda activate stm32_sim

# Install packages
conda install -c conda-forge dash-core-components=2.0.0
conda install -c conda-forge dash=2.4.0
conda install -c conda-forge dash-daq=0.5.0
conda install -c plotly plotly=5.19.0

# Verify installation
python -c "import plotly; print('Plotly version:', plotly.__version__)"
python -c "import dash; print('Dash version:', dash.__version__)"

# Install ipykernel and register the environment for Jupyter
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=stm32_sim

# Deactivate the environment
conda deactivate
