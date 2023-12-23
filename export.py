import os
from PIL import Image
from moviepy.editor import VideoFileClip
from utils import read_json, write_json

def export_frame(filepath: str, outdir: str, target_fps: int=12) -> None:
    if not os.path.exists(filepath):
        print("File not found!")
        return
    
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    
    clip = VideoFileClip(filepath)
    data_frame_path = os.path.join(outdir, "data.json")
    data_frame = read_json(data_frame_path)

    total_frames = int(clip.fps * clip.duration)
    frames_to_skip = int(clip.fps / target_fps)

    for i, frame in enumerate(clip.iter_frames(fps=clip.fps, dtype='uint8'), start=1):
        if i % frames_to_skip != 0:
            continue
        
        frame_number = i
        frame_time = (frame_number - 1) / clip.fps
        duration_minutes = int(frame_time // 60)
        duration_seconds = int(frame_time % 60)
        duration_ms = int((frame_time % 1) * 1000)
        
        filename = f"frame_{frame_number}_time_{duration_minutes:02d}m{duration_seconds:02d}s{duration_ms:03d}ms.png"
        
        new_dict = {'frame': frame_number, 'path': os.path.join(outdir, filename)}
        data_frame.append(new_dict)
        write_json(data_frame_path, data_frame)
        
        save_image(os.path.join(outdir, filename), frame, frame_number, total_frames, duration_minutes, duration_seconds, duration_ms)

    print("Export selesai.")

def save_image(filepath: str, frame, frame_number: int, total_frames: int, duration_minutes: int, duration_seconds: int, duration_ms: int) -> None:
    Image.fromarray(frame).save(filepath)
    print(f"Saved frame {frame_number}/{total_frames} - Time: {duration_minutes:02d}m{duration_seconds:02d}s{duration_ms:03d}ms - Filename: {filepath}")