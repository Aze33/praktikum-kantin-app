from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

kantin_data = {
    "menu": ["Nasi Goreng", "Es Teh", "Gorengan"]
}

@app.route('/api/info', methods=['GET'])
def get_info():
    # Menangkap variabel lingkungan dari Kubernetes YAML
    nama_mahasiswa = os.getenv('NAMA_MAHASISWA', 'Nama Default')
    nim_mahasiswa = os.getenv('NIM_MAHASISWA', '000000')
    
    # Memasukkan identitas ke dalam respons
    response_data = {
        "nama_kantin": "Kantin FPMIPA",
        "identitas": f"{nama_mahasiswa} - {nim_mahasiswa}",
        "menu": kantin_data["menu"]
    }
    return jsonify(response_data)

@app.route('/api/add-menu', methods=['POST'])
def add_menu():
    new_item = request.json.get('item')
    if new_item:
        kantin_data["menu"].append(new_item)
        return jsonify({"message": "Menu berhasil ditambah!", "menu": kantin_data["menu"]}), 201
    return jsonify({"error": "Data tidak valid"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)