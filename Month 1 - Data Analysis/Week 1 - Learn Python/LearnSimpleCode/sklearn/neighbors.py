
'''
    Nearest Neighbors Classifier: Phân loại hàng xóm gần nhất
    class: sklearn.neighbors.KNeighborsClassifier : learning based on the k nearest neighbors of each query point
        
'''

from sklearn.neighbors import KNeighborsClassifier

# [height, weight,shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# với mỗi bộ X ở trên gán nhãn cho Y

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf1 = KNeighborsClassifier( n_neighbors=4)

clf1 = clf1.fit(X,Y)

prection1 = clf1.predict([[190, 70, 43]])

print(prection1)


clf2 = KNeighborsClassifier( n_neighbors=3)

clf2 = clf2.fit(X,Y)

prection2 = clf2.predict([[190, 70, 43]])

print(prection2)

# Nếu chọn k khác nhau thì kết quả khác nhau ?