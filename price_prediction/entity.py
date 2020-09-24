from dataclasses import dataclass
@dataclass
class Entity:
    context: str = '/Users/jongm/SBAprojects/cabbage/data/'
    filename: str = ''
    train : object = None
    test : object = None
    id : str = ''
    label : str = ''
    # 전형적인 지도학습 entity
    