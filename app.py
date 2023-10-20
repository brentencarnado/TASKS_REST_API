from flask import Flask, jsonify, request

students = [
    {
        'id': 1,
        'name': 'Brent',
        'grade': 100
    },
    {
        'id': 2,
        'name': 'Jack',
        'grade': 75
    }
]

app = Flask(__name__)

@app.route('/')
def hello():
    return "Working"

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({'students': students})

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = None
    for t in students:
        if t["id"] == student_id: 
            student = t
            break
    if student is None:
        return jsonify({'error': 'student not found'}), 404
    return jsonify({'student': student})

@app.route('/students', methods=['POST'])
def add_student():

    score = request.json.get('grade', False)

    new_student = {
        'id': len(students) + 1, 
        'name': request.json['name'],  
        'grade': score  
    }

    students.append(new_student)

    return jsonify({'student': new_student}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = None
    for t in students:
        if t["id"] == student_id: 
            break
    
    if student is None:
        return jsonify({'error': 'student not found'}), 404
    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    return jsonify({'student': student})

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students 
    student = None
    for t in students:
        if t["id"] == student_id: 
            student = t
            break
    if student is None:
        return jsonify({'error': 'student not found'}), 404
    students.remove(student)
    return jsonify({'result': 'student deleted successfully'}), 200

if __name__ == '__main__':
    # Start the Flask development server with debugging enabled
    app.run(debug=True)