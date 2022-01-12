## Inspiration
Security is a concern of all 

## What it does
It secures your password in a way that is not understandable commmonly

## How we built it
I used python as programming langage and cryptography library to use Fernet algorithm to encrypt password 

## How to use it 
* Install required packages from requirements.txt 
* Add KEY variable and secret value in .env file and give python call as 
```python 
python encrypt.py
```
 or 
```python
 python encrypt.py {password}
 ``` 
 without curly brackets 

## What's next for Passcrypt
Passcrypt can add other encrypting algorithms and then give an option to choose based on categority of security you want.
