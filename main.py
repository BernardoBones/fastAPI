from fastapi import FastAPI
from pyswip import Prolog
import uvicorn

app = FastAPI()
prolog = Prolog()

prolog.consult('base.pl')

@app.get('/gosta/{nome}', description='Buscar a(s) marca(s) que a pessoa gosta')
def gosta_marca(nome: str):
    try:
        resultados = prolog.query(f'gosta({nome}, Marca)') 

        return resultados
    except Exception as e:
        print(e)
        return {"error": str(e)}

@app.get('/gosta_cor/{nome}', description='Buscar a(s) cor(es) de carro(s) que a pessoa gosta')
def gosta_cor(nome: str):
    try:
        resultados = prolog.query(f'gosta_cor({nome}, Cor)') 
        return resultados
    except Exception as e:
        print(e)
        return {"error": str(e)}

@app.get('/gosta_carro_cor/', description='Para múltiplas pesquisas, obrigatório pelo menos um parâmetro')
def gosta_carro_cor(nome: str = None, marca: str = None, cor: str = None):
    try:
        if nome is None and marca is None and cor is None:
            return {'Pelo menos um parâmetro deve ser informado!'}
        
        if nome is None:
            nome = 'X'
        if marca is None:
            marca = 'Y'
        if cor is None:
            cor = 'Z'
        
        else:
            resultados = prolog.query(f'gosta_carro_cor({nome}, {marca}, {cor})')
            return resultados
    except Exception as e:
        print(e)
        return {"error": str(e)}

@app.get('/marca_do_modelo/{modelo}', description='')
def marca_do_modelo(modelo: str):
    try:
        resultado = prolog.query(f'marca(Marca, {modelo}, Cor)')
        return resultado
    except Exception as e:
        print(e)
        return {"error": str(e)}

@app.get('/modelos_marca/{marca}')
def modelos_marca(marca: str):
    try:
        resultado = prolog.query(f'marca({marca}, Modelo, Cor)')
        return resultado
    except Exception as e:
        print(e)
        return {"error": str(e)}

@app.get('/modelos_da_cor/{cor}', description='teste')
def modelos_da_cor(cor: str):
    try:
        resultado = prolog.query(f'marca(Marca, Modelo, {cor})')
        return resultado
    except Exception as e:
        print(e)
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)