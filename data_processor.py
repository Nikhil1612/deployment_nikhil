import time

def process_data(data):
    # Example processing (replace with your actual logic)
    return [d * 2 for d in data]

if __name__ == "__main__":
    while True:
        sample_data = [1, 2, 3, 4, 5]
        processed = process_data(sample_data)
        print("Processed Data:", processed)
        # Pause for a specified amount of time (e.g., 10 seconds) before the next iteration
        time.sleep(10)
