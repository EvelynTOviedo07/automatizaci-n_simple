import urllib.request
import json

def obtener_clima(driver, consulta):
    # 1. Limpiamos la consulta para extraer el nombre de la ciudad
    # Por si el usuario escribe "clima en Madrid", nos quedamos solo con "Madrid"
    ciudad = consulta.replace("clima en", "").replace("clima", "").replace("temperatura en", "").replace("temperatura", "").strip()
    
    if not ciudad:
        return "Por favor, dime de qué ciudad quieres saber el clima (ej: 'clima Madrid')."
        
    try:
        # 2. Primero usamos el geocodificador gratuito de Open-Meteo para convertir el nombre de la ciudad en Latitud y Longitud
        url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(ciudad)}&count=1&language=es"
        
        req = urllib.request.Request(url_geo, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            datos_geo = json.loads(response.read().decode())
            
        if not datos_geo.get("results"):
            return f"No logré encontrar la ubicación geográfica de '{ciudad}'. Intenta con otra ciudad."
            
        # Extraemos coordenadas y el nombre real encontrado
        resultado = datos_geo["results"][0]
        lat = resultado["latitude"]
        lon = resultado["longitude"]
        nombre_ciudad = resultado["name"]
        pais = resultado.get("country", "")

        # 3. Consultamos el clima real usando las coordenadas obtenidas
        url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        
        with urllib.request.urlopen(url_clima) as response:
            datos_clima = json.loads(response.read().decode())
            
        clima_actual = datos_clima["current_weather"]
        temperatura = clima_actual["temperature"]
        
        # Opcional: Mapear códigos de clima básicos
        codigo_clima = clima_actual["weathercode"]
        estados = {0: "Despejado", 1: "Principalmente despejado", 2: "Parcialmente nublado", 3: "Nublado", 45: "Niebla", 51: "Llovizna", 61: "Lluvia ligera", 71: "Nieve"}
        estado_texto = estados.get(codigo_clima, "Variable")

        # 4. Devolvemos la respuesta formateada limpia
        return f"El clima actual en {nombre_ciudad} ({pais}) es de {temperatura}°C y el cielo está '{estado_texto}'."

    except Exception as e:
        return f"Hubo un problema al conectar con el servicio meteorológico: {str(e)}"