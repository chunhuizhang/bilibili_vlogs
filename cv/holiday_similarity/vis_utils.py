import matplotlib.pyplot as plt


def plot_training_curve(history):
    # print(history.history.keys())
    plt.subplot(211)
    plt.title("Loss")
    plt.plot(history.history["loss"], color="r", label="train")
    plt.plot(history.history["val_loss"], color="b", label="validation")
    plt.legend(loc="best")

    plt.subplot(212)
    plt.title("Accuracy")
    plt.plot(history.history["accuracy"], color="r", label="train")
    plt.plot(history.history["val_accuracy"], color="b", label="validation")
    plt.legend(loc="best")

    plt.tight_layout()
    plt.show()
