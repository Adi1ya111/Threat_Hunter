# Network Threat Detector (Elasticsearch Direct)

## Quick Start

1. Install dependencies:
```
pip install -r requirements.txt
```
python capture/packet_capture.py


2. Train model:
```
python model/train_model.py
```

3. Process packets and send to Elasticsearch:
```
python pipeline/process_packets.py
```

4. Start the stack:
```
cd elk
docker-compose up --build
```
start http://localhost:8000

5. Open Kibana: http://localhost:5601  
   Create index pattern: `packet-anomalies`