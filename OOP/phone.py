from Items import Item

class Phone(Item):
  
    def __init__(self, name: str, price: float, quantity=1, broken=0) -> None:
        #super function to inherit the parent class' attributes and methods
        super().__init__(name, price, quantity)
    
        assert broken >= 0, "Broken is zero"

        self.broken = broken

   