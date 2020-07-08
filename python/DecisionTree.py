import math
import random
from scipy.stats import chi2

# Decision Tree: A simple yet effective method of machine learning that is easy for humans to interpret and is accurate for simple tasks.
# This specific decion tree implements multivalued attributes and classes, k-fold cross-validation, and chi-square pruning.
# k-fold cross-validation is a good way of getting an accurate model that should not overfit as easily, however, larger k values mean longer training.
# k-fold cross-validation:
    # 1. Shuffle and divide the data (training and testing) into k equal partitions.
    # For example, if the data was [1, 2, 3, 4, 5, 6] and k = 3, the partitions could be [1, 3], [2, 6], [4, 5]
    # 2. For each model tested, set aside (k - 1) of the partitions for training and 1 of the paritions for testing.
    # In the example above, Model #n might receive [1, 3] and [2, 6] as training and be tested on [4, 5].
    # 3. Choose the model that minimizes loss/cost values.
# Chi-square pruning:
    # 1. As with all chi-square tests, a null hypothesis (assumption that there is no correlation) is required.
    # 2. Assume the null hypothesis has a probability of occuring of p. This is also known as the confidence interval.
    # 3. Calculate the total deviation from expectation created by adopting a target attribute.
    # 4. If total deviation > chi square statistic: do not choose this attribute.
# Method:
    # 1. Initialize an empty decision tree.
    # 2. Choose the attribute that has the greatest information gain.
    # 3. Split the examples based on that attribute. Add the attribute to the tree.
    # 4. Repeat 2-3 recursively for each set of split examples.

# The entropy (uncertainty) of a random variable that can fall into one of many attributes according to probs.
def entropy(probs):
    x = 0
    for p in probs:
        if p != 0 and p != 1:
            x -= p * math.log(p) / math.log(2)
    return x

# The information gain of a target attribute is the change in entropy from adding a target attribute to the decision tree.
def information_gain(target_attribute, examples, attributes, classes, confidence = 0.05):
    # Find the entropy of the parent set by noting the frequency of each classification and then dividing by the size of the parent set
    class_counts = {c: 0 for c in classes}
    for example in examples: class_counts[example[-1]] += 1
    information_gain = entropy([class_counts[x]/len(examples) for x in class_counts])
    # Find the entropy of splitting the parent set by a certain attribute.
    # Entropy is calculated by summing over the entropies for each possible value of the attribute times the probability that it occurs in the parent set.
    attribute_entropy = 0
    total_deviation = 0
    # There are len(examples) - 1 degrees of freedom.
    chisquare_statistic = chi2.isf(confidence, len(examples) - 1)
    for a in attributes[target_attribute]:
        examples_subset = [e for e in examples if e[target_attribute] == a]
        if len(examples_subset) != 0:
            attribute_class_counts = {c: 0 for c in classes}
            for example in examples_subset: attribute_class_counts[example[-1]] += 1

            # Determine the deviation from expectation.
            observed = [attribute_class_counts[x] for x in attribute_class_counts]
            expected = [class_counts[x] * len(examples_subset) / len(examples) for x in attribute_class_counts]
            deviations = [(observed[i] - expected[i]) ** 2 / expected[i] for i in range(len(observed))]
            total_deviation += sum(deviations)

            attribute_entropy += entropy([attribute_class_counts[x]/len(examples_subset) for x in attribute_class_counts]) * len(examples_subset)/len(examples)
    if total_deviation > chisquare_statistic: return 0
    information_gain -= attribute_entropy
    return information_gain

def DecisionTree(examples, attributes, classes, attribute_names, tree = None, path = []):
    if tree == None: tree = []
    class_counts = {c: 0 for c in classes}
    for example in examples: class_counts[example[-1]] += 1
    if sorted(set([class_counts[k] for k in class_counts])) == [0, len(examples)]:
        tree.append(path + [examples[0][-1],])
        return None
    if len(examples) == 1: return None
    information_gains = [information_gain(a, examples, attributes, classes) for a in attributes]
    best_attribute = list(attributes)[information_gains.index(max(information_gains))]
    new_attributes = attributes.copy()
    del new_attributes[best_attribute]
    for k in attributes[best_attribute]:
        examples_subset = [e for e in examples if e[best_attribute] == k]
        DecisionTree(examples_subset, new_attributes, classes, attribute_names, tree, path + [[best_attribute, k]])
    return tree

def predict(tree, unclassified_data):
    if tree == None: return None
    for possibility in tree:
        decision = possibility[-1]
        criteria = possibility[:-1]
        criteria_met = 0
        for property in criteria:
            if unclassified_data[property[0]] == property[1]: criteria_met += 1
        if criteria_met == len(criteria): return decision
    return None

def accuracy(tree, target_data):
    corrects = 0
    for target in target_data:
        if predict(tree, target) == target[-1]: corrects += 1
    return corrects / len(target_data)

def kfold_partition(data, k):
    if k == 1: return data, []
    shuffled_data = data[::]
    random.shuffle(shuffled_data)
    i = (k - 1) * (len(data) // k)
    training_data, validation_data = shuffled_data[:i], shuffled_data[i:]
    return training_data, validation_data

# All values except the last are attributes, the last is the class value
data = [[0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [1, 1, 1, 1, 0]]
attributes = {0: [0, 1],
              1: [0, 1],
              2: [0, 1],
              3: [0, 1]}
attribute_names = ["a", "b", "c", "d"]
classes = [0, 1]

# Training: k-fold cross-validation with k = 5
best_accuracy = 0
k_max = 5
iterations = 1
best_trees = {}
for iteration in range(iterations):
    for k in range(2, k_max + 1):
        train_data, valid_data = kfold_partition(data, k)
        tree = DecisionTree(train_data, attributes, classes, attribute_names)
        acc = accuracy(tree, valid_data)
        if acc >= best_accuracy:
            best_accuracy = acc
            if acc not in best_trees: best_trees[acc] = []
            best_trees[acc].append(tree)
# Occam's Razor: The hypothesis (in our case model) which makes the least assumptions (in our case, requires the least criteria) is likely the best hypothesis.
best_tree = None
min_tree_length = 1e6
for tree in best_trees[max(best_trees)]:
    if len(tree) < min_tree_length:
        best_tree = tree
        min_tree_length = len(tree)
# Print results:
print("Decision tree that fits the training data: ")
print("-" * 25)
for possibility in best_tree:
    decision = possibility[-1]
    criteria = possibility[:-1]
    criteria_met = 0
    s = "If "
    for property in criteria: s += attribute_names[property[0]] + " = " + str(property[1]) + ", "
    print(s + "then the data belongs to class " + str(classes[decision]))
print("-" * 25)
print("The accuracy of the decision tree is %.2f%% during validation." % (100 * best_accuracy))
