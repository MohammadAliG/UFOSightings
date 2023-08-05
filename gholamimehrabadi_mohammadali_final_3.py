fIn = open("Documents/Python/latlon/gholamimehrabadi_mohammadali_latlon.txt", "r")
fOutHTML = open("Documents/Python/latlon/gholamimehrabadi_mohammadali.html", "w")
fOutJS = open("Documents/Python/latlon/gholamimehrabadi_mohammadali.js", "w")

#I added this break string for my own testing purposes because anything after 14900~ had this due to my key expiring
breakString = "please consider upgrading to a plan that offers additional transactions. If you would like to talk to an Account Manager about Enterprise Edition licensing options,  please contact sales@mapquest.com."

htmlStr = """<html>
  <head>
    <script src="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.js"></script>
    <link type="text/css" rel="stylesheet" href="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.css"/>
    <script src="https://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"></script>
    <script src="gholamimehrabadi_mohammadali.js"></script>

    <script type="text/javascript">
      window.onload = function() {
        L.mapquest.key = 'lYrP4vF3Uk5zgTiGGuEzQGwGIVDGuy24';
        var baseLayer = L.mapquest.tileLayer('map');

        var map = L.mapquest.map('map', {
          center: [39.8283, -98.5795],
          layers: baseLayer,
          zoom: 4
        });
        L.heatLayer(addressPoints, {radius: 30}).addTo(map);
      }
    </script>
  </head>

  <body style="border: 0; margin: 0;">
    <div id="map" style="width: 100%; height: 530px;"></div>
  </body>
</html>
"""

fOutHTML.write(htmlStr)
fOutJS.write("var addressPoints = [")

while True:
	line = fIn.readline()
	#I wrote a comment further up for why I have this
	if breakString in line:
		break
	if(len(line) == 0):
		break
	line = line.replace(",", "\t")
	line = line.replace("\n", "")
	l = line.split("\t")
	fOutJS.write("[" + l[0] + ", " + l[1] + ", " + '"' + l[2] + '"' + "], ")

fOutJS.write("];")

fOutHTML.close()
fOutJS.close()
fIn.close()