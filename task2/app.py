from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect-unauthorized-sales', methods=['POST'])
def detect_unauthorized_sales():
    # Parse JSON data from the request
    data = request.get_json()

    # Ensure productListings and salesTransactions are present in the request
    if 'productListings' not in data or 'salesTransactions' not in data:
        return jsonify({'error': 'Missing productListings or salesTransactions in request'}), 400

    # Extract product listings and sales transactions
    product_listings = data['productListings']
    sales_transactions = data['salesTransactions']

    # Initialize dictionary to store unauthorized sales
    unauthorized_sales = {}

    # Iterate over sales transactions
    for sale in sales_transactions:
        product_id = sale.get('productID')
        seller_id = sale.get('sellerID')

        if not product_id or not seller_id:
            return jsonify({'error': 'Invalid sales transaction data'}), 400

        # Check if seller is unauthorized for the product
        for listing in product_listings:
            listing_product_id = listing.get('productID')
            authorized_seller_id = listing.get('authorizedSellerID')

            if not listing_product_id or not authorized_seller_id:
                return jsonify({'error': 'Invalid product listing data'}), 400

            if listing_product_id == product_id and authorized_seller_id != seller_id:
                unauthorized_sales.setdefault(product_id, []).append(seller_id)

    # Format response
    response = {'unauthorizedSales': [{'productID': product_id, 'unauthorizedSellerID': sellers} 
                                       for product_id, sellers in unauthorized_sales.items()]}

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
