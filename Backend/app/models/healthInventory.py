#!/usr/bin/env python3
"""Home Medicine Inventory Feature"""
from app.db import db
from datetime import date, timedelta, datetime
from app.utils.crud import CRUD


class HealthInventory(db.Model):
    """An Inventory class to keep track of home health supplies"""
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    drug_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    inventory_date = db.Column(db.Date, default=date.today, nullable=False)
    restock_date = db.Column(db.Date, nullable=True)

    def __init__(self, *args, **kwargs):
        """Set default restock_date if not entered by the user"""
        super().__init__(*args, **kwargs)
        if isinstance(self.expiry_date, str):
            self.expiry_date = datetime.strptime(self.expiry_date, '%Y-%m-%d').date()  # Convert string to date
        if not self.restock_date and self.expiry_date:
            self.calculate_default_restock_date()

    def to_dict(self):
        """Convert the item to a dictionary for JSON serialization"""
        return {
            "id": self.id,
            "drug_name": self.drug_name,
            "quantity": self.quantity,
            "unit": self.unit,
            "expiry_date": self.expiry_date.isoformat(),
            "restock_date": self.restock_date.isoformat() if self.restock_date else None,
            "inventory_date": self.inventory_date.isoformat()
        }

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

    @staticmethod
    def restock_notification():
        """Notifies user when restock date reached"""
        today = date.today()
        items_to_restock = CRUD.read(model=HealthInventory)
        items_to_restock_today = [item for item in items_to_restock if item.restock_date <= today]
        for item in items_to_restock_today:
            print(f'{item.drug_name} needs restocking!')

    def add_item(self, drug_name, quantity, unit, user_id, expiry_date, restock_date=None,):
        """Add item to the inventory"""
        if isinstance(expiry_date, str):
            expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').date()  # Convert string to date
        new_item = self.__class__(
            drug_name=drug_name,
            quantity=quantity,
            unit=unit,
            expiry_date=expiry_date, 
            restock_date=restock_date,
            user_id=user_id
        )
        added_item = CRUD.create(new_item)
        if added_item is None:
            return None
        return added_item

    def view_inventory(self, search_term=None, page=1, per_page=10):
        """Search and filter inventory"""
        query = CRUD.read(HealthInventory)
        if search_term:
            query = query.filter(HealthInventory.drug_name.ilike(f'%{search_term}%'))
        paginated_items = query.limit(per_page).offset((page - 1) * per_page)
        return paginated_items.all()
    
    def restock(self, quantity_to_add, restock_date=None):
        """Restock Inventory"""
        if quantity_to_add <= 0:
            raise ValueError('Quantity to add must be a positive number')
        # Increase quantity
        self.quantity += quantity_to_add
        # Update restock_date or set to current date
        self.restock_date = restock_date or date.today()
        db.session.commit()
        return self

    def items_due_for_restock(self, restock_date=None):
        """
        Retrieves items due for restock.
        :param restock_date: The date to use for restock filtering (default: today's date)
        :return: List of items due for restock
        """
        restock_date = restock_date or date.today()
        items_due = CRUD.read(model=HealthInventory, restock_date__lte=restock_date)
        return items_due

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
                    return item
                elif confirm.lower() == 'n':
                    print(f'{item.drug_name} deletion has been canceled')
                    break
                else:
                    print("Invalid input, please enter 'y' or 'n'.")
        else:
            # Delete all items
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

    def delete_expired_items(self, expired_date=None):
        """Deletes expired items from the inventory."""
        expired_date = expired_date or date.today()
        expired_items = CRUD.read(
            model=HealthInventory,
            filters={"expiry_date__lte": expired_date}
        )
        deleted_items = []
        for item in expired_items:
            deleted = self.delete_item(item=item)
            deleted_items.append(deleted)
        
        return deleted_items

