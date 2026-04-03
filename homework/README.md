# analysis.py 简要说明

## 一、程序分为哪些代码块（及目的）

1. **导入模块 + 定义文件路径**
   - 目的：准备读写 CSV 和统计需要的工具 
   - 代码：`import csv`、`from collections import defaultdict`、`FILE = ...`

2. **读取原始数据**
   - 目的：把 `shots-2023.csv` 读入 `rows` 列表 
   - 代码：`open()` + `csv.DictReader()` + `for row in reader`

3. **定义得分函数 `calc_points(row)`**
   - 目的：把每条投篮记录转换为分值 
   - 规则：`missed=0`，`made且3-pointer=3`，其余命中=2，**没有罚球**

4. **给每条记录添加 `points`**
   - 目的：为后续统计准备统一得分字段 
   - 代码：`row["points"] = calc_points(row)`

5. **按 `(team, player, game_id)` 累加总分**
   - 目的：得到某球员某场比赛总得分
   - 结构：`game_pts = defaultdict(int)`

6. **按 `(team, player)` 统计总分与场次**
   - 目的：计算球员场均得分 
   - 结构：`player_total`（总分）、`player_games`（场次）

7. **生成第一步结果 `step1`**
   - 目的：输出每球队-每球员场均得分表 
   - 字段：`team/player/games/total_pts/avg_pts_per_game`
   - 排序：球队升序 + 场均降序 

8. **生成第二步结果 `step2`**
   - 目的：在 `step1` 基础上得到每球队平均得分 
   - 结构：`team_sum`（球队内场均和）、`team_count`（球队球员数）
   - 排序：`team_avg_pts` 降序 

9. **导出 CSV 结果**
   - 目的：保存可在 Excel 打开的结果文件
   - 文件：`step1_player_avg.csv`、`step2_team_avg.csv`

---

## 二、主要函数/方法

- **文件与CSV**
  - `open()`：打开文件
  - `csv.DictReader()`：读 CSV 为哈希表行
  - `csv.DictWriter()`：写回 CSV
  - `writeheader()` / `writerows()`：写表头 / 写数据

- **统计结构**
  - `defaultdict(int)`：默认 0，便于累加
  - `defaultdict(float)`：默认 0.0，便于累计平均值

- **字符串处理**
  - `strip()`：去首尾空格
  - `lower()`：统一小写
  - `in`：判断是否包含 `3-pointer`

- **计算与排序**
  - `round(x, 2)`：保留 2 位小数
  - `sort(key=lambda ...)`：按规则排序
  - `items()`：遍哈希表值对
  - `append()`：结尾追加

---

## 三、输出结果

- `player_avg.csv`：每球队、每球员每场平均得分
- `team_avg.csv`：每球队平均得分
