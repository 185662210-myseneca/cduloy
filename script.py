#!/usr/bin/env python3

class ProductStock:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
 
    def make_sale(self, amt):
        self.stock -= amt
        print(f'You take {amt} down, and pass it around')
    
    @property
    def in_stock(self):
        return self.stock > 0
    
    def __repr__(self):
        return f'{self.name} {self.stock}x'
    
    def __str__(self):
        return f'{self.stock} bottles of {self.name} on the wall, {self.stock} bottles of {self.name}'
    
    def __sub__(self, amt):
      self.make_sale(amt)
      return self
