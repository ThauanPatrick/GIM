from django.shortcuts import render

def home(request):
    resultado = 'Content-type: text/html\n\n'
    resultado = resultado + '<html>\n'
    resultado = resultado + '<head><title>CGI - python</title></head>\n'
    resultado = resultado + '<body><h1>CGI - python</h1>Seu CGI esta funcionando</body>\n'
    resultado = resultado + '</html>'

    return render(request, resultado)
