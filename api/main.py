from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///classrooms.db'
db = SQLAlchemy(app)

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    classroom_name = db.Column(db.String(100), nullable=False)
    bookings = db.relationship('Booking', backref='classroom', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    purpose = db.Column(db.String(200), nullable=False)

@app.route('/classrooms', methods=['GET'])
def get_classrooms():
    classrooms = Classroom.query.all()
    output = []
    for classroom in classrooms:
        classroom_data = {'id': classroom.id,
                          'location': classroom.location,
                          'classroom_name': classroom.classroom_name}
        output.append(classroom_data)
    return jsonify({'classrooms': output})

@app.route('/classrooms', methods=['POST'])
def add_classroom():
    data = request.json
    new_classroom = Classroom(location=data['location'], classroom_name=data['classroom_name'])
    db.session.add(new_classroom)
    db.session.commit()
    return jsonify({'message': 'Classroom added successfully'})

@app.route('/bookings', methods=['POST'])
def book_classroom():
    data = request.json
    classroom_id = data['classroom_id']
    date = data['date']
    purpose = data['purpose']
    classroom = Classroom.query.get(classroom_id)
    if not classroom:
        return jsonify({'message': 'Classroom not found'}), 404
    new_booking = Booking(classroom_id=classroom_id, date=date, purpose=purpose)
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({'message': 'Classroom booked successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
