class flexdict:
    
    def __init__(self, attributes={}):
        if not isinstance(attributes, dict):
            raise ValueError('You can init flexdict only with dict')

        self.attributes = attributes

    def __getattr__(self, name):
        print(f'run getattr for {name!r}')
        setattr(self, name, '')
        return ''

    def __setattr__(self, name, value):
        setattr(self, name, value)

#    def __getattribute__(self, name):
#        print(f'run getattribute for {name!r}')
#        setattr(self, name, '')
#        return ''
