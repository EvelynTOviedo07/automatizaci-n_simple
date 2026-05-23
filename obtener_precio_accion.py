import yfinance as yf
from utils import sanitizar

# Diccionario para mapear nombres comunes de empresas a sus Tickers de bolsa correspondientes
COMPANY_TICKERS = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "tesla": "TSLA",
    "meta": "META",
    "facebook": "META",
    "netflix": "NFLX",
    "nvidia": "NVDA",
    "apple inc": "AAPL",
    "microsoft corp": "MSFT",
    "tesla motors": "TSLA"
}

def obtener_precio_accion(driver, user_input):
    # 1. Convertimos el input a minúsculas para buscar en el diccionario
    input_minuscula = user_input.lower()
    
    ticker_encontrado = None
    
    # 2. Buscamos si alguna de las palabras clave está en el input del usuario
    for empresa, ticker in COMPANY_TICKERS.items():
        if empresa in input_minuscula:
            ticker_encontrado = ticker
            break
            
    # 3. Si no encontramos la empresa en el diccionario, avisamos al usuario
    if not ticker_encontrado:
        return "No logré identificar de qué empresa quieres el precio. Intenta con 'precio de Apple' o 'valor de Tesla'."
    
    try:
        # 4. Usamos yfinance para obtener el precio real en tiempo real
        accion = yf.Ticker(ticker_encontrado)
        # Obtenemos la información más reciente
        historial = accion.history(period="1d")
        
        if not historial.empty:
            # Tomamos el último precio de cierre disponible
            precio_actual = historial['Close'].iloc[-1]
            return f"El precio actual de {ticker_encontrado} es ${precio_actual:.2f} USD."
        else:
            return f"No se pudieron obtener datos en este momento para {ticker_encontrado}."
            
    except Exception as e:
        return f"Hubo un error al consultar el precio de {ticker_encontrado}: {str(e)}"
