import requests
from flask import Flask, jsonify, render_template, request
from sales_analysis import calculate_sales_metrics 

app = Flask(__name__)

@app.route('/analyze_sales', methods=['POST'])
def analyze_sales():
    if 'csv_file' not in request.files:
        return 'CSV file not provided', 400

    csv_file = request.files['csv_file']
    # Add file saving logic if you want to store it on the server

    sales_metrics = calculate_sales_metrics(csv_file.stream) 
    return jsonify(sales_metrics)

# Store your Cardmarket API key in config.json
import json
with open('config.json') as f:
    config = json.load(f)
    API_KEY = config['api_key']  

# A route to fetch the best selling cards
@app.route('/get_best_selling', methods=['GET'])
def get_best_selling():
    search_term = request.args.get('search', 'best selling')  

    # Placeholder for your Cardmarket API logic 
    response = requests.get('https://api.cardmarket.com/ws/v2.0/output.json/products/find', 
                            params={'search': search_term,
                                    # ... other relevant parameters}, 
                            headers={ # ... Your authorization headers }) 

    if response.status_code == 200:
        card_data = response.json()
        return jsonify(card_data)
    else:
        return 'Error fetching data', 500 

if __name__ == '__main__':
    app.run(debug=True) 
