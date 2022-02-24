# Flask 

## Createn and activate venv
create virtual env:
python3 -m venv .venv

activate the .venv:
. venv/bin/activate

powershell:
venv\Scripts\activate

## On Raspberry Pi

sudo apt install python3-pip
sudo pip3 install flask

## tutorial

run Powershell command:
> $env:FLASK_APP = "flaskr"
> $env:FLASK_ENV = "development"
> flask run


### Templates
Anything between {{ and }} is an expression that will be output to the final document. {% and %} denotes a control flow statement like if and for. Unlike Python, blocks are denoted by start and end tags rather than indentation since static text within a block could change indentation.




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

