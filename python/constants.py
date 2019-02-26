TRADED_PAIRS = {
    "USD/JPY":'usd_jpy',
    "EUR/USD":'eur_usd',
    "GBP/USD":'gbp_usd',
    "AUD/USD":'aud_usd',
    "USD/CAD":'usd_cad',
    "USD/CHF":'usd_chf',
    "NZD/USD":'nzd_usd'
}
#connect to DB local
DATABASES = {
    'local':{
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD':'password',
        'HOST':'localhost',
        'PORT':5432
    },
    'production':{
        'NAME': 'd7h0bl2kg6v3c2',
        'USER': 'nqfromejvqdewm',
        'PASSWORD':'d4268ae3afeffc9507eb9537d7ce4c53a82e4a0578a1f16b41ea4d489bad4686',
        'HOST':'ec2-54-83-196-179.compute-1.amazonaws.com',
        'PORT':5432
    }
}