# Zalo AI Challenge 2025: Traffic Buddy

## Description

Traffic is a critical issue in today's society. The challenge "RoadBuddy – Understanding the Road through Dashcam AI" aims to build a driving assistant capable of understanding video content from dashcams to quickly answer questions about traffic signs, signals, and driving instructions. This helps enhance safety, ensure legal compliance, and reduce driver distraction. The solution is also useful for post-accident analysis, evidence retrieval, logistics optimization, and enriching map/infrastructure data from common camera sources.

From a research perspective, the challenge creates a Vietnamese benchmark tailored to the traffic context in Vietnam.

Input: 
- A traffic video recorded by a car dashcam mounted on a car, lasting from 5 to 15 seconds in various scenarios such as urban/highway traffic, day/night, rain/sun. It may include traffic signs, signals, lane arrows, road markings, vehicles, etc.
- A user question.

Output: Corresponding answer to the question.

(Knowledge used to answer questions must comply with current Vietnamese road traffic laws.)

## Dataset

• Training data: ~600 videos, ~1000 samples including: questions, videos, answers, support frames 
• Public test: ~300 videos, ~500 samples including: questions, videos
• Private test: ~300 videos, ~500 samples including: questions, videos 

Training dataset including a train.json file and a folder of traffic videos. Each item in the annotations of training data include:

- video_path: the video which is used for the question 
- question: the question
- choices: choices of the questions 
- answer: the correct answer
- support_frames: reference frame in videos at a specific time

```json
{
  "id": "...",
  "question": "Trong video này, vạch kẻ đường dạng chữ viết trên mặt đường có ý nghĩa gì?",
  "choices": [
    "A. Làn đường dành cho xe buýt",
    "B. Làn thu phí không dừng",
    "C. Làn đường dành cho xe tải",
    "D. Khu vực được phép quay đầu xe"
  ],
  "answer": "B. Làn thu phí không dừng",
  "support_frames": [
    5.05
  ],
  "video_path": "....mp4"
}
```

The dataset is available in the [dataset](dataset) directory.

## Rule

- Model size at inference time ≤ 8B parameters. You can use several small models if needed.
- Inference time ≤ 30s/sample.
- The machine for running the Docker of the final solution is configured with 1 GPU (RTX 3090 or NVIDIA A30), CPU: 16 cores, RAM: 64GB, Intel(R) Xeon(R) Gold 6442Y
- No Internet access during inference.
- Open-source data/models allowed.
- Synthetic data generation allowed using services or other models (LLM, VLM, etc.).
- After the competition ends, participants commit not to store any training data for personal purposes.