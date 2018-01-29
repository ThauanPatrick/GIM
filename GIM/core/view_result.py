from django.shortcuts import render

def result(request):

    class resultado1:
        nome = 'l8_oli_002065_20140803_b654_fuseo_sirgas2000_utm.tiff'
        diretorio = '//172.23.5.17/Imagens/landsat/IMAGENS_LANDSAT_8_2014/'
        download = nome + diretorio

    resultado2 = resultado1
    resultado3 = resultado1

    resultados = [resultado1, resultado2, resultado3]

    context = {
        'resultados' : resultados
    }

    return render(request, 'result.html', context)
