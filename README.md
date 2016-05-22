# eslpod-downloader
Python script that allows to download available episodes of http://eslpod.com podcast.

- 1200+ episodes of ESL Podcast
- 550+ episodes of English Cafe

### Params
- **-t** - type of an episode
- **-s** - start range of episodes numbers to get
- **-e** - end range of episodes numbers to get
- **-o** - number of single episode to get

### Start and end of the range
Go to the podcast's site and see which episode is the newest one (end of the range).

### Types
- **eslpod** - Original series of ESL Podcast
- **ec** - English Cafe series


### Usage
```bash
python eslpod.py -t "eslpod" -s 1 -e 1208
python eslpod.py -t "eslpod" -s 153 -e 420
```

```bash
python eslpod.py -t "eslpod" -o 1207
```

```bash
python eslpod.py -t "ec" -o 500
```

Script downloads everything what it gets from the request and stores as mp3 file. If file is not available on the server anymore, it will save 1 KB file with 404 error. Just delete such file because it can't be played anyway. Episodes 1, 12-57, 68, 182 of "eslpod" type.
