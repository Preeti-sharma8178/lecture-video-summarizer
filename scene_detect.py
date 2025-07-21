import cv2

def detect_scenes(video_path):
    cap = cv2.VideoCapture(video_path)
    prev_frame = None
    scenes = []
    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if prev_frame is not None:
            diff = cv2.absdiff(gray, prev_frame)
            score = diff.mean()
            if score > 30:
                scenes.append(frame_id)
        prev_frame = gray
        frame_id += 1

    cap.release()
    return scenes
