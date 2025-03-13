# 實驗一
1. 藉由預先紀錄速度、角度、時間這三項數據，在低速情況下即可將其軌跡繪製出來。
2. 再將繪製出來的曲線平滑化，與原本的曲線相對比，求出兩者的方均根，即可大致評估此控制系統的穩定度
## 記錄程式
```python 
start = 0
def record(velocity,angle):
  loop_time = time.time()
  df = pd.DataFrame({"v":velovity,"a":angle,"t":loop_time-start})
  df.to_csv(path_or_buf='data.csv', header=False, index=False, mode='a')
  start = loop_time  
```
## 數據檔案
```test1/data/XXX.csv```
## 測試程式
```plot.py```
## 實驗結果
.....
