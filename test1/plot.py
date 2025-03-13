import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def calculate_rmsd(x_values, y_values, smoothed_x_values, smoothed_y_values):
    dx = x_values - smoothed_x_values
    dy = y_values - smoothed_y_values
    rmsd = np.sqrt(np.mean(dx**2 + dy**2))
    return rmsd

def smooth_trajectory(x_values, y_values, window_size):
    smoothed_x_values = np.convolve(x_values, np.ones(window_size)/window_size, mode='valid')
    smoothed_y_values = np.convolve(y_values, np.ones(window_size)/window_size, mode='valid')
    return smoothed_x_values, smoothed_y_values


def plot_vehicle_trajectory(speeds, angles, timestamp):
    x = 0.0
    y = 0.0
    heading = -0.0

    x_values = [x]
    y_values = [y]

    for speed, angle, dt in zip(speeds, angles, timestamp):
        distance = speed * dt
        x += distance * np.cos(heading)
        y += distance * np.sin(heading)
        heading += np.radians(-angle-0.02)

        x_values.append(x)
        y_values.append(y)

    window_size = 5  # 調整平滑窗口大小
    smoothed_x_values, smoothed_y_values = smooth_trajectory(x_values, y_values, window_size)
    
    rmsd = calculate_rmsd(x_values[:len(smoothed_x_values)], y_values[:len(smoothed_y_values)], smoothed_x_values, smoothed_y_values)

    print("均方根差異為" + str(rmsd))
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, marker='o', )
    plt.plot(smoothed_x_values, smoothed_y_values, color='red')
    plt.title('Vehicle Trajectory')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# 讀取CSV檔案
csv_file = 'data/data.csv'  # 將 'data/data.csv' 替換為實際的檔案路徑
data = pd.read_csv(csv_file)

# 從CSV檔案中獲取速度、角度和時間數據
speeds = data['v'].values
angles = data['a'].values
timestamp = data['t'].values

# 呼叫函式繪製軌跡
plot_vehicle_trajectory(speeds, angles, timestamp)
