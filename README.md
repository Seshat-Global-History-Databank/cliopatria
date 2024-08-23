# Cliopatria

Cliopatria is a comprehensive open-source geospatial dataset of worldwide states, political groups, events, and rulers from 3400BCE to 2024CE.  It is part of the [Seshat Global History Databank](https://seshatdatabank.info/) project.  Presently it comprises over 1800 political entities sampled at varying timesteps and spatial scales. Description of its initial format, construction, and source material may be found [here: socarxiv, then Nature].  Released versions may be accessed here or [on Zenodo](https://zenodo.org/records/13363121).

*The [Seshat Global History Databank](https://seshat-db.com/) will soon feature Cliopatria. For now, you can see how it will be used on our test site:*

* *[Seshat World Map](https://seshatdata.com/core/world_map)*
* *[Seshat Polity Pages](https://seshatdata.com/core/polity/71) (Roman Empire - Dominate)*

While we strive to reflect the most current historical knowledge, we acknowledge that these maps reflect only one version of the territory held by past polities. Border uncertainties, as well as differing opinions on the names, territorial changes, and durations of polities, are common challenges facing historians. We welcome feedback and suggestions for improvement. Following [standard Seshat protocol](https://seshatdatabank.info/methods/world-sample-30), any reported errors will be addressed after expert historian review.

Please note that users and analysts of this map data are solely responsible for assessing its suitability for their specific purposes.

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

2. Unzip `cliopatria.geojson.zip` to get `cliopatria.geojson` and make the relevant modifications for the new release. If wish to check the new version, you can inspect it in the Jupyter interactive plot (see [here](./notebooks)).

3. Rezip the file and save it over `cliopatria.geojson.zip`. 

4. Decide on a new version number based on the numbering system decided above.

5. Commit the zip file with an informative commit message and create a tag with the version number:

    ```
        git add cliopatria.geojson.zip
        git commit -m 'Update to vX.X.X'
        git tag vX.X.X
    ``` 

6. Push your updated zip file and the tag to GitHub:

    ```
        git push
        git push origin vX.X.X
    ```

7. On GitHub, click "Releases" (on the right of this page). Choose the tag you created and name the release the same i.e. `vX.X.X`. Enter any relevant info describing the changes in the release. The linked [Zenodo](https://zenodo.org/records/13363121) will automatically get updated with the latest release.

