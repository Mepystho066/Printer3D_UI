class Addres:
    def __init__(self,Country,city,addres,postalCode):
        self.Country=Country
        self.city=city
        self.addres=addres
        self.postalCode=postalCode

    def __str__(self):
        return f"Addres(Country={self.Country},city={self.city},addres={self.addres},postalCode={self.postalCode})"

    """ 
    country TEXT,
    city TEXT , 
    addres TEXT, 
    postalCode  INTEGER,
    """
    def to_tuble(self):
        return (self.Country ,self.city ,self.addres ,self.postalCode)

    @classmethod
    def from_tuple(clss, tupleData): 
        return clss(*tupleData)