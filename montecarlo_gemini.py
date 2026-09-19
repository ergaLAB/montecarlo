import random
import numpy as np
import matplotlib.pyplot as plt

# 試行回数の入力
n = int(input("繰り返す回数を入力してください（整数値のみ）："))

# -1〜1の範囲でランダムなx, y座標を生成
x = np.random.uniform(-1, 1, n)
y = np.random.uniform(-1, 1, n)

# 原点からの距離（ノルム）を計算
distances = np.hypot(x, y)

# 円の内部にある点と外部にある点を判定
inside = distances <= 1
c = np.sum(inside)  # 円の内部にある点の数

# 円周率の近似計算
pi = (c / n) * 4
print(f"計算完了 π: {pi} (n={n})")

# グラフ描画
plt.figure(figsize=(8, 8))
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# 円の描画
theta = np.linspace(0, 2 * np.pi, 200)
circle_x = np.sin(theta)
circle_y = np.cos(theta)
plt.plot(circle_x, circle_y, color='black')

# 軸の設定
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')

# 枠線の描画
plt.axvline(x=1, color='gray', linestyle='--')
plt.axvline(x=-1, color='gray', linestyle='--')
plt.axhline(y=1, color='gray', linestyle='--')
plt.axhline(y=-1, color='gray', linestyle='--')

# 点のプロット（内部：赤、外部：青）
plt.scatter(x[inside], y[inside], color='red', s=5, alpha=0.6, label='Inside')
plt.scatter(x[~inside], y[~inside], color='blue', s=5, alpha=0.6, label='Outside')

plt.title(f'π: {pi} (n={n})')
plt.legend(loc='upper right')
plt.show()