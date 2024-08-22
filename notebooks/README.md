# Visualise Cliopatria shape dataset

Cliopatria is the shape dataset used by the Seshat Global History Databank website. It can also be explored in a local Jupyter notebook running on your local machine by following these instructions.

<!-- TODO: Add download link for Cliopatria -->

1. Ensure you have a working installation of Python 3 and Conda. If not, [download Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html), which should give you both
    - Note: you can use a different tool for creating a Python virtual environment than conda (e.g. venv) if you prefer

2. Set up the required virtual environment, install packages into it and create a jupyter kernel.
    - Conda example:
        ```
            conda create --name cliopatria python=3.11
            conda activate cliopatria
            pip install -r requirements.txt
            python -m ipykernel install --user --name=cliopatria --display-name="Python (cliopatria)"
        ```
    - Note: This will install Geopandas 0.13.2, but if you [install from source](https://geopandas.org/en/stable/getting_started/install.html#installing-from-source) it's much faster with version 1.0.0 (unreleased on pip as of 18th June 2024)

3. Open the `cliopatria.ipynb` notebook with Jupyter (or another application that can run notebooks such as VSCode).
    - `jupyter lab` (or `jupyter notebook`)
    - Note: make sure the notebook Python kernel is using the virtual environment you created (click top right)
4. Follow the instructions in the notebook.