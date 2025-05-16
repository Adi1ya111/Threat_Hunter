# packet_capture.py

from scapy.all import sniff
import json
from datetime import datetime

def packet_to_dict(pkt):
    """Convert scapy packet to a serializable dictionary with length and protocol."""
    return {
        'length': len(pkt),
        'proto': pkt.proto if hasattr(pkt, 'proto') else None
    }

def capture_packets(count=100, iface='wlan0', output_file='live_capture.json'):
    """Capture 100 packets from the WiFi interface and store in a JSON file."""
    print(f"[*] Starting packet capture on WiFi interface {iface}...")

    packets = sniff(count=count, iface=iface)
    print(f"[*] Captured {len(packets)} packets.")

    packet_list = [packet_to_dict(pkt) for pkt in packets]

    with open(output_file, 'w') as f:
        json.dump(packet_list, f, indent=4)

    print(f"[*] Packet capture saved to {output_file}")

if __name__ == '__main__':
    capture_packets()
