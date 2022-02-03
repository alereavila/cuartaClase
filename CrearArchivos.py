"""
Convertidor de texto simple a HTML
autor :yo
OS : Win Lin.
"""


def convertir():
    print('Convertidor de txt a HTML')
    aOrigen = input('Ingrese el nombre de archivo : ')
    # poema.txt  -> poema.html
    aDestino = aOrigen.replace('.txt', '.html')
    # print(aOrigen, aDestino)

    encabezado = """<html>
    <head>
    <title>{titulo}</title>
    </head>

    <body>
    <h1>{titulo}</h1>

    """

    pie = """
    </body>
    </html>
    """

    with open(aOrigen, 'r', encoding='utf8') as fuente:
        tituloOrigen = fuente.readline()
        texto = fuente.read()

    encabezado = encabezado.format(titulo=tituloOrigen)

    textohtml = '<p> <br/>' + texto.replace('.\n\n', '.\n <br/> </p>\n<p>\n')
    textohtml = textohtml.replace('.\n', '.\n<br/>\n')
    textohtml = textohtml.replace(',\n', ',\n<br/>\n')

    htmlcompleto = ''.join([encabezado, textohtml, pie])
    htmlcompleto = htmlcompleto.replace('Á', '&Aacute;')
    htmlcompleto = htmlcompleto.replace('É', '&Eacute;')
    htmlcompleto = htmlcompleto.replace('Í', '&Iacute;')
    htmlcompleto = htmlcompleto.replace('Ó', '&Oacute;')
    htmlcompleto = htmlcompleto.replace('Ú', '&Uacute;')
    htmlcompleto = htmlcompleto.replace('á', '&aacute;')
    htmlcompleto = htmlcompleto.replace('é', '&eacute;')
    htmlcompleto = htmlcompleto.replace('í', '&iacute;')
    htmlcompleto = htmlcompleto.replace('ó', '&oacute;')
    htmlcompleto = htmlcompleto.replace('ú', '&uacute;')

    htmlcompleto = htmlcompleto.replace('ñ', '&ntilde;')
    htmlcompleto = htmlcompleto.replace('Ñ', '&Ntilde;')

    htmlcompleto = htmlcompleto.replace('¡', '&iexcl;')
    htmlcompleto = htmlcompleto.replace('¿', '&iquest;')

    with open(aDestino, 'w', encoding='utf8') as destino:
        destino.write(htmlcompleto)


if __name__ == '__main__':
    convertir()