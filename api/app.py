from flask import Flask, request, jsonify
from article_processor import ArticleProcessor

app = Flask(__name__)
article_processor = ArticleProcessor()

@app.route('/analyze', methods=['POST'])
def analyze():
    """Endpoint to analyze a given article."""
    article = request.json.get('article')
    if not article:
        return jsonify({'error': 'No article provided'}), 400

    analysis = article_processor.analyze_article(article)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True)
