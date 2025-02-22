from beem import Hive
from concurrent.futures import ThreadPoolExecutor

def read_node_file():
    with open('config/node.txt', 'r') as file:
        return file.read()

def read_accounts_file():
    with open('accounts.txt', 'r') as file:
        accounts = []
        for line in file.readlines():
            data = {
                'username': line.strip().split(':')[0],
                'active': line.strip().split(':')[1],
                'posting': line.strip().split(':')[2]
            }
            accounts.append(data)
        print(accounts)
        return accounts
    
def transfer_to_main(account):
    passwords = [account['active']]
    

from concurrent.futures import ThreadPoolExecutor
import time

def process_transfer(account):
    """Wrapper function to handle transfer with error handling."""
    while True:  # Ensures retry on failure
        try:
            transfer_to_main(account)  # Perform the transfer
            break  # Exit loop if successful
        except Exception as e:
            print(f"Error processing {account['username']}: {e}")
            time.sleep(1)  # Wait before retrying (prevents excessive retries)

def main():
    accounts = [...]  # Assuming this list is defined
    valid_accounts = [acc for acc in accounts if acc['username'] in read_alt_usernames_file()]

    with ThreadPoolExecutor(max_workers=10) as executor:  # Limits concurrent threads to 10
        future_threads = [executor.submit(process_transfer, acc) for acc in valid_accounts]

        # Wait for all transfers to finish
        for future in future_threads:
            future.result()

if __name__ == "__main__":
    main()
