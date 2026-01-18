# **********************************************************************************************
# * Name:   city_latlong.py
# * Author: Teo Espero
# *         MAS-GIT
# * Date written:   01/17/2026
# * Description:    This short Python script is used to demonstrate the ways we use dictionaries
# *                 how their data is handled, and accessed.
# **********************************************************************************************


# -------------------------------------------------------
# - Declare our data types
# -------------------------------------------------------
cities = {
    "Sacramento, CA": {"coordinates": (-121.4944, 38.5816)},
    "Washington, DC": {"coordinates": (-77.0369, 38.9072)},
    "Las Vegas, NV": {"coordinates": (-115.1398, 36.1699)},
    "Napa Valley, CA": {"coordinates": (-122.2654, 38.5025)},
    "Marina, CA": {"coordinates": (-121.8022, 36.6844)},
    "Monterey, CA": {"coordinates": (-121.8947, 36.6002)},
    "Carmel-by-the-Sea, CA": {"coordinates": (-121.9233, 36.5552)}
}
ctr = 0

# -------------------------------------------------------
# - Print the cities and their lat long coordinates
# -------------------------------------------------------
print("Below are some of the cities I've visited")
print("-------------------------------------------------")
for city, data in cities.items():
    ctr = ctr + 1
    print(f"{ctr}: {city}: {data['coordinates']}")
print("-------------------------------------------------")

# -------------------------------------------------------
# - EOF
# -------------------------------------------------------
