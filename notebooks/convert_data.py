import geopandas as gpd
from distinctipy import get_colors, get_hex
import sys

def cliopatria_gdf(gdf):
    """
    Load the Cliopatria polity borders dataset from a GeoDataFrame created by GeoPandas (from a GeoJSON file).
    Process the Cliopatria dataset for loading to the Seshat database and visualisation in the Seshat website.

    Args:
        gdf (GeoDataFrame): A GeoDataFrame containing the Cliopatria polity borders dataset.

    Returns:
        GeoDataFrame: The input GeoDataFrame with additional columns 'DisplayName', 'Color', 'PolityStartYear', and 'PolityEndYear'.
    """

    # Generate DisplayName for each shape based on the 'Name' field
    gdf['DisplayName'] = gdf['Name'].str.replace('[()]', '', regex=True)

    # Add type prefix to DisplayName where type is not 'POLITY'
    gdf.loc[gdf['Type'] != 'POLITY', 'DisplayName'] = gdf['Type'].str.capitalize() + ': ' + gdf['DisplayName']

    print(f"Generated shape names for {len(gdf)} shapes.")
    print("Assigning colours to shapes...")

    # Use DistinctiPy package to assign a colour based on the DisplayName field
    colour_keys = gdf['DisplayName'].unique()
    colours = [get_hex(col) for col in get_colors(len(colour_keys))]
    colour_mapping = dict(zip(colour_keys, colours))

    # Map colors to a new column
    gdf['Color'] = gdf['DisplayName'].map(colour_mapping)

    print(f"Assigned colours to {len(gdf)} shapes.")
    print("Determining polity start and end years...")

    # Add a column called 'PolityStartYear' to the GeoDataFrame which is the minimum 'FromYear' of all shapes with the same 'Name'
    gdf['PolityStartYear'] = gdf.groupby('Name')['FromYear'].transform('min')

    # Add a column called 'PolityEndYear' to the GeoDataFrame which is the maximum 'ToYear' of all shapes with the same 'Name'
    gdf['PolityEndYear'] = gdf.groupby('Name')['ToYear'].transform('max')

    print(f"Determined polity start and end years for {len(gdf)} shapes.")

    return gdf


# Check if a GeoJSON file path was provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide the path to the GeoJSON file as a command line argument.")
    sys.exit(1)

geojson_path = sys.argv[1]

try:
    gdf = gpd.read_file(geojson_path)
except Exception as e:
    print(f"Error loading GeoJSON file: {str(e)}")
    sys.exit(1)

# Call the cliopatria_gdf function to process the GeoDataFrame
processed_gdf = cliopatria_gdf(gdf)

# Save the processed GeoDataFrame as a new GeoJSON file
output_path = geojson_path.replace('.geojson', '_seshat_processed.geojson')
try:
    processed_gdf.to_file(output_path, driver='GeoJSON')
    print(f"Processed GeoDataFrame saved to: {output_path}")
except Exception as e:
    print(f"Error saving processed GeoDataFrame: {str(e)}")
    sys.exit(1)