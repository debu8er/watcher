<h1 align="center">watcher</h1>
<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#tool-options">Tool options</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>

watcher is a tool for get details of watch

## Installation
* install MongoDB on local https://www.mongodb.com/docs/manual/installation/
* ```bash
  git clone https://debu8er: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@github.com/debu8er/watcher.git
  cd watch
  pip install -r requirements.txt
  python3 main.py
  ```

### Tool Options
```
options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain input.
  -a, --add             add new domain
  -r, --remove          remove domain
  -s STATUS, --status STATUS
                        filter by status.
  -t TECH, --tech TECH  filter by technologies.
  -sc, --status-changed
                        filter by status changed
  -tc, --tech-changed   filter by technologies.
  -f, --fresh           filter by fresh
  -as, --all-sub        get all sub in result.
  -fr, --full-result    get full result.
```


## Usage
Simple usage:
```bash
python3 main.py --domain domain.tld --full-result
```

Output:
```json
{
"sub": "www.domain.tld",
  "status": 302,
  "tech": PHP,
  "fresh": false,
  "status_changed": 200 : 302,
  "tech_changed": react : PHP,
  "timestamp": {
    "$date": "2023-11-01T09:17:28.845Z"
  }
}
```

## License
This project is licensed under the MIT license. See the LICENSE file for details.
