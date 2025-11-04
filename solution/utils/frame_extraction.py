import cv2
import os
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

SAVE_DIR = "solution/dataset/frame_extraction"
os.makedirs(SAVE_DIR, exist_ok=True)

def frame_extraction(video_path, reference_frames):
    print(f"Extracting frames for {video_path} with reference frames {reference_frames}")
    cap = cv2.VideoCapture(video_path)

    video_fps = cap.get(cv2.CAP_PROP_FPS)

    for target_frame in reference_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame * video_fps)
        ret, frame = cap.read()
        cv2.imwrite(f"{SAVE_DIR}/{video_path.split('/')[-1].replace('.mp4', f'_{target_frame}.jpg')}", frame)
    
    cap.release()

if __name__ == "__main__":
    input_dir = "dataset/train/videos"
    json_file = "dataset/train/train.json"

    if not os.path.exists(input_dir):
        print(f"Input directory {input_dir} does not exist")
        exit(1)

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)["data"]

    video_path_to_support_frames = {}
    for item in data:
        video_path = os.path.join("dataset", item["video_path"])
        if video_path not in video_path_to_support_frames:
            video_path_to_support_frames[video_path] = []
        video_path_to_support_frames[video_path].extend(item["support_frames"])
        video_path_to_support_frames[video_path] = sorted(list(set(video_path_to_support_frames[video_path])))

    tasks = []
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as executor:
        for video_path, support_frames in video_path_to_support_frames.items():
            tasks.append(executor.submit(frame_extraction, video_path, support_frames))

        for future in as_completed(tasks):
            pass

    print("Frame extraction complete")
