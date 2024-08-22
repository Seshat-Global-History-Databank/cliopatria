import folium
import ipywidgets as widgets
from IPython.display import display, clear_output
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def create_carto_map(selected_year, gdf, map_output, components=False, projection=ccrs.Robinson()):
    """
    Create a map of the world with the shapes from the GeoDataFrame gdf that
    overlap with the selected_year. If components is True, only shapes that
    are components are displayed. If components is False, only shapes that are
    not components (full polities) are displayed. Uses Cartopy for the map.

    Args:
        selected_year (int): The year to display shapes for.
        gdf (GeoDataFrame): The GeoDataFrame containing the shapes.
        map_output (Output): The Output widget to display the map in.
        components (bool): Whether to display components or not.

    Returns:
        None
    """
    # Filter the gdf for shapes that overlap with the selected_year
    filtered_gdf = gdf[(gdf['FromYear'] <= selected_year) & (gdf['ToYear'] >= selected_year)]

    # This logic is duplicated in shouldDisplayComponent() in map_functions.js
    if components:
        # Only shapes where the "Components" column is not populated (i.e., the shape doesn't have components, it is a lowest-level component itself)
        filtered_gdf = filtered_gdf[(filtered_gdf['Components'].isnull()) | (filtered_gdf['Components'] == '')]
    else:
        # Only shapes where the "MemberOf" column is not populated (i.e., the shape is not a member of another shape, it is a top-level shape itself)
        filtered_gdf = filtered_gdf[(filtered_gdf['MemberOf'].isnull()) | (filtered_gdf['MemberOf'] == '')]

    # Transform the CRS of the GeoDataFrame to WGS84 (EPSG:4326)
    filtered_gdf = filtered_gdf.to_crs(epsg=4326)

    # Set up the plot with a Robinson projection using cartopy
    fig, ax = plt.subplots(1, 1, figsize=(15, 10), subplot_kw={'projection': projection})
    ax.set_global()
    ax.coastlines()

    # Plot the filtered geometries
    filtered_gdf.plot(ax=ax, transform=ccrs.PlateCarree(), edgecolor='black', facecolor='none')

    # Add the polygons with colors
    for _, row in filtered_gdf.iterrows():
        ax.add_geometries([row.geometry], crs=ccrs.PlateCarree(), facecolor=row['Color'], edgecolor=row['Color'], alpha=0.5)

    # Display the map
    with map_output:
        clear_output(wait=True)
        display(fig)


def create_folium_map(selected_year, gdf, map_output, components=False):
    """
    Create a map of the world with the shapes from the GeoDataFrame gdf that
    overlap with the selected_year. If components is True, only shapes that
    are components are displayed. If components is False, only shapes that are
    not components (full polities) are displayed. Uses Folium for the map.

    Args:
        selected_year (int): The year to display shapes for.
        gdf (GeoDataFrame): The GeoDataFrame containing the shapes.
        map_output (Output): The Output widget to display the map in.
        components (bool): Whether to display components or not.

    Returns:
        None
    """
    global m
    m = folium.Map(location=[0, 0], zoom_start=2, tiles='https://a.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png', attr='CartoDB')

    # Filter the gdf for shapes that overlap with the selected_year
    filtered_gdf = gdf[(gdf['FromYear'] <= selected_year) & (gdf['ToYear'] >= selected_year)]

    # This logic is duplicated in shouldDisplayComponent() in map_functions.js
    if components:
        # Only shapes where the "Components" column is not populated (i.e., the shape doesn't have components, it is a lowest-level component itself)
        filtered_gdf = filtered_gdf[(filtered_gdf['Components'].isnull()) | (filtered_gdf['Components'] == '')]
    else:
        # Only shapes where the "MemberOf" column is not populated (i.e., the shape is not a member of another shape, it is a top-level shape itself)
        filtered_gdf = filtered_gdf[(filtered_gdf['MemberOf'].isnull()) | (filtered_gdf['MemberOf'] == '')]

    # Transform the CRS of the GeoDataFrame to WGS84 (EPSG:4326)
    filtered_gdf = filtered_gdf.to_crs(epsg=4326)

    # Define a function for the style_function parameter
    def style_function(feature, color):
        return {
            'fillColor': color,
            'color': color,
            'weight': 2,
            'fillOpacity': 0.5
        }

    # Add the polygons to the map
    for _, row in filtered_gdf.iterrows():

        # Convert the geometry to GeoJSON
        geojson = folium.GeoJson(
            row.geometry,
            style_function=lambda feature, color=row['Color']: style_function(feature, color)
        )

        # Add a popup to the GeoJSON
        folium.Popup(row['DisplayName']).add_to(geojson)

        # Add the GeoJSON to the map
        geojson.add_to(m)

    # Display the map
    with map_output:
        clear_output(wait=True)
        display(m)


def display_map(gdf, display_year, map_function='folium', projection=ccrs.Robinson()):
    """
    Display a map of the world with the shapes from the GeoDataFrame gdf that
    overlap with the display_year. The user can change the year using a text box
    or a slider, and can switch between displaying polities and components using
    a radio button.

    Args:
        gdf (GeoDataFrame): The GeoDataFrame containing the shapes.
        display_year (int): The year to display shapes for.

    Returns:
        None
    """
    if map_function == 'folium':
        create_map = create_folium_map
    elif map_function == 'cartopy':
        def create_map(selected_year, gdf, map_output, components=False):
            return create_carto_map(selected_year, gdf, map_output, components, projection=projection)
    # Create a text box for input
    year_input = widgets.IntText(
        value=display_year,
        description='Year:',
    )

    # Create a slider for input
    year_slider = widgets.IntSlider(
        value=display_year,
        min=gdf['FromYear'].min(),
        max=gdf['ToYear'].max(),
        description='Year:',
    )

    # Link the text box and the slider
    widgets.jslink((year_input, 'value'), (year_slider, 'value'))

    # Create a radio button to switch between "Polities" and "Components".
    # The value should be a boolean indicating whether to display components or not.
    components_radio = widgets.RadioButtons(
        options=['Polities', 'Components'],
        description='Display:',
        disabled=False
    )

    # Define a function to be called when the value of the text box changes
    def on_value_change(change):
        """
        This function is called when the value of the text box or slider changes.
        It calls create_map with the newly selected year and the GeoDataFrame gdf.
        It sets the components parameter based on the current value of the radio button.

        Args:
            change (dict): A dictionary containing information about the change.

        Returns:
            None
        """
        if components_radio.value == 'Polities':
            create_map(change['new'], gdf, map_output)
        elif components_radio.value == 'Components':
            create_map(change['new'], gdf, map_output, components=True)

    # Define a function to be called when the value of the radio button changes
    def on_radio_change(change):
        """
        This function is called when the value of the radio button changes. It calls
        create_map with the newly selected year of the text box and the GeoDataFrame gdf.
        It sets the components parameter based on the current value of the radio button.

        Args:
            change (dict): A dictionary containing information about the change.

        Returns:
            None
        """
        if change['new'] == 'Polities':
            create_map(year_input.value, gdf, map_output)
        elif change['new'] == 'Components':
            create_map(year_input.value, gdf, map_output, components=True)

    # Attach the function to the text box
    year_input.observe(on_value_change, names='value')

    # Attach the function to the radio button
    components_radio.observe(on_radio_change, names='value')

    # Create an output widget
    map_output = widgets.Output()

    # Display the widgets
    display(year_input, year_slider, components_radio, map_output)

    # Call create_map initially to display the map
    create_map(display_year, gdf, map_output, )