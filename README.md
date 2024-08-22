# Cliopatria

**TODO:** About Cliopatria...

**TODO:** Links to:
- Seshat world map, example polity pages
- Seshat website disclaimer on historical borders text
- Zenodo


## Exploring Cliopatria

You can explore the Cliopatria dataset in an interactive Jupyter notebook. The [notebooks](./notebooks) folder contains a processing script to add colors to the dataset, alongside a notebook which loads the data in GeoPandas and includes an interactive Folium plot.

## Releases

Whenever updates are made to `cliopatria.geojson`, a new release is made according to the following MAJOR.MINOR.PATCH versioning system:

1. MAJOR version when incompatible changes are made to the GeoJSON structure
2. MINOR version when large edits are made e.g. new polities have been added
3. PATCH version when smaller edits are made e.g. existing polgons and years have been adjusted

Past releases can be found on the right hand side of this page.

## Making a release

If you wish to edit Cliopatria and make a new release, do the following:

1. Ensure you have cloned the repo to your local machine:

    ```
        git clone https://github.com/Seshat-Global-History-Databank/cliopatria
    ```

2. Save over `cliopatria.geojson` with your new version of the file. If wish to check the new version, you can inspect it in the Jupyter interactive plot (see [here](./notebooks)).

3. Decide on a new version number based on the numbering system decided above.

4. Enter the repo, create a new branch named according to the version number (e.g. v1.0.0) and commit the geojson with an informative commit message:

    ```
        cd cliopatria
        git checkout -b vX.X.X
        git add cliopatria.geojson
        git commit -m 'Adjusts duration of Roman Empire polygons'
    ```
    Note: you could make multiple commits for separate edits if appropriate.

5. Once you have finished making commits, make a tag (which will point to the last commit):

    ```
       git tag -a vX.X.X
    ``` 

6. Push your new branch (and tag) to GitHub:

    ```
        git push --set-upstream origin vX.X.X --follow-tags
    ```
    Note: you only need to include `--set-upstream origin vX.X.X` the first time you push a branch.

7. Open a pull request on GitHub from the `vX.X.X` branch to `main`. You can request reviews from other maintainers if needed.

8. Once any reviewers are happy, merge the pull request. A release will be created on GitHub and should be visible on the right hand side. The linked Zenodo will also get updated with the latest release.

