import sys
sys.path.insert(0,'/Users/jongm/SBAprojects')
import nltk
from miner.entity import Entity
from miner.service import Service
class Controller:
    def __init__(self):
        self.service =Service()
        self.entity = Entity()
        
    def getdataready(self,filename):
        service = self.service
        this = self.entity
        data = service.openfile_as_soup(filename)

        prepro_file = 'word2vec.prepro'
        this = Service.savefile(Service.append_words(service.read_data(data,filename)),prepro_file)
        print('컨트롤러에서도' + prepro_file + '생성됌표시')
        return this

    def create_model_and_prepro(self,filename):
        service = self.service
        this = self.getdataready(filename)

        prepro_file= 'word2vec.prepro'
        
        data = service.sentence_creator(prepro_file, filename)
        model_filename= 'word2vec.model'
        service.model_creator(data,model_filename,prepro_file,filename)
        print('done')

if __name__ =='__main__':
    ctrl = Controller()
    ctrl.create_model_and_prepro('문재인대통령신년사.txt')