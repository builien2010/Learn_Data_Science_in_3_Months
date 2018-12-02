
'''
    Decision Tree Classifier : Phân loại cây quyết định
    class: sklearn.tree.DecisionTreeClassifier
'''


from sklearn import tree

# from sklearn.tree import DecisionTreeClassifier

# initialize
clf = tree.DecisionTreeClassifier()


# [height, weight,shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# với mỗi bộ X ở trên gán nhãn cho Y

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# .fit(X,Y) method: build a decision tree classifier from the training set (X,Y) --> return object
clf = clf.fit(X,Y)

#.predict(X) : return predicted class or predict values (regression)
prediction = clf.predict([[190,70,43]])

print(prediction)
