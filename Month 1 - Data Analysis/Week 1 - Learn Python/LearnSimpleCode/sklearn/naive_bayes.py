
'''
    class : sklearn.naive_bayes.GaussianNB
'''

from sklearn.naive_bayes import GaussianNB

# [height, weight,shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# với mỗi bộ X ở trên gán nhãn cho Y

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

gnb = GaussianNB()

gnb = gnb.fit(X,Y)

prediction = gnb.predict([[190, 70, 43]])

print(prediction)