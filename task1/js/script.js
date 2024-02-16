// Fetch the polygon coordinates from polygon.json
fetch('polygon.json')
  .then(response => response.json())
  .then(data => {
    // Initialize map
    const map = new ol.Map({
      target: 'map',
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM(),
        }),
      ],
      view: new ol.View({
        center: ol.proj.fromLonLat([data.polygon[0][0], data.polygon[0][1]]),
        zoom: 10,
      }),
    });

    // Create polygon geometry
    const coordinates = data.polygon.map(coord => ol.proj.fromLonLat(coord));
    const polygon = new ol.geom.Polygon([coordinates]);

    // Create polygon feature
    const feature = new ol.Feature({
      geometry: polygon,
    });

    // Create style for polygon
    const style = new ol.style.Style({
      fill: new ol.style.Fill({
        color: 'rgba(255, 0, 0, 0.2)', // Red with 20% opacity
      }),
      stroke: new ol.style.Stroke({
        color: 'red',
        width: 2,
      }),
    });

    // Apply style to polygon feature
    feature.setStyle(style);

    // Create vector layer with polygon feature
    const vectorLayer = new ol.layer.Vector({
      source: new ol.source.Vector({
        features: [feature],
      }),
    });

    // Add vector layer to map
    map.addLayer(vectorLayer);
  });
