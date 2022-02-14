from flask import Flask, render_template, Response, json
import requests, time
from datetime import datetime


app = Flask(__name__)

url = ('https://climatologia.meteochile.gob.cl/application/productos/emaResumenDiario/330020')

@app.route("/")
def vista():
    return render_template ("vista.html")


@app.route('/data')
def data():
    
    def temperatura_actual():
        
        while True:
            response = requests.get(url)
            weatherdata = response.json()
            high = weatherdata['datos']['valoresMasRecientes']['temperatura'] 
            weatherdata = json.dumps(high)
            yield f"data:{weatherdata}\n\n"
            #print(high)
            time.sleep(300)
            
    return Response(temperatura_actual(), mimetype='text/event-stream')

@app.route('/chart-data')
def chart_data():
    
    def temp_actual():
        
        while True:
            response = requests.get(url)
            tempdata = response.json()
            temp = tempdata['datos']['valoresMasRecientes']['temperatura'] 
            tempdata = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': temp})
            yield f"data:{tempdata}\n\n"
            #print(high)
            time.sleep(300)
            
    return Response(temp_actual(), mimetype='text/event-stream')

@app.route('/viento')
def viento():
    
    def viento_actual():
        
        while True:
            response = requests.get(url)
            viento = response.json()
            viento_f = viento['datos']['valoresMasRecientes']['fuerzaDelViento']
            viento = json.dumps( viento_f)
            yield f"data:{viento}\n\n"
            #print(high)
            time.sleep(300)
            
    return Response(viento_actual(), mimetype='text/event-stream')

@app.route('/agua')
def agua():
    
    def agua_actual():
        
        while True:
            response = requests.get(url)
            agua = response.json()
            agua_c = agua['datos']['valoresMasRecientes']['aguaCaidaDelMinuto']
            agua = json.dumps(agua_c)
            yield f"data:{agua}\n\n"
            #print(high)
            time.sleep(300)
            
    return Response(agua_actual(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 8080, debug=True)