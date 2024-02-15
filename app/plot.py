
import matplotlib.pyplot as plt


x = ["0", "10k", "20k", "30k", "40k", "50k"]
y_fid = []
y_precision = []
y_recall = []


# サブプロットを一括で作成
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# FIDをプロット
axs[0].plot(x, y_fid, 'b-')
axs[0].set_yticks([23.0, 24.0, 25.0, 26.0, 27.0])
axs[0].set_xlabel('Training Steps')
axs[0].set_ylabel('FID')

# Precisionをプロット
axs[1].plot(x, y_precision, 'g-')
axs[1].set_yticks([0.50, 0.52, 0.54, 0.56, 0.58])
axs[1].set_xlabel('Training Steps')
axs[1].set_ylabel('Precision')

# Recallをプロット
axs[2].plot(x, y_recall, 'r-')
axs[2].set_yticks([0.26, 0.28, 0.30, 0.32, 0.34])
axs[2].set_xlabel('Training Steps')
axs[2].set_ylabel('Recall')

# グラフの表示
plt.tight_layout()
plt.show()

# 保存
plt.savefig("metrics.pdf")
# xlabel = "epochs"
# ylabel = "loss"
# loc = "lower right"

# plt.plot(x, loss["train_losses"], label="train_loss")
# plt.plot(x, loss["val_losses"], label="val_loss")
# plt.xticks(xticks)
# plt.yticks(yticks)
# plt.xlabel(xlabel)
# plt.ylabel(ylabel)
# plt.legend(loc=loc)
# plt.show()
# plt.savefig(os.path.join(out_dir, f"{exp_name}.png"))
# plt.clf()
