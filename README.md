# Fancaps Downloader

## About <a name = "about"></a>

This project it's a simple Python script for download screencaps from https://fancaps.net.

## Rate Limit
If the images are too small, you may hit the rate limit. If this happens you will want to add: `--slow` at the end of the command.
You will either have to wait a while for the limit block to pass, or use a vpn.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

To run this script you need to have Python 3.x installed, the Beautifulsoup4 and tqdm library:

#### python install: 
https://www.python.org/downloads/

#### Beautifulsoup4 and tqdm install: 
```
pip install beautifulsoup4 tqdm
```

## Usage <a name = "usage"></a>

### Arguments
`url`: Url of ressource to download

`--output`: Folder used for download each images

### Url support:
* `https://fancaps.net/{tv|anime}/showimages.php?...`: Url of season page
* `https://fancaps.net/{tv|anime}/episodeimages.php?...`: Url of episode page
* `https://fancaps.net/movies/MovieImages.php?...`: Url of movie page

Warning: Due to an issue with `&` caractère in args. Use double quote for the URL argument

### Usage exemple:

```
python fancaps-downloader.py --output "Download" URL
```
In this exemple we download all pics of URL into Download folder
 
## TODO List <a name = "todo_list"></a>
- Input txt file for bulk
- Add more arguments

