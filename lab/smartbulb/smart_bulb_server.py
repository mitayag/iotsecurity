from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import secrets
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Bulb state
bulb_state = {
    "power": False,
    "brightness": 50,
    "color": "#FFEB3B",
    "device_id": "SB2000-" + secrets.token_hex(4),
    "firmware_version": "BULB_2_1_0"
}

@app.route('/')
def home():
    logger.info(f"Current bulb state: {bulb_state}")
    return render_template('index.html', 
                         device_id=bulb_state["device_id"],
                         firmware_version=bulb_state["firmware_version"])

@app.route('/api/control/power', methods=['POST'])
def power_control():
    try:
        data = request.get_json()
        logger.info(f"Received power control request: {data}")
        
        if data is None:
            return jsonify({"error": "No JSON data received"}), 400
            
        if 'state' not in data:
            return jsonify({"error": "No state parameter in request"}), 400
            
        bulb_state['power'] = bool(data['state'])
        logger.info(f"Power state changed to: {bulb_state['power']}")
        
        # Emit state change to all clients
        socketio.emit('state_update', bulb_state)
        
        return jsonify({
            "success": True,
            "message": f"Power {'ON' if bulb_state['power'] else 'OFF'}",
            "state": bulb_state
        })
        
    except Exception as e:
        logger.error(f"Error in power control: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/control/brightness', methods=['POST'])
def brightness_control():
    try:
        data = request.get_json()
        logger.info(f"Received brightness control request: {data}")
        
        if data is None:
            return jsonify({"error": "No JSON data received"}), 400
            
        if 'brightness' not in data:
            return jsonify({"error": "No brightness parameter in request"}), 400
            
        brightness = int(data['brightness'])
        if brightness < 0 or brightness > 100:
            return jsonify({"error": "Brightness must be between 0 and 100"}), 400
            
        bulb_state['brightness'] = brightness
        logger.info(f"Brightness changed to: {brightness}")
        
        # Emit state change to all clients
        socketio.emit('state_update', bulb_state)
        
        return jsonify({
            "success": True,
            "message": f"Brightness set to {brightness}",
            "state": bulb_state
        })
        
    except Exception as e:
        logger.error(f"Error in brightness control: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/control/color', methods=['POST'])
def color_control():
    try:
        data = request.get_json()
        logger.info(f"Received color control request: {data}")
        
        if data is None:
            return jsonify({"error": "No JSON data received"}), 400
            
        if 'color' not in data:
            return jsonify({"error": "No color parameter in request"}), 400
            
        bulb_state['color'] = data['color']
        logger.info(f"Color changed to: {data['color']}")
        
        # Emit state change to all clients
        socketio.emit('state_update', bulb_state)
        
        return jsonify({
            "success": True,
            "message": f"Color set to {data['color']}",
            "state": bulb_state
        })
        
    except Exception as e:
        logger.error(f"Error in color control: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/control/factory_reset', methods=['POST'])
def factory_reset():
    try:
        logger.info("Received factory reset request")
        
        global bulb_state
        bulb_state = {
            "power": False,
            "brightness": 50,
            "color": "#FFEB3B",
            "device_id": bulb_state['device_id'],
            "firmware_version": "BULB_2_1_0"
        }
        
        # Emit state change to all clients
        socketio.emit('state_update', bulb_state)
        
        logger.info("Factory reset completed")
        return jsonify({
            "success": True,
            "message": "Device reset to factory settings",
            "state": bulb_state
        })
        
    except Exception as e:
        logger.error(f"Error in factory reset: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify(bulb_state)

if __name__ == '__main__':
    print(f"Smart Bulb Simulator Starting")
    print(f"Device ID: {bulb_state['device_id']}")
    print(f"Web interface: http://localhost:8080")
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)