from flask import Blueprint, request, jsonify
from utils.crud import CRUD
from app.models.dashboard import Dashboard, DashboardSchema, PersonalInformation, PhysicalAttributes, HealthMetrics

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
def get_dashboard():
    dashboards = Dashboard.query.all()
    dashboard_schema = DashboardSchema(many=True)
    return jsonify(dashboard_schema.dump(dashboards))

@dashboard_bp.route('/dashboard/<int:id>', methods=['GET'])
def get_dashboard_by_id(id):
    dashboard = Dashboard.query.get_or_404(id)
    dashboard_schema = DashboardSchema()
    return jsonify(dashboard_schema.dump(dashboard))

@dashboard_bp.route('/dashboard', methods=['POST'])
def create_dashboard():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    personal_info_data = data.get('personal_information')
    physical_attr_data = data.get('physical_attributes')
    health_metrics_data = data.get('health_metrics')

    if not personal_info_data or not physical_attr_data or not health_metrics_data:
        return jsonify({"error": "Missing required fields"}), 400

    personal_info = PersonalInformation(**personal_info_data)
    physical_attr = PhysicalAttributes(**physical_attr_data)
    health_metrics = HealthMetrics(**health_metrics_data)

    CRUD.create(personal_info)
    CRUD.create(physical_attr)
    CRUD.create(health_metrics)

    dashboard = Dashboard(
        personal_information_id=personal_info.id,
        physical_attributes_id=physical_attr.id,
        health_metrics_id=health_metrics.id
    )

    CRUD.create(dashboard)

    dashboard_schema = DashboardSchema()
    return jsonify(dashboard_schema.dump(dashboard)), 201

@dashboard_bp.route('/dashboard/<int:id>', methods=['PUT'])
def update_dashboard(id):
    dashboard = Dashboard.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    if 'personal_information' in data:
        personal_info_data = data['personal_information']
        personal_info = PersonalInformation.query.get(dashboard.personal_information_id)
        personal_info.name = personal_info_data.get('name', personal_info.name)
        personal_info.age = personal_info_data.get('age', personal_info.age)
        CRUD.update(personal_info)

    if 'physical_attributes' in data:
        physical_attr_data = data['physical_attributes']
        physical_attr = PhysicalAttributes.query.get(dashboard.physical_attributes_id)
        physical_attr.weight = physical_attr_data.get('weight', physical_attr.weight)
        physical_attr.height = physical_attr_data.get('height', physical_attr.height)
        physical_attr.gender = physical_attr_data.get('gender', physical_attr.gender)
        CRUD.update(physical_attr)

    if 'health_metrics' in data:
        health_metrics_data = data['health_metrics']
        health_metrics = HealthMetrics.query.get(dashboard.health_metrics_id)
        health_metrics.blood_sugar = health_metrics_data.get('blood_sugar', health_metrics.blood_sugar)
        health_metrics.systolic = health_metrics_data.get('systolic', health_metrics.systolic)
        health_metrics.diastolic = health_metrics_data.get('diastolic', health_metrics.diastolic)
        health_metrics.heart_rate = health_metrics_data.get('heart_rate', health_metrics.heart_rate)
        health_metrics.body_temperature = health_metrics_data.get('body_temperature', health_metrics.body_temperature)
        CRUD.update(health_metrics)

    CRUD.update(dashboard)

    dashboard_schema = DashboardSchema()
    return jsonify(dashboard_schema.dump(dashboard))

@dashboard_bp.route('/dashboard/<int:id>', methods=['DELETE'])
def delete_dashboard(id):
    dashboard = Dashboard.query.get_or_404(id)
    CRUD.delete(dashboard)
    return '', 204

@dashboard_bp.route('/displaymetriclinegraph/<int:id>', methods=['GET'])
def display_line_graph(id):
    dashboard = Dashboard.query.get_or_404(id)
    dashboard.plot_metrics()    

@dashboard_bp.route('/displaymetricpiechart/<int:id>', methods=['GET'])
def display_piechart(id):
    dashboard = Dashboard.query.get_or_404(id)
    dashboard.plot_piechart()