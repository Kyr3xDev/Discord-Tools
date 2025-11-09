# Develop by NK Development Team
import time
import requests
import threading

def main():
    webhook = input("Enter WebHook URL >> ").strip()
    message = input("Enter WebHook Message >> ").strip()
    threadsn = int(input("Enter Number of Threads >> "))
    sleep = float(input("Enter Sleep Time (seconds) >> "))

    def send_message():
        while True:
            try:
                response = requests.post(webhook, json={'content': message})
                if response.status_code == 204:
                    print(f"[+] Sent successfully: {message}")
                else:
                    print(f"[!] Failed ({response.status_code}): {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"[!] Error: {e}")
            time.sleep(sleep)

    print(f"\nStarting {threadsn} threads... Press Ctrl+C to stop.\n")
    for i in range(threadsn):
        thread = threading.Thread(target=send_message, daemon=True)
        thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()
