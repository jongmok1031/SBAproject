# url, parser, path, api, apikey -> all str type
from dataclasses import dataclass

@dataclass
class Entity:
    
    url: str = '/Users/jongm/SBAprojects/titanic/data/'
    parser: str = ''
    path: str = ''
    api: str = ''
    apikey: str = ''
