from scapy.all import sniff
import json

def extract_features(pkt):
    features = {
        "length": len(pkt),
        "proto": pkt.proto if hasattr(pkt, 'proto') else 0,
    }
    print(f"Captured Packet: {features}")
    return features

print("[*] Starting packet capture...")

packets = sniff(count=100)
features = [extract_features(pkt) for pkt in packets]

with open('live_capture.json', 'w') as f:
    json.dump(features, f, indent=4)

print("[*] Packet capture successful. Saved to live_capture.json")
