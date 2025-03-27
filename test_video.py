from ultralytics import YOLO
import cv2
import os

def process_video(model_path, video_path, conf=0.25):
    # 加载模型
    print(f"正在加载模型 {model_path}...")
    model = YOLO(model_path)
    
    # 设置正确的类别名称
    model.names[0] = "swimming"  # 将默认的"0"改为"swimming"
    
    # 检查视频文件是否存在
    if not os.path.exists(video_path):
        print(f"错误：找不到视频文件 {video_path}")
        return
        
    print(f"开始处理视频 {video_path}")
    print(f"检测类别: {model.names}")
    print(f"原始视频分辨率: 1280x720")
    print(f"处理分辨率: 640x640")
    
    # 运行预测
    # save=True 会自动保存带有检测框的视频
    # conf 是置信度阈值
    # show=True 会实时显示处理过程
    results = model.predict(
        source=video_path,
        conf=conf,
        save=True,
        show=True,
        stream=True,  # 使用流式处理以节省内存
        imgsz=640    # 设置处理分辨率为 640x640
    )
    
    # 处理结果
    for r in results:
        # 获取当前帧的检测数量
        num_detections = len(r.boxes)
        if num_detections > 0:
            print(f"当前帧检测到 {num_detections} 个目标，置信度：", end=" ")
            for box in r.boxes:
                print(f"{box.conf.item():.2f}", end=" ")
            print()
    
    print("\n处理完成！")
    print("结果保存在 runs/detect/predict 目录下")

if __name__ == "__main__":
    # 设置模型和视频路径
    model_path = "best3.pt"  # 使用新的模型
    video_path = "videos/D04_20250324085959.mp4"  # 视频文件路径
    
    # 运行检测
    process_video(model_path, video_path)