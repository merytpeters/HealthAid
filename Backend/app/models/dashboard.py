#!/usr/bin/env python3
"""User dashboard, concepts to look at : SQLALCHEMY relationships, marshmallow, matplotlib and matlib"""
from marshmallow import fields
from app.db import db
from datetime import datetime, timezone
import matplotlib.pyplot as plt
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Dashboard(db.Model):
    """Dashboard on the home page that takes and display all metrics"""
    __tablename__ = 'dashboard'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
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
        """Graphs health metrics against time"""
        if not self.health_metrics:
            print("No health metrics to plot")
            return
        
        times = []
        blood_sugar = []
        heart_rate = []
        systolic_bp = []
        diastolic_bp = []

        metric = self.health_metrics
        if metric.timestamp is not None:
            times.append(metric.timestamp)

        blood_sugar.append(metric.blood_sugar or 0)
        heart_rate.append(metric.heart_rate or 0)
        systolic_bp.append(metric.systolic or 0)
        diastolic_bp.append(metric.diastolic or 0)
        
        if not times:
            print("No valid timestamps found in health metrics.")
            return

        plt.figure(figsize=(10, 6))
        plt.plot(times, blood_sugar, label='Blood Sugar')
        plt.plot(times, heart_rate, label='Heart Rate')
        plt.plot(times, systolic_bp, label='Systolic BP')
        plt.plot(times, diastolic_bp, label='Diastolic BP')
        plt.xlabel('Time')
        plt.ylabel('Metrics')
        plt.title('Health Metrics Over Time')
        plt.legend()
        plt.savefig('health_metrics.png')
        plt.close()
        print("Plot saved as health_metrics.png")

    def plot_piechart(self):
        """Piechart of metrics"""
        if not self.health_metrics:
            print('No metrics to plot')
            return []

        blood_sugar = []
        heart_rate = []
        systolic_bp = []
        diastolic_bp = []

        blood_sugar = self.health_metrics.blood_sugar or 0
        heart_rate = self.health_metrics.heart_rate or 0
        systolic_bp = self.health_metrics.systolic or 0
        diastolic_bp = self.health_metrics.diastolic or 0
        
        labels = ['Blood Sugar', 'Heart Rate', 'Systolic BP', 'Diastolic BP']
        sizes = [blood_sugar, heart_rate, systolic_bp, diastolic_bp]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0, 0)  # explode 1st slice

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Health Metrics Distribution')
        plt.savefig('health_metrics_piechart.png')
        plt.close()
        print("Pie chart saved as health_metrics_piechart.png")
        diastolic_bp = []
    

class PersonalInformation(db.Model):
    """Personal Information"""
    __tablename__ = 'personal_information'
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    
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
    weight_unit = db.Column(db.String(25), nullable=False, default="kg")
    height = db.Column(db.Float, nullable=True, default=0.0)
    height_unit = db.Column(db.String(25), nullable=False, default="ft")
    gender = db.Column(db.String(25), nullable=True)
    
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
    blood_sugar_unit = db.Column(db.String(50), nullable=False, default="mg/dL")
    systolic = db.Column(db.Integer, nullable=True, default=0)
    diastolic = db.Column(db.Integer, nullable=True, default=0) 
    blood_pressure_unit = db.Column(db.String(50), nullable=False, default="mmHg")
    heart_rate = db.Column(db.Integer, nullable=True, default=0)
    heart_rate_unit = db.Column(db.String(50), nullable=False, default="bpm")
    body_temperature = db.Column(db.Float, nullable=True, default=0.0)
    body_temperature_unit = db.Column(db.String(50), nullable=False, default="C")
    timestamp = db.Column(db.DateTime, default=datetime.now(tz=timezone.utc))
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def convert_blood_sugar_to_mmol_per_l(self):
        """Converts blood sugar to mmol per liter"""
        if self.blood_sugar_unit == "mg/dL":
            return self.blood_sugar / 18.0182
        return self.blood_sugar
    
    def convert_temperature_to_fahrenheit(self):
        """Converts temperature to fahrenheit"""
        if self.body_temperature_unit == "C":
            return (self.body_temperature * 9/5) + 32
        return self.body_temperature

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

class DashboardSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Dashboard
        include_relationships = True
        load_instance = True

    personal_information = fields.Nested(PersonalInformationSchema)
    physical_attributes = fields.Nested(PhysicalAttributesSchema)
    health_metrics = fields.Nested(HealthMetricsSchema)
