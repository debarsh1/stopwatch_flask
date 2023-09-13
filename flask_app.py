from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_stopwatch', methods=['POST'])
def start_stopwatch():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        time.sleep(0.1)  # Update every 0.1 seconds
        if elapsed_time >= 3600:  # If elapsed time exceeds 1 hour, stop
            break
        yield jsonify({'elapsed_time': elapsed_time})

if __name__ == '__main__':
    app.run(debug=True)
