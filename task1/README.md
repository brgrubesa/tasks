# Display Polygon on Map

This project displays a polygon on a map using OpenLayers library.

## Setup Instructions

1. **Clone the Repository**: 

   ```bash
   git clone <repository_url>
   ```

2. **Serve the Files**: 

   You need to serve the HTML, CSS, and JavaScript files in a web server. You can use any web server of your choice. For example:

   - Using Python's built-in HTTP server:
   
     ```bash
     python -m http.server
     ```

3. **Access the Page**:

   Once the server is running, open a web browser and navigate to `http://localhost:<port>`, where `<port>` is the port number specified by the web server.

## File Structure

- `index.html`: HTML file for displaying the map.
- `css/styles.css`: CSS file for styling the map.
- `js/script.js`: JavaScript file for fetching polygon coordinates and displaying them on the map.

## Dependencies

- [OpenLayers](https://openlayers.org/): JavaScript library used for displaying maps.
