import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def evaluate_model(model, test_gen, test_triples, batch_size):
    # model_name = os.path.basename(model_file)
    # model = load_model(model_file)
    # print("=== Evaluating model: {:s} ===".format(model_name))
    print("=== Evaluating model")
    ytrue, ypred = [], []
    num_test_steps = len(test_triples) // batch_size
    for i in range(num_test_steps):
        # (X1, X2), Y = test_gen.next()
        (X1, X2), Y = next(test_gen)
        Y_ = model.predict([X1, X2])
        ytrue.extend(np.argmax(Y, axis=1).tolist())
        ypred.extend(np.argmax(Y_, axis=1).tolist())
    accuracy = accuracy_score(ytrue, ypred)
    print("\nAccuracy: {:.3f}".format(accuracy))
    print("\nConfusion Matrix")
    print(confusion_matrix(ytrue, ypred))
    print("\nClassification Report")
    print(classification_report(ytrue, ypred))
    return accuracy
