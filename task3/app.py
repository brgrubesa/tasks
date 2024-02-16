from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-max-interviews', methods=['POST'])
def calculate_max_interviews():
    # Parse JSON data from the request
    data = request.get_json()

    # Ensure start_times and end_times are present in the request
    if 'start_times' not in data or 'end_times' not in data:
        return jsonify({'error': 'Missing start_times or end_times in request'}), 400

    # Extract start_times and end_times
    start_times = data['start_times']
    end_times = data['end_times']

    # Sort the interview times based on end times
    interview_times = sorted(zip(start_times, end_times), key=lambda x: x[1])

    # Initialize variables
    max_interviews = 0
    current_end_time = 0

    # Iterate through sorted interview times
    for start_time, end_time in interview_times:
        # Check if the current interview overlaps with the previous one
        if start_time >= current_end_time:
            # Update the current end time
            current_end_time = end_time
            # Increment the number of max interviews
            max_interviews += 1

    # Return the response
    return jsonify({'max_interviews': max_interviews}), 200

if __name__ == '__main__':
    app.run(debug=True)
