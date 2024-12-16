#!/usr/bin/env python3
"""Global CRUD functions to be used in other classes"""
from app import db
from sqlalchemy.exc import IntegrityError

class CRUD():
    """Global create, read, update and delete"""

    @staticmethod
    def create(item):
        """Add an item to the database"""
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            raise Exception(f'Failed to create item: {e}')

    @staticmethod
    def read(model, **filters):
        """
        Reads an item or items from the database.
        Args:
            model: The database model to query.
            **filters: Key-value pairs to filter the query.
        Returns:
            Query result(s) based on the filters.
        """
        query = db.session.query(model)
        if filters:
            query = query.filter_by(**filters)
        return query.all()

    @staticmethod
    def update(item, **fields):
        """
        Updates an existing item with new field values.
        Args:
            item: The object to update.
            **fields: The fields to update as key-value pairs.
        """
        if not item:
            raise ValueError('Item does not exist')
        for field, value in fields.item:
            setattr(item, field, value)
        db.session.commit()
        
    @staticmethod
    def delete(item):
        """
        Deletes an item from the database.
        Args:
            item: The object to delete.
        """
        if not item:
            raise ValueError('Item does not exist')
        try:
            db.session.delete(item)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            raise Exception(f'Failed to delete item: {e}')
