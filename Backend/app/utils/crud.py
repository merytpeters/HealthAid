#!/usr/bin/env python3
"""
Global CRUD functions to be used in other classes
"""

from app import db
from sqlalchemy.exc import IntegrityError
import openai
import time
from config import Config

# Ensure that OpenAI API key is loaded
openai.api_key = Config.API_KEY

class CRUD:
    """Global create, read, update and delete"""

    @staticmethod
    def create(item):
        """Add an item to the database"""
        try:
            db.session.add(item)
            db.session.commit()
            return item
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
        for key, value in filters.items():
            if '__' in key:
                column_name, operator = key.split('__')
                column = getattr(model, column_name, None)

                if column:
                    if operator == 'lte':
                        query = query.filter(column <= value)
                    elif operator == 'gte':
                        query = query.filter(column >= value)
            else:
                column = getattr(model, key, None)
                if column:
                    query = query.filter(column == value)
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
        for field, value in fields.items():
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

        #import openai
#import time

# class CRUD: redundant
    @staticmethod
    def get_first_aid_guide(query):
        """
        Fetches a first aid guide from OpenAI API based on the user's query.

        Args:
            query (str): The query string for which the first aid guide is needed.

        Returns:
            str: The first aid guide generated by OpenAI or an error message.
        """
        retries = 3  # Max number of retries
        backoff_time = 5  # Initial backoff time in seconds
        for attempt in range(retries):
            try:
                response = openai.Completion.create(
                    model="gpt-3.5-turbo",
                    prompt=f"Provide a detailed first aid guide for: {query}",
                    max_tokens=200
                )
                return response.choices[0].text.strip()  # Return the text from the API response
            except openai.error.RateLimitError:
                # If rate limit exceeded, retry after backoff time
                if attempt < retries - 1:
                    print(f"Rate limit exceeded. Retrying after {backoff_time} seconds...")
                    time.sleep(backoff_time)
                    backoff_time *= 2  # Double the backoff time for each retry
                else:
                    return "Error: Rate limit exceeded after multiple retries. Please try again later."
            except openai.error.APIError:
                return "Error: There was an error with the OpenAI API. Please try again."
            except openai.error.AuthenticationError:
                return "Error: Authentication failed. Please check your API key."
            except Exception as e:
                return f"Error: {str(e)}"
