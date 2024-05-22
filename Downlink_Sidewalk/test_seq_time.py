import argparse
import time

def parse_arguments():
    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('--routine', help='Name of the routine to execute', required=True)
    return parser.parse_args()

def run_routine(routine_name):
    print(f"Running routine: {routine_name}")
    # Add your routine logic here

def main():
    args = parse_arguments()
    run_routine(args.routine)
    
if __name__ == "__main__":
    main()

# # After the first time, schedule the script to run after 2, 5, and 10 minutes respectively
# schedules = [120, 300, 600]  # in seconds
# for delay in schedules:
#     time.sleep(delay)
#     main()
