import cv2
import argparse
import sys

def read_rtsp_stream(url):
    # Create a video capture
    cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)
    
    if not cap.isOpened():
        print("Error: Unable to open RTSP stream")
        sys.exit(1)

    try:
        while True:
            # Read a frame
            ret, frame = cap.read()
            
            if not ret:
                print("Error: Unable to read frame")
                break

            # Display the frame
            cv2.imshow('RTSP Stream', frame)
            
            # Exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    finally:
        # Release resources
        cap.release()
        cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description='Read an RTSP stream')
    parser.add_argument('rtsp_url', type=str, help='URL of the RTSP stream (e.g., rtsp://example.com/stream)')
    
    args = parser.parse_args()
    read_rtsp_stream(args.rtsp_url)

if __name__ == "__main__":
    main() 