# Visualise Cliopatria shape dataset

You can explore the Cliopatria dataset in an interactive Jupyter notebook. This folder contains a processing script to add colors to the dataset, alongside a notebook which loads the data in GeoPandas and includes an interactive Folium plot.

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

3. Open the `cliopatria.ipynb` notebook with Jupyter (or another application that can run notebooks such as VSCode).
    - `jupyter lab` (or `jupyter notebook`)
    - Note: make sure the notebook Python kernel is using the virtual environment you created (click top right)
4. Follow the instructions in the notebook.