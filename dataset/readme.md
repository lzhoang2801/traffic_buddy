# TrafficBuddy Dataset Structure
```
TrafficBuddyHZUTAXF/
├── public_test/
│   ├── public_test.json
│   └── videos/
│       ├── video_1.mp4
│       ├── video_2.mp4
│       └── ...
├── train/
│   ├── train.json
│   └── videos/
│       ├── video_1.mp4
│       ├── video_2.mp4
│       └── ...
├── download_videos.py
└── readme.txt
```
## Downloading Videos
Due to the large size of the video files, they are not included directly in the dataset. Instead, you can download them using the provided URLs.


Each video referenced in `public_test.json` and `train.json` can be accessed using the following URL pattern:
```
https://dl-challenge.zalo.ai/2025/TrafficBuddyHZUTAXF/<video_path>
```

Where `<video_path>` corresponds to the `video_path` field in the JSON files.

### Using the Download Script

A convenience script `download_videos.py` is provided to download all videos automatically:
```bash
# Modify the paths to public_test.json and train.json in the script if needed
python download_videos.py
```

Your solution should use videos stored on disk, not access them directly from the URL.