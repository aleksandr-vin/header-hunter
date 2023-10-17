# Header-Hunter

Python library for hunting HTTP headers.

Supporting paste buffer sniffing for Cookie and custom HTTP headers.


## Setup

```
python3 -m venv .venv
. .venv/bin/activate
pip install poetry
```

### Install dependencies

```
sudo apt-get install python3-tk
```

or

```
brew install python-tk
```

### Development install

```
poetry install
```


## Run

### Sniff cookies

Open a site in your browser. Log in, open Developer Tools > Network tab and right-click on any request to the domain of your choice, choose *Save as Curl*.
That will copy full request command (with cookies) to clip (paste) buffer.

```
header-hunter
```

### Help

Seek `header-hunter --help` for more options.
