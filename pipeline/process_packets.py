import joblib, json, numpy as np, pandas as pd, requests

with open('live_capture.json') as f:
    packets = pd.DataFrame(json.load(f))

model = joblib.load('model/model.joblib')
scaler = joblib.load('model/scaler.joblib')

X = scaler.transform(packets)
scores = model.decision_function(X)
z_scores = (scores - np.mean(scores)) / np.std(scores)

def label(z): return 'High' if z < -2 else 'Medium' if z < -1 else 'Low'
packets['z_score'] = z_scores
packets['threat_level'] = [label(z) for z in z_scores]

def send_to_elasticsearch(docs, index="packet-anomalies"):
    bulk_data = ""
    for doc in docs:
        meta = {"index": {}}
        bulk_data += json.dumps(meta) + "\n"
        bulk_data += json.dumps(doc) + "\n"
    response = requests.post(
        f"http://localhost:9200/{index}/_bulk",
        headers={"Content-Type": "application/x-ndjson"},
        data=bulk_data
    )
    print("Elasticsearch response:", response.status_code, response.text[:200])

send_to_elasticsearch(packets.to_dict(orient="records"))