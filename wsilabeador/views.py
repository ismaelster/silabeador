from wsilabeador import app
from pipapilapibra.pilengua import pilengua, inversa
from flask import jsonify


@app.route("/<frase>")
def index (frase):
    diccionario = {}
    diccionario["Response"] = True
    diccionario["result"] = {"original": frase, "traducido": pilengua(frase)}


    return jsonify(diccionario)

@app.route("/decodifica/<frase>")
def decodifica(frase):
    diccionario = {}
    diccionario ["Response"] = True
    diccionario ["result"] = {"original":frase, "traducido": inversaa(frase+" ")}
    
    return jsonify(diccionario)