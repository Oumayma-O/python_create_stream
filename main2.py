import subprocess
import csv
import time
import random
# Start the nc command
process = subprocess.Popen(['nc', '-lk', '9999'], stdin=subprocess.PIPE)

# Open the CSV file
with open('customer_data.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Convert the reader to a list and shuffle it
    rows = list(reader)
    random.shuffle(rows)
    
    for row in rows:
        # Convert the row to a string and add a newline character
        data = ','.join(row) + '\n'
        
        # Send the data
        process.stdin.write(data.encode())
        process.stdin.flush()
        print(f"Sent: {data.strip()}")
        time.sleep(1)

# Close the stdin pipe
process.stdin.close()

# Wait for the nc command to terminate
process.wait()