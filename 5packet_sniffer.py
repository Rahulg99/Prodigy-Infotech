from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

        if TCP in packet:
            print(f"Protocol: TCP")
            tcp_layer = packet[TCP]
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
            if Raw in packet:
                print(f"Payload: {packet[Raw].load}")

        elif UDP in packet:
            print(f"Protocol: UDP")
            udp_layer = packet[UDP]
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
            if Raw in packet:
                print(f"Payload: {packet[Raw].load}")

        else:
            print(f"Protocol: Other")

        print("\n" + "-"*50 + "\n")

print("Starting packet capture. Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)
