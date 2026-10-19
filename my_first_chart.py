import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"

hours = [2, 3, 1, 4, 3, 5, 4]

fig, ax = plt.subplots(figsize=(7, 4))

ax.plot(hours, marker="o")

for i, h in enumerate(hours):
    ax.annotate(
        f"{h}시간",
        (i, h),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center"
    )

ax.set_title("일주일간 공부시간 변화")

fig.savefig("my_first_chart.png", bbox_inches="tight")