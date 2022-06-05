# PetRx Web Server / Flask Web App

## Setup & Installtion

Make sure you have the latest version of Python installed.

```bash
git clone <https://github.com/Castor-Digital/PetRx-webserver>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`

## Possible Errors:

- ImportError: "DLL load failed while importing _sqlite3: The specified module could not be found."
-> go to this link: https://www.sqlite.org/download.html
-> download the zip for your machine under "precompiled binaries"
-> extract "sqlite3.dll" and place it in Users\yourname\anaconda3\DLLs