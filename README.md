# 游泳检测项目 (Swimming Detection Project)

基于 YOLOv8 的实时游泳者检测系统，用于视频中的游泳者识别和跟踪。

## 功能特点

- 使用 YOLOv8 进行实时游泳者检测
- 支持视频文件处理
- 可调整检测分辨率
- 实时显示检测结果和置信度
- 支持结果视频保存

## 环境要求

- Python 3.8+
- ultralytics
- OpenCV (opencv-python)
- PyTorch

## 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/YUOU23099/swimming-detection-yolov8.git
cd swimming-detection-yolov8
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 准备模型文件（best3.pt）和视频文件

2. 运行检测：
```bash
python test_video.py
```

## 项目结构

```
swimming-detection-yolov8/
├── test_video.py          # 主要的视频检测脚本
├── check_video_info.py    # 视频信息查看工具
├── requirements.txt       # 项目依赖
└── videos/               # 视频文件目录
```

## 配置说明

在 `test_video.py` 中可以调整以下参数：
- `conf`：检测置信度阈值（默认0.25）
- `imgsz`：处理分辨率（默认640x640）
- `show`：是否显示实时检测结果
- `save`：是否保存结果视频

## 注意事项

- 模型文件 (best3.pt) 需要放在项目根目录
- 视频文件建议放在 videos 目录下
- 检测结果会保存在 runs/detect/predict 目录下