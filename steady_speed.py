import time
import keyboard  # This module allows monitoring specific keys; install with `pip install keyboard` if needed.

def collect_data_for_steady_speed_motion(distance_per_segment):
    print("Press ENTER to start the timer. Each ENTER records a time, and SPACE stops the journey and shows results.")
    input("Press ENTER when you're ready...")

    times = []
    speeds = []
    
    # Start timing with the first Enter press
    input("Press ENTER to start the journey.")
    start_time = time.time()
    times.append(start_time)
    segment_count = 0

    while True:
        # Wait for the next Enter press or a Space press to stop
        while True:
            if keyboard.is_pressed('enter'):
                current_time = time.time()
                times.append(current_time)
                segment_count += 1

                # Calculate time difference from the last segment
                segment_time = times[-1] - times[-2]

                # Calculate speed for the current segment
                speed = distance_per_segment * segment_time #calculate segment speed
                speeds.append(speed)

                print(f"Segment {segment_count}:")
                print(f"Time t{segment_count} = {segment_time:.2f} seconds")
                print(f"Distance d{segment_count} = {distance_per_segment * segment_count} cm")
                print(f"Speed v{segment_count} = {speed:.2f} cm/s\n")
                time.sleep(0.3)  # Prevents multiple detections on a single press
                break

            elif keyboard.is_pressed('space'):
                end_time = time.time()
                total_time = end_time - start_time
                total_distance = segment_count * distance_per_segment
                average_speed = total_distance * total_time if total_time > 0 else 0 #calculate total speed
                print("\nJourney Summary:")
                
                for i in range(1, segment_count + 1):
                    segment_time = times[i] - times[i - 1]
                    print(f"d{i} = {distance_per_segment * i} cm, t{i} = {segment_time:.2f} s, v{i} = {speeds[i - 1]:.2f} cm/s")

                print(f"\nTotal Distance: {total_distance} cm")
                print(f"Total Time: {total_time:.2f} s")
                print(f"Average Speed: {average_speed:.2f} cm/s")
                return  # Exit the function to end program

# Define the distance per segment (e.g., 10 cm)
distance_per_segment = 10
collect_data_for_steady_speed_motion(distance_per_segment)
