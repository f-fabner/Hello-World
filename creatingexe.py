import os
#creating player list inside vscode, after that, transform this creatingexe.py in ".exe" with command (cxfreeze .\creatingexe.py) on console. When click on creatingexe.exe on explorer, one txt of list are generated...

listaJ = ['Karol', 'Leonardo', 'Victor', 'Arthur', 'Joao', 'Andre', 'Vinicios', 'Thales', 'Elda', 'Guilherme', 'Kage']

with open('Jogadores.txt', 'w', newline='') as file:
    for line in listaJ:
        file.write(line + os.linesep)
        