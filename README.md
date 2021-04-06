# Personal Knowledge Base

A Personal Knowledge Base is a place to store one's personal knowledge for later reference.

## Pre-Requisites

- mongodb running on port 27017
  ```bash
  brew install mongodb-community
  brew services start mongodb-community
  ```

## Installation
```
./kb-scripts.sh init
```

## Usage

Run the api server:
```
./kb-scripts.sh serve
```

I suggest using the following alias for convenience:
```
alias kb=./kb-scripts.sh
```
