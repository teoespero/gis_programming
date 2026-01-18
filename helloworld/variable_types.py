# **********************************************************************************************
# * Name:   variable_types.py
# * Author: Teo Espero
# *         MAS-GIT
# * Date written:   01/17/2026
# * Description:    This short Python script is used to demonstrate the ways data and variables
# *                 are handled in the Python environment.
# **********************************************************************************************


# -------------------------------------------------------
# - Declare our data types
# -------------------------------------------------------
num_points = 120                # integer
latitude = 35.6895              # float
longitude = 139.6917            # float
coordinate_system = "WGS 84"    # string
is_georeferenced = True         # boolean
coordinates = [                 # list
    35.6895,
    139.6917,
]
feature_attributes = {          # dictionaries
    "name": "Mount Fuji",
    "height_meters": 3776,
    "type": "Stratovolcano",
    "location": [35.3606, 138.7274],
}




print("Below are some of the data types that we will be using in the course.")
print("---------------------------------------------------------------------\n")
# -------------------------------------------------------
# - Print the data and the data type used
# -------------------------------------------------------
print(num_points, type(num_points))
print("lat", latitude, type(latitude))
print("long", longitude, type(longitude))
print(coordinate_system, type(coordinate_system))
print(is_georeferenced, type(is_georeferenced))
print(coordinates, type(coordinates))
print(feature_attributes, type(feature_attributes))


# -------------------------------------------------------
# - EOF
# -------------------------------------------------------