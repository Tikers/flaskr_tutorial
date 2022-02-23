# Flask 

## Createn and activate venv
-create virtual env:
python3 -m venv .venv
-activate .venv
. venv/bin/activate

## On Raspberry Pi

sudo apt install python3-pip
sudo pip3 install flask

## tutorial



## Quick start
# Converter types

```python
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

string
(default) accepts any text without a slash
int
accepts positive integers
float
accepts positive floating point values
path
like string but also accepts slashes
uuid
accepts UUID strings

