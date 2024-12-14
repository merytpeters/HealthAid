#!/usr/bin/env python3
"""Home Medicine Inventory Feature"""
from app import db
from datetime import date, timedelta
from utils.crud import CRUD


class HealthInventory(db.Model):
    """An Inventory class to keep track of home health supplies"""
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    drug_name = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    inventory_date = db.Column(db.Date, default=date.today, nullable=False)
    restock_date = db.Column(db.Date, nullable=True)

    def __init__(self, *args, **kwargs):
        """Set default restock_date if not entered by the user"""
        super().__init__(*args, **kwargs)
        if not self.restock_date and self.expiry_date:
            self.calculate_default_restock_date()

    def use_item(self, amount):
        """Handles item use"""
        if amount <= 0:
            raise ValueError('Amount to reduce must be positive')
        if amount > self.quantity:
            raise ValueError('Not enough quantity in inventory')
        self.quantity -= amount
        return self.quantity

    def calculate_default_restock_date(self):
        """Set default restock date to two days before expiry_date"""
        if self.expiry_date:
            self.restock_date = self.expiry_date - timedelta(days=2)
        else:
            raise ValueError('Expiry date must be set to calculate restock date.')
        return self.restock_date

    def restock_notification(self):
        """Notifies user when restock date reached"""
        items_to_restock = CRUD.read(
            model=HealthInventory,
            restock_date=self.restock_date
        )
        for item in items_to_restock:
            print(f'{item.drug_name} needs restocking!')

    def add_item(
            self, drugname, quantity, unit, expiry_date,
            restock_date=None
            ):
        """Add item to the inventory"""
        new_item = self.__class__(
            drugname=drugname,
            quantity=quantity,
            unit=unit,
            expiry_date=expiry_date, 
            # inventory_date already set by default in class atrribute
            restock_date=restock_date
        )
        CRUD.create(new_item)

    def view_inventory(self):
        """Search and filter inventory"""
        pass

    def restock(self):
        """Restock Inventory"""
        pass

    def delete_item(self):
        """Delete item from inventory"""
        pass
