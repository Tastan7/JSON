import socket
import json

def main():
    # Definerer server adresse og port
    server_address = ('localhost', 12346)  # Localhost og IP

    # Opretter en TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Forbinder til serveren
        client_socket.connect(server_address)

        # Beder brugeren om kommando, tal, osv.
        method = input("Enter command (Random/Add/Subtract): ")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        # Konstruerer JSON-besked til serveren
        request = {"method": method, "Tal1": num1, "Tal2": num2}

        # Sender beskeden til serveren
        client_socket.sendall(json.dumps(request).encode())

        # Modtager serverens svar
        response = client_socket.recv(1024)

        # Udskriver svaret
        print("Server response:", json.loads(response.decode()))

    except Exception as e:
        print("Error:", e)

    finally:
        # Lukker socket
        client_socket.close()

if __name__ == "__main__":
    main()
