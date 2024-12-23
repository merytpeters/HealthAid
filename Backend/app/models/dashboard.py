#!/usr/bin/env python3
"""User dashboard, concepts to look at : SQLALCHEMY relationships, marshmallow, matplotlib and matlib"""
from app.db import db
from datetime import datetime, timezone
import matplotlib.pyplot as plt
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Dashboard(db.Model):
    """Dashboard on the home page that takes and display all metrics"""
    __tablename__ = 'dashboard'

    id = db.Column(db.Integer, primary_key=True)
    personal_information_id = db.Column(db.Integer, db.ForeignKey('personal_information.id'))
    physical_attributes_id = db.Column(db.Integer, db.ForeignKey('physical_attributes.id'))
    health_metrics_id = db.Column(db.Integer, db.ForeignKey('health_metrics.id'))

    personal_information = db.relationship("PersonalInformation", backref="dashboard", uselist=False)
    physical_attributes = db.relationship("PhysicalAttributes", backref="dashboard", uselist=False)
    health_metrics = db.relationship("HealthMetrics", backref="dashboard", uselist=False)

    created_at = db.Column(db.DateTime, default=datetime.now(tz=timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(tz=timezone.utc), onupdate=datetime.now(tz=timezone.utc))

    def generate_dashboard(self):
        personal_info = self.personal_information
        physical_attributes = self.physical_attributes
        health_metrics = self.health_metrics

        dashboard_data = {
            "name" : personal_info.name,
            "age" : personal_info.age, 
            "weight" : physical_attributes.weight,
            "height" : physical_attributes.height,
            "gender" : physical_attributes.gender,
            "blood_sugar" : health_metrics.blood_sugar,
            "blood_pressure" : {
                "systolic": health_metrics.systolic,
                "diastolic": health_metrics.diastolic
            },
            "heart_rate" : health_metrics.heart_rate,
            "body_temperature" : health_metrics.body_temperature
        }

        return dashboard_data
    
    def plot_metrics(self):
        """Graphs"""
        metrics = [
            self.health_metrics.blood_sugar,
            self.health_metrics.heart_rate
        ]
        labels = ['Blood Sugar', 'Heart Rate']
        plt.bar(labels, metrics)
        plt.title('Health Metrics')
        plt.savefig('health_metrics.png')


class PersonalInformation(db.Model):
    """Personal Information"""
    __tablename__ = 'personal_information'
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def add_info(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return {
            "name": self.name,
            "age": self.age
        }
    
    
class PhysicalAttributes(db.Model):
    """Physical Attributes"""
    __tablename__ = 'physical_attributes'
    
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=True, default=0.0)
    weight_unit = db.Column(db.String, nullable=False, default="kg")
    height = db.Column(db.Float, nullable=True, default=0.0)
    height_unit = db.Column(db.String, nullable=False, default="ft")
    gender = db.Column(db.String, nullable=True)
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def add_attr(self, weight, height, gender):
        if weight < 0 or height < 0:
            raise ValueError("Weight and height must be positive")
        self.weight = weight
        self.height = height
        self.gender = gender

    def get_weight_in_kg(self):
        """Converts weight to kilograms if needed"""
        if self.weight_unit == "lbs":
            return self.weight * 0.453592
        return self.weight
    
    def get_height_in_cm(self):
        """Converts heights to centimeters if needed"""
        if self.height_unit == "in":
            return self.height * 2.54
        return self.height
    
    def get_height_in_ft(self):
        """"Converts height to feet if needed"""
        if self.height_unit == "cm":
            return self.height / 30.48
        elif self.height_unit == "in":
            return self.height / 12
        return self.height
    
    
class HealthMetrics(db.Model):
    """HealthMetrics"""
    __tablename__ = 'health_metrics'
    
    id = db.Column(db.Integer, primary_key=True)
    blood_sugar = db.Column(db.Float, nullable=True, default=0.0)
    systolic = db.Column(db.Integer, nullable=True, default=0)
    diastolic = db.Column(db.Integer, nullable=True, default=0) # need to add units for these
    blood_pressure_unit = ''
    heart_rate = db.Column(db.Integer, nullable=True, default=0)
    heart_rate_unit = ''
    body_temperature = db.Column(db.Float, nullable=True, default=0.0)
    body_temperature_unit = ''
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def add_metrics(self, blood_sugar, systolic, diastolic, heart_rate, body_temperature):
        if blood_sugar < 0 or body_temperature < 0:
            raise ValueError("Blood sugar and body temperature must be positive")
        self.blood_sugar = blood_sugar
        self.systolic = systolic
        self.diastolic = diastolic
        self.heart_rate = heart_rate
        self.body_temperature = body_temperature

    def get_metrics(self):
        return {
            "blood_sugar": self.blood_sugar,
            "blood_pressure": {
                "systolic": self.systolic,
                "diastolic": self.diastolic
            },
            "heart_rate": self.heart_rate,
            "body_temperature": self.body_temperature
        }


class DashboardSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Dashboard
        include_relationships = True
        load_instance = True


class PersonalInformationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PersonalInformation
        load_instance = True


class PhysicalAttributesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PhysicalAttributes
        load_instance = True


class HealthMetricsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HealthMetrics
        load_instance = True
