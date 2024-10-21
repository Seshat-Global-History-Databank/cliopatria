# Visualise Cliopatria shape dataset

You can explore the Cliopatria dataset in an interactive Jupyter notebook. This folder contains a processing script to add colors to the dataset, alongside a notebook which loads the data in GeoPandas and includes an interactive Folium plot.

1. Ensure you have a working installation of Python 3 and Conda. If not, [download Anaconda](https://seshat-global-history-databank.github.io/seshat/software-tools.html#python-anaconda), which should give you both
    - Note: you can use a different tool for creating a Python virtual environment than conda (e.g. venv) if you prefer

2. Clone this GitHub repository
    ```
        git clone https://github.com/Seshat-Global-History-Databank/cliopatria
    ```

3. Navigate to the cloned repo and set up the required virtual environment, install packages into it and create a jupyter kernel.
    - Conda example:
        ```
            cd cliopatria/notebooks
            conda create --name cliopatria python=3.11
            conda activate cliopatria
            pip install -r requirements.txt
            python -m ipykernel install --user --name=cliopatria --display-name="Python (cliopatria)"
        ```

4. You can then open the notebook with Jupyter (or another application that can run notebooks such as VSCode). First open the Jupyter notebook application:
    ```
        jupyter notebook
    ```
    - Note: if Jupyter wants to to set a password, use `Ctrl-C` to escape and run `jupyter notebook --generate-config` before running `jupyter notebook` again and entering a blank password.

5. From the Jupyter notebook interface in your browser, open `notebooks/cliopatria.ipynb` and choose the Kernel that you created called `Python (cliopatria)` in the top right.

6. Follow the instructions in the notebook.
