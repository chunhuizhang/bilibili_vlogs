from sklearn.externals import joblib
import itertools
import os

import numpy as np
from sklearn import model_selection
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import KFold

DATA_DIR = './data'
IMAGE_DIR = '/Users/chunhuizhang/workspaces/00_datasets/images/INRIA Holidays dataset /jpg'


def get_holiday_triples(image_dir):
    image_groups = {}
    for image_name in os.listdir(image_dir):
        base_name = image_name[0:-4]
        group_name = base_name[0:4]
        if group_name in image_groups:
            image_groups[group_name].append(image_name)
        else:
            image_groups[group_name] = [image_name]
    num_sims = 0
    image_triples = []
    group_list = sorted(list(image_groups.keys()))
    for i, g in enumerate(group_list):
        if num_sims % 100 == 0:
            print("Generated {:d} pos + {:d} neg = {:d} total image triples"
                  .format(num_sims, num_sims, 2 * num_sims))
        images_in_group = image_groups[g]
        sim_pairs_it = itertools.combinations(images_in_group, 2)
        # for each similar pair, generate a corresponding different pair
        for ref_image, sim_image in sim_pairs_it:
            image_triples.append((ref_image, sim_image, 1))
            num_sims += 1
            while True:
                j = np.random.randint(low=0, high=len(group_list), size=1)[0]
                if j != i:
                    break
            dif_image_candidates = image_groups[group_list[j]]
            k = np.random.randint(low=0, high=len(dif_image_candidates), size=1)[0]
            dif_image = dif_image_candidates[k]
            image_triples.append((ref_image, dif_image, 0))
    print("Generated {:d} pos + {:d} neg = {:d} total image triples"
          .format(num_sims, num_sims, 2 * num_sims))
    return image_triples


def load_vectors(vector_file):
    vec_dict = {}
    fvec = open(vector_file, "r")
    for line in fvec:
        image_name, image_vec = line.strip().split("\t")
        vec = np.array([float(v) for v in image_vec.split(",")])
        vec_dict[image_name] = vec
    fvec.close()
    return vec_dict


def preprocess_data(vector_file, train_size=0.7):
    xdata, ydata = [], []
    vec_dict = load_vectors(vector_file)
    for image_triple in image_triples:
        X1 = vec_dict[image_triple[0]]
        X2 = vec_dict[image_triple[1]]
        # xdata.append(np.multiply(X1, X2) / (np.linalg.norm(X1, 2) * np.linalg.norm(X2, 2)))
        # xdata.append(np.power(np.subtract(X1, X2), 2))
        xdata.append(np.abs(np.subtract(X1, X2)))
        ydata.append(image_triple[2])
    X, y = np.array(xdata), np.array(ydata)
    Xtrain, Xtest, ytrain, ytest = model_selection.train_test_split(X, y, train_size=train_size)
    return Xtrain, Xtest, ytrain, ytest


def cross_validate(X, y, clf, k=10):
    best_score, best_clf = 0.0, None
    kfold = KFold(k)
    for kid, (train, test) in enumerate(kfold.split(X, y)):
        Xtrain, Xtest, ytrain, ytest = X[train], X[test], y[train], y[test]
        clf.fit(Xtrain, ytrain)
        ytest_ = clf.predict(Xtest)
        score = accuracy_score(ytest_, ytest)
        print("fold {:d}, score: {:.3f}".format(kid, score))
        if score > best_score:
            best_score = score
            best_clf = clf
    return best_clf, best_score


def test_report(clf, Xtest, ytest):
    ytest_ = clf.predict(Xtest)
    print("\nAccuracy Score: {:.3f}".format(accuracy_score(ytest_, ytest)))
    print("\nConfusion Matrix")
    print(confusion_matrix(ytest_, ytest))
    print("\nClassification Report")
    print(classification_report(ytest_, ytest))


# def get_model_file(data_dir, vec_name, clf_name):
#     return os.path.join(data_dir, "models", "{:s}-{:s}-dot.pkl"
#                         .format(vec_name, clf_name))

def get_model_file(data_dir, vector_name, merge_mode, borf):
    return os.path.join(data_dir, "models", "{:s}-{:s}-{:s}.h5"
                        .format(vector_name, merge_mode, borf))


def save_model(model, model_file):
    joblib.dump(model, model_file)

# image_triples = get_holiday_triples(IMAGE_DIR)
#
# NUM_VECTORIZERS = 5
# NUM_CLASSIFIERS = 4
# scores = np.zeros((NUM_VECTORIZERS, NUM_CLASSIFIERS))
#
# VECTOR_FILE = os.path.join(DATA_DIR, "vgg19-vectors.tsv")
# Xtrain, Xtest, ytrain, ytest = preprocess_data(VECTOR_FILE)
# print(Xtrain.shape, Xtest.shape, ytrain.shape, ytest.shape)
# clf = XGBClassifier()
# best_clf, best_score = cross_validate(Xtrain, ytrain, clf)
# scores[0, 2] = best_score
# test_report(best_clf, Xtest, ytest)
# save_model(best_clf, get_model_file(DATA_DIR, "vgg19", "xgb"))
