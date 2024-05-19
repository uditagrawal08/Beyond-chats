from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://devapi.beyondchats.com/api/get_message_with_sources"


def fetch_data(page):
    try:
        response = requests.get(f"{API_URL}?page={page}")
        response.raise_for_status()  # Raises an error for bad HTTP responses
        page_data = response.json()
        return page_data['data']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page}: {e}")
        return None


def find_citations(response_text, sources):
    citations = []

    for source in sources:
        if not source["link"]:
            continue
        else:
            citations.append({
                "id": source['id'],
                "link": source.get('link', '')
            })

    return citations


def process_data(data):
    results = []
    for item in data['data']:
        response_text = item['response']
        sources = item['source']
        citations = find_citations(response_text, sources)
        results.append({
            "response": response_text,
            "source": sources,
            "citations": citations
        })
    return results


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    data = fetch_data(page)
    if data:
        processed_data = process_data(data)
        return render_template(
            'index.html',
            results=processed_data,
            current_page=page
        )
    return "Failed to fetch data"


@app.route('/next')
def next_page():
    page = request.args.get('page', 1, type=int) + 1
    if page == 14:
        return jsonify({"url": f"/?page={1}"})
    return jsonify({'url': f'/?page={page}'})


if __name__ == "__main__":
    app.run(debug=True)
