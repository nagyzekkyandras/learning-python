Install requirements
```sh
pip3 install -r requirements.txt --ignore-installed
```
Check requirements
```sh
python3 -c "import flask; print(flask.__version__)"
```
Database init
```sh
python3 init_db.py
```
Run app
```sh
export FLASK_APP=project
export FLASK_DEBUG=1

flask run
```