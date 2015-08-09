from flask import Flask, render_template, url_for, request, redirect
import xml.etree.ElementTree as ET
import os

app = Flask(__name__)


def getcoords(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    trk = root.find("[{http://www.topografix.com/GPX/1/1}trk]")
    trkpt = trk.find('.//{http://www.topografix.com/GPX/1/1}trkpt')
    x = trkpt.attrib
    lat, lon = x['lat'], x['lon']
    coords = [float(lon), float(lat)]
    return coords


@app.route('/', methods=['GET', 'POST'])
def index():
    maps = {'type': 'default'}
    if request.method == 'POST':
        f = request.files['file']
        myfilename = f.filename
        myfileurl = url_for('static', filename=myfilename)
        centercoords = getcoords(os.path.join('static', myfilename))
        if request.form['maptype'] == 'OSM':
            maps['type'] = 'OSM'
        elif request.form['maptype'] == 'bing':
            maps['type'] = 'bing'
        return render_template('index.html', myfileurl=myfileurl,
                               centercoords=centercoords, maps=maps)
    return render_template('index.html', maps=maps)

if __name__ == '__main__':
    app.run(debug=True)
