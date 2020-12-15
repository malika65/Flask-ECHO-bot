def reformat_weather(r):
    params = {
        'main':r['weather'][0]['main'],
        'description':r['weather'][0]['description'],
        'humidity' : r['main']['humidity'],
        'feels_like' : r['main']['feels_like'],
        'temp' : r['main']['temp']
    }
    return params
