class Animal:

    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    def __init__(self, name, species):
        self.name = name
        self._species = species
    
    #adding property director
    @property
    def species(self):
        return self._species 
    
    #updating species method with species setter
    @species.setter
    def species(self,into):
        #testing to see if a valid species
        assert into in Animal.valid_species, Exception(f'invalid species: {into}')
        #returning the updated species
        self._species = into

    def __repr__(self):
        return f'{self.name} ({self._species})'