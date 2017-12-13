def getSig(data, ws, mu):
    zaehler = 0
    nenner = 0
    for x, w in zip(data, ws):
        zaehler += float(w * (x - mu)**2)
        nenner += float(w)
    return float(np.sqrt(zaehler/nenner))