# "git mit is csináltam ma?" 

### Leírás
Ez egy tool ami segít a nap végi logoláshoz amikor nem tudom hogy mit is csináltam egy pörgős nap.

### Előfeltétel
Ubuntu:
- `echo 'export HISTTIMEFORMAT="%y-%m-%d %T "' >> ~/.bashrc`

Ezzel a history kap egy időbéjeget `<parancssorszám> <év-hónap-nap> <óra:perc:másodperc> <parancs>`

pl.: `1946  22-02-21 11:26:33 history`.

### A program működése
Adott fájlt ( `~/.bash_history`-t ) megnézi hogy adott napon szerepel-e a `git commit` vagy (nálam legalábbis) röviden a `gcm` szavak.

> Itt fontos megjegyezni hogy ha dolgozom akkor a commit üzenetben mindig van egy ID ami álltalában Jira ID ami alapján könnyű beazonosítani hogy ott kb. mi volt a feladat.

### Futtatás
Mivel a progi elején nincs definiálva hogy mit használjon a futtatáshoz ezért mi mondjuk meg hogy mivel fusson valahogy így:
```sh
python3 gmicsi.py
```
> Ha neked csak python3-as van telepítva akkor elég `python`-ként hívni.