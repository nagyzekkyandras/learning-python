import typer
from pathlib import Path
from datetime import datetime
from datetime import timedelta

app = typer.Typer()

home = str(Path.home())
historyFile = home+"/.bash_history" # addig nem frissüla fájl amíg be nem zártad a terminál ablakokat ahol ilyen parancsokat adták ki, TODO utána nézni
sorok = []
keresettSzovegek = ["git commit", "gcm"]

ma = datetime.today()
tegnap = ma - timedelta(days=1)

maString = ma.strftime("%y-%m-%d")
tegnapString = tegnap.strftime("%y-%m-%d")

def fileOlvasEsKeres(): # 1 adatsor valójában ketté van szedve a linuxban, 1 sor timestamp #1645439193 és 1 sor ami maga a parancs
    with open(historyFile, "r", encoding="utf-8") as history:
        for egySor in history:
            egySor = egySor.strip() # sorvegi \n miatt
            sorok.append(egySor)

    print(f'Sorok száma: {len(sorok)}')

    szamlalo = 0
    for i in range(0, len(sorok)):
        for j in range(0, len(keresettSzovegek)):
            if keresettSzovegek[j] in sorok[i]:
                if "#" in sorok[i-1]:
                    idobelyeg = sorok[i-1][1:]
                    idobelyeg = datetime.fromtimestamp(int(idobelyeg))
                    if str(maString) in str(idobelyeg):
                        print(f'timestamp: {str(idobelyeg)} command: {sorok[i]}')
                        szamlalo = szamlalo + 1
    
    print(f'Összes találat: {szamlalo}')

@app.command()
def ma():
    typer.echo(f"File: {historyFile}")
    fileOlvasEsKeres()

#
# TODO
#@app.command()
#def tegnap():
#    typer.echo(f"File: {historyFile}")
#    fileOlvasEsKeres()
#

if __name__ == "__main__":
    app()
