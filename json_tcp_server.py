import socket
import json
import random

# Definerer host og port
HOST = '127.0.0.1'  # Standard loopback interface adresse (localhost)
PORT = 12346        # Port at lytte til (vælg hvilken som helst tilgængelig port)

# Funktion til at håndtere klientens forespørgsel
def handle_request(data):
    try:
        # Parser JSON-dataen
        request = json.loads(data)
        method = request.get("method")
        num1 = request.get("Tal1")
        num2 = request.get("Tal2")

        if method == "Random":
            # Generer et tilfældigt tal mellem de angivende tal (fx 1 og 10)
            random_number = random.randint(num1, num2)
            return {"result": random_number}
        elif method == "Add":
            # summet af angivne tal (fx 5+5 = 10)
            result = num1 + num2
            return {"result": result}
        elif method == "Subtract":
            # Trækker tal 2 fra tal 1 (fx 5-5 = 0)
            result = num1 - num2
            return {"result": result}
        else:
            return {"error": "Invalid command"}
    except Exception as e:
        return {"error": str(e)}

# Opretter en TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Binder socket til adressen og porten
    server_socket.bind((HOST, PORT))
    
    # Lytter efter indkommende forbindelser
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        # Accepterer indkommende forbindelser
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Behandler forbindelsen
        with client_socket:
            # Modtager data fra clienten
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Processer den modtagende data og sender en respons
            response = handle_request(data.decode())
            client_socket.sendall(json.dumps(response).encode())
