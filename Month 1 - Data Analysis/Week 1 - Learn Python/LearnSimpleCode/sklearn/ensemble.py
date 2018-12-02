
'''
    Ensemble method: phương pháp kết hợp
    class: sklearn.ensemble.ExtraTreeClassifier
    class: sklearn.ensemble.RandomForestClassifier
'''

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

# [height, weight,shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# với mỗi bộ X ở trên gán nhãn cho Y

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


clf = RandomForestClassifier(n_estimators=2)

clf = clf.fit(X,Y)

prection = clf.predict([[190, 70, 43]])

print(prection)

clf2 = ExtraTreesClassifier(n_estimators=2)

clf2 = clf2.fit(X,Y)

prection2 = clf2.predict([[190, 70, 43]])

print(prection2)

