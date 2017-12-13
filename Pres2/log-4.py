def getMu(data, ws):
    zaehler = 0
    nenner = 0
    for x, w in zip(data, ws):
        zaehler += float(x*w)
        nenner += float(w)
    return zaehler/nenner