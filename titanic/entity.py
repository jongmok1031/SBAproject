class Entity:
    def __init__(self, context, fname, train, test, id, label):
        self._context = context # _1개는 default 접근의미, __는 private접근의미
        self._fname = fname
        self._train = train
        self._test = test
        self._id = id
        self._label = label

    # context get, set 를 만듦

    @property
    def context(self) -> str:
        return self._context
    
    @context
    def context(self, context):
        self._context = context

    # fname get,set 만듦
    @property
    def fname(self) -> str:
        return self._fname
    
    @context
    def fname(self, fname):
        self._fname = fname
    # train get,set 만듦
    
    # test get,set 만듦
    
    # id get,set 만듦
    
    # label get,set 만듦