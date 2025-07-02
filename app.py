from flask import Flask, render_template, request, jsonify
import block_sites
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open("config.json", "r") as f:
        config = json.load(f)
    return render_template("index.html", config=config)

@app.route('/block', methods=['POST'])
def block():
    block_sites.block_domains()
    block_sites.block_ips()
    return jsonify({"status": "success", "message": "Blocked successfully."})

@app.route('/unblock', methods=['POST'])
def unblock():
    block_sites.unblock_domains()
    block_sites.unblock_ips()
    return jsonify({"status": "success", "message": "Unblocked successfully."})

@app.route('/update_config', methods=['POST'])
def update_config():
    data = request.get_json()
    with open("config.json", "w") as f:
        json.dump(data, f, indent=2)
    return jsonify({"status": "success", "message": "Config updated."})

if __name__ == '__main__':
    app.run(debug=True)
