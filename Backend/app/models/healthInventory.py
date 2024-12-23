#!/usr/bin/env python3
"""Home Medicine Inventory Feature"""
from app.db import db
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
        today = date.today()
        items_to_restock = CRUD.read(
            model=HealthInventory
        )
        items_to_restock_today = [item for item in items_to_restock if item.restock_date == today]
        for item in items_to_restock_today:
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

    def view_inventory(self, search_term=None):
        """Search and filter inventory"""
        items = CRUD.read(HealthInventory)
        if search_term:
            items = [item for item in items if search_term.lower() in item.drug_name.lower()]
        return items
        

    def restock(self, item, quantity_to_add, restock_date=None):
        """Restock Inventory"""
        if item:
            if quantity_to_add <= 0:
                raise ValueError('Quantity to add must be a positive number')
            # Increase quantity
            item.quantity += quantity_to_add

            # Update restock_date or set to current date
            item.restock_date = restock_date or date.today()
            CRUD.update(item)
            print(f'{item.drug_name} restocked. New quantity: {item.quantity}, Restock date: {item.restock_date}.')

    def delete_item(self, item=None):
        """Delete item from inventory"""
        if item:
            # Delete specific items
            while True:
                # warning message to user
                confirm = input(f'Are you sure you want to delete {item.drug_name} from inventory? (y/n): ')
                if confirm.lower() == 'y':
                    CRUD.delete(item)
                    print(f'{item.drug_name} has been deleted from inventory!')
                elif confirm.lower() == 'n':
                    print(f'{item.drug_name} deletion has been canceled')
                    break
                else:
                    print("Invalid input, please enter 'y' or 'n'.")

        else:
            # Delete all item
            while True:
                confirm = input('Are you sure you want to delete all items from the inventory? (y/n): ')
                if confirm.lower() == 'y':
                    items = CRUD.read(HealthInventory)
                    for item in items:
                        CRUD.delete(item)
                    print(f'All items have been deleted from the inventory')
                elif confirm.lower() == 'n':
                    print(f'All item deletion has been canceled')
                    break
                else:
                    print("Invalid input, please enter 'y' or 'n'.")
