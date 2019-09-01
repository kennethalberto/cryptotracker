from django.shortcuts import render, redirect
from requests import Request, Session
from django.views.generic import (
    CreateView
)
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def CryptoView(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'50',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '9e14c935-7d36-4321-864c-668315cf3056',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)
        # print(data["data"]["1"])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return render(request, 'crypto/index.html', context = data)