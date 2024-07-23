#!/usr/bin/env python3


class ProductStock:
    def _init_(self, name, stock):
        self.name = name
        self.stock = stock
        self.in_stock = stock > 0

    def make_sale(self, amt):
        self.stock -= amt
        print(f'You take {amt} down, and pass it around')
        self.in_stock = self.stock > 0
        
    def _sub_(self, amt):
        self.make_sale(amt)
        return self
    
    def _repr_(self):
        return f'{self.name} {self.stock}x'
    
    def _str_(self):
        return f'{self.stock} bottles of {self.name} on the wall, {self.stock} bottles of {self.name}'
