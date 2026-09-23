#!/usr/bin/env python3
"""
Arma el PDF de un informe de Maison.

    python3 informes/construir.py informes/2026-09-23-donde-se-cae-la-venta.html

Deja el PDF en reportes/ con el mismo nombre. Se le puede pasar un segundo
argumento para elegir otra salida.

Lo que hace, en orden:
  1. Junta figtree.css (las fuentes ya empotradas en base64), estilo.css y
     impresion.css con el cuerpo del informe.
  2. Saca los bloques de tema oscuro: el PDF es siempre blanco.
  3. Llama a Chrome sin ventana para imprimirlo.

Por qué las fuentes van empotradas: Chrome no confía en la CA del proxy de
este entorno, así que un <link> a Google Fonts falla en silencio y el PDF
sale con la tipografía del sistema. Con base64 no hay red de por medio.
"""

import os
import re
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)

CHROMES = [
    '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    '/usr/bin/chromium',
    '/usr/bin/google-chrome',
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
]


def buscar_chrome():
    for ruta in CHROMES:
        if os.path.exists(ruta):
            return ruta
    raise SystemExit(
        'No encontré Chrome. Agregá su ruta a la lista CHROMES de este archivo.'
    )


def leer(nombre):
    with open(os.path.join(AQUI, nombre), encoding='utf-8') as f:
        return f.read()


def armar(ruta_cuerpo):
    cuerpo = open(ruta_cuerpo, encoding='utf-8').read()

    titulo = 'Maison Meszarics'
    marca = re.search(r'<!--\s*titulo:\s*(.+?)\s*-->', cuerpo)
    if marca:
        titulo = 'Maison Meszarics — ' + marca.group(1)
        cuerpo = cuerpo.replace(marca.group(0), '', 1)

    estilo = leer('estilo.css')
    # El PDF es siempre blanco: fuera los dos bloques de tema oscuro.
    estilo = re.sub(r'@media \(prefers-color-scheme: dark\) \{.*?\n  \}\n', '', estilo, flags=re.S)
    estilo = re.sub(r':root\[data-theme="dark"\] \{.*?\n  \}\n', '', estilo, flags=re.S)

    return """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>%s</title>
<style>
%s
</style>
<style>
%s
</style>
<style>
%s
</style>
</head>
<body>
%s
</body>
</html>
""" % (titulo, leer('figtree.css'), estilo, leer('impresion.css'), cuerpo.strip())


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)

    ruta_cuerpo = sys.argv[1]
    if len(sys.argv) > 2:
        salida = sys.argv[2]
    else:
        nombre = os.path.splitext(os.path.basename(ruta_cuerpo))[0] + '.pdf'
        salida = os.path.join(RAIZ, 'reportes', nombre)

    salida = os.path.abspath(salida)
    os.makedirs(os.path.dirname(salida), exist_ok=True)

    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as t:
        t.write(armar(ruta_cuerpo))
        temporal = t.name

    try:
        subprocess.run(
            [buscar_chrome(), '--headless', '--disable-gpu', '--no-sandbox',
             '--no-pdf-header-footer', '--print-to-pdf=' + salida,
             'file://' + temporal],
            check=True, capture_output=True,
        )
    finally:
        os.unlink(temporal)

    print(salida)

    try:
        import pypdfium2
        print(len(pypdfium2.PdfDocument(salida)), 'páginas')
    except ImportError:
        pass


if __name__ == '__main__':
    main()
