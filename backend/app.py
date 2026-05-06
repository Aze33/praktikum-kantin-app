from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


kantin_data = {
    "menu": ["Blink Dagger", "Aghanim's Scepter", "Monkey King Bar"]
}

@app.route('/api/info', methods=['GET'])
def get_info():
    # Menangkap variabel lingkungan dari Kubernetes YAML
    nama_mahasiswa = os.getenv('NAMA_MAHASISWA', 'Zahran Zaidan Saputra')
    nim_mahasiswa = os.getenv('NIM_MAHASISWA', '2415429')
    
    # Menangkap nama catalog dari env, jika tidak ada default-nya langsung Dota 2 Catalog
    nama_kantin = os.getenv('NAMA_KANTIN', 'Dota 2 Item Catalog')

    # Memasukkan identitas ke dalam respons JSON
    response_data = {
        "nama_kantin": nama_kantin,
        "identitas": f"{nama_mahasiswa} - {nim_mahasiswa}",
        "menu": kantin_data["menu"]
    }
    return jsonify(response_data)

@app.route('/api/add-menu', methods=['POST'])
def add_menu():
    new_item = request.json.get('item')
    if new_item:
        kantin_data["menu"].append(new_item)
        return jsonify({"message": "Item berhasil ditambahkan!", "menu": kantin_data["menu"]}), 201
    return jsonify({"error": "Data tidak valid"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)