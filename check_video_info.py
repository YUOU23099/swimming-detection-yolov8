import cv2

def get_video_info(video_path):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"错误：无法打开视频文件 {video_path}")
        return
    
    # 获取视频属性
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0
    
    # 打印视频信息
    print(f"\n视频信息：")
    print(f"分辨率: {width}x{height}")
    print(f"帧率: {fps:.2f} fps")
    print(f"总帧数: {total_frames}")
    print(f"时长: {duration:.2f} 秒 ({duration/60:.2f} 分钟)")
    
    # 释放视频对象
    cap.release()

if __name__ == "__main__":
    video_path = "videos/D04_20250324085959.mp4"
    get_video_info(video_path)