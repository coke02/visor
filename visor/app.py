from flask import Flask, render_template
import requests,time
import json
import requests,time
from datetime import datetime
from flask import Flask, Response, render_template
from flask import jsonify
from werkzeug.wrappers import response

application = Flask(__name__)

url = ('https://climatologia.meteochile.gob.cl/application/productos/emaResumenDiario/330020')

@application.route('/')
def home():
    
    while True:
        response = requests.get(url)
        weatherdata = response.json()
        estacion = weatherdata['datosEstacion']['nombreEstacion']
        momento = weatherdata['datos']['valoresMasRecientes']['momento']
        high = weatherdata['datos']['valoresMasRecientes']['temperatura']
        viento_f = weatherdata['datos']['valoresMasRecientes']['fuerzaDelViento']
        viento_d = weatherdata['datos']['valoresMasRecientes']['direccionDelViento']
        agua_c = weatherdata['datos']['valoresMasRecientes']['aguaCaidaDelMinuto']
        #print("temperatura: ", high)
        #time.sleep(300)
            
        return render_template('home.html',est = estacion, momen = momento, tem = high, viento = viento_f, agua = agua_c, dviento = viento_d)

@application.route('/chart-data')
def chart_data():
    
    def temperatura_actual():
        
        while True:
            response = requests.get(url)
            weatherdata = response.json()
            high = weatherdata['datos']['valoresMasRecientes']['temperatura'] 
            weatherdata = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': high})
            yield f"data:{weatherdata}\n\n"
            #print(high)
            time.sleep(300)
            
    return Response(temperatura_actual(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(host= '0.0.0.0', port= 8080, debug=True)
    
""""
<----Actualizar info--->
url = ('https://climatologia.meteochile.gob.cl/application/productos/emaResumenDiario/330020')

@application.route('/', methods=['post'])
def home():
    
    response = requests.get(url)
    weatherdata = response.json()
    high = weatherdata['datos']['valoresMasRecientes']['temperatura']
    if weatherdata:
        if 'temperatura' in high:
            temp = high['temperatura']
            print("temperatura: ", temp)
        time.sleep(300)
            
    return render_template('home.html')


if __name__ == '__main__':
    application.run(host= '0.0.0.0', port= 8080, debug=True)
    
    
"""