import cv2
import os

def extract_frames(video_path, output_folder, reference_frame):
    new_name = video_path.split("/")[-1].split(".")[0] + "_" + str(reference_frame)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count == int(reference_frame * fps):
            cv2.imwrite(os.path.join(output_folder, f"{new_name}.jpg"), frame)
            break

    cap.release()
    return os.path.join(output_folder, f"{new_name}.jpg")

if __name__ == "__main__":
    import json
    train_json = "dataset/train/train.json"
    output_folder = "solution/test/extracted_frames"

    with open(train_json, "r", encoding="utf-8") as f:
        train_data = json.load(f)["data"]

    for item in train_data:
        video_path = os.path.join("dataset", item["video_path"])
        
        for reference_frame in item["support_frames"]:
            frame_path = extract_frames(video_path, output_folder, reference_frame)
            print(f"Frame saved to: {frame_path}")