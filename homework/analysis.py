# ============================================================
#   第一步：统计每个球队、每个球员每场比赛的平均得分
#   第二步：在第一步基础上，统计每个球队的平均得分
# 表格中的变量：
# attempt：只有2/3分，没有罚球，outcome->made得分 missed失误
# ============================================================

import csv
from collections import defaultdict

FILE = "/home/vect/Python/homework/shots-2023.csv"

# 读数据
rows = []
with open(FILE, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# 算每条记录的得分
#   made + 3-pointer  → 3 分
#   made + 2-pointer  → 2 分
#   missed            → 0 分

def calc_points(row):
    # 没命中，直接pass
    if row["outcome"].strip().lower() != "made":
        return 0
    
    # 命中了，再判断是几分
    attempt = row["attempt"].strip().lower()
    if "3-pointer" in attempt:
        return 3
    else:  
        return 2

# 给每一行添加 points 列
for row in rows:
    row["points"] = calc_points(row)

# 把同一球员同一场的所有投篮得分加起来
# 例如：湖人的勒布朗在game1的所有投篮得分加起来

# 用 defaultdict 存：(球队, 球员, 场次) → 总得分
game_pts = defaultdict(int)

for row in rows:
    # 三位数组，元素是哈希表
    team = row["team"].strip()
    player = row["shots_by"].strip()
    game_id = row["game_id"].strip()
    key = (team, player, game_id)
    
    # 累加得分
    game_pts[key] += row["points"]

# 把同一球员在同一球队的所有场次的得分平均
# 例如：湖人的勒布朗出10场，总得分250，场均25

# 用两个 defaultdict 分别存：总得分和场次
player_total = defaultdict(int)    # (球队, 球员) → 总得分
player_games = defaultdict(int)    # (球队, 球员) → 场次

# 遍历第 2 步的结果
for (team, player, game_id), pts in game_pts.items():
    # 累加总得分
    player_total[(team, player)] += pts
    # 累加场次
    player_games[(team, player)] += 1


# 构建第一步的结果列表
step1 = []

for (team, player), total in player_total.items():
    # 获取场次
    games = player_games[(team, player)]
    
    # 场均得分
    avg = round(total / games, 2)
    
    # 哈希表，存储一个球员的统计数据
    record = {
        "team": team,
        "player": player,
        "games": games,
        "total_pts": total,
        "avg_pts_per_game": avg
    }
    step1.append(record)

# 排序第一步的结果
# 先按球队升序，再按场均得分降序
step1.sort(key=lambda x: (x["team"], -x["avg_pts_per_game"]))

# 计算每球队的平均得分
# 在第一步的基础上，把同一球队所有球员的场均得分再平均一次
# 用两个 defaultdict 分别存：总得分和球员数
team_sum = defaultdict(float)    # 球队 → 所有球员场均得分的总和
team_count = defaultdict(int)      # 球队 → 球员数

# 遍历第一步的结果
for r in step1:
    team = r["team"]
    avg = r["avg_pts_per_game"]
    
    # 累加该球队所有球员的场均得分
    team_sum[team] += avg
    # 累加该球队的球员数
    team_count[team] += 1

# 构建第二步的结果列表
step2 = []

for team, total in team_sum.items():
    count = team_count[team]
    avg = round(total / count, 2)
    record = {
        "team": team,
        "player_count": count,
        "team_avg_pts": avg
    }
    step2.append(record)

# 排序第二步的结果
# 按球队平均得分降序排列
step2.sort(key=lambda x: -x["team_avg_pts"])

# 导出结果
OUT1 = "/home/vect/Python/homework/player_avg.csv"
OUT2 = "/home/vect/Python/homework/team_avg.csv"

with open(OUT1, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["team", "player", "games", "total_pts", "avg_pts_per_game"])
    writer.writeheader()  
    writer.writerows(step1) 

with open(OUT2, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["team", "player_count", "team_avg_pts"])
    writer.writeheader() 
    writer.writerows(step2)  

