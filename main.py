from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import sys

DEFAULT_PORT = 5000

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers=["Content-Type"])


@app.route('/proxy', methods=['POST'])
def proxy():
    data = request.json
    url = data.get('url')
    method = data.get('method', 'GET').upper()
    headers = data.get('headers', {})
    body = data.get('body', None)

    try:
        response = requests.request(method, url, headers=headers, data=body)
        return jsonify({
            'status': response.status_code,
            'headers': dict(response.headers),
            'body': response.text
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"⚠️ Неверный порт: {sys.argv[1]}. Используется порт по умолчанию: {DEFAULT_PORT}")

    print(f"============================================================\n\n")
    print(f"Прокси-сервер запущен!")
    print(f"Используйте: http://localhost:{port}/proxy для подключения\n\n")
    print(f"============================================================\n")
    app.run(port=port)
