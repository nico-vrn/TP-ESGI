import exifread
import webbrowser

def get_if_exist(data, key):
    return data[key] if key in data else None

def convert_to_degrees(value):
    """
    Convert the GPS coordinates stored in the EXIF to degrees in float format
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    
    return d + (m / 60.0) + (s / 3600.0)

def get_coordinates(tags):
    """
    Extract the GPS coordinates from the EXIF tags
    """
    lat = get_if_exist(tags, 'GPS GPSLatitude')
    lat_ref = get_if_exist(tags, 'GPS GPSLatitudeRef')
    lon = get_if_exist(tags, 'GPS GPSLongitude')
    lon_ref = get_if_exist(tags, 'GPS GPSLongitudeRef')

    if not lat or not lon or not lat_ref or not lon_ref:
        return None

    lat = convert_to_degrees(lat)
    if lat_ref.values[0] != 'N':
        lat = -lat

    lon = convert_to_degrees(lon)
    if lon_ref.values[0] != 'E':
        lon = -lon

    return lat, lon

def main(image_path):
    # Open image file for reading (binary mode)
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)

    # Print all metadata
    for tag in tags.keys():
        print(f"{tag}: {tags[tag]}")

    # Get GPS coordinates
    coordinates = get_coordinates(tags)
    if coordinates:
        print(f"Coordinates: {coordinates}")

        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={coordinates[0]},{coordinates[1]}"
        print(f"Google Maps URL: {google_maps_url}")
    else:
        print("No GPS data found.")

if __name__ == "__main__":
    image_path = "./mcafee.jpg"  
    main(image_path)
