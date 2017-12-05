import vector

#test1
# v1 = Vector([8.218,-9.341])
# v2 = Vector([-1.129,2.111])
# v3 = Vector([7.119,8.215])
# v4 = Vector([-8.223,0.878])
# v5 = Vector([1.671,-1.012,-0.318])

# print "test 1 result:"
# print v1.plus(v2)
# print v3.minus(v4)
# print v5.multiply(7.41)

#test2
# v6 = Vector([-0.221,7.437])
# v7 = Vector([8.813,-1.331,-6.247])
# v8 = Vector([5.581,-2.136])
# v9 = Vector([1.996,3.108,-4.554])

# print "test 2 result:"
# print v6.magnitude()
# print v7.magnitude()
# print v8.direction()
# print v9.direction()

#test3
print "test 3 results:"
v10 = Vector([7.887,4.138])
v11 = Vector([-8.802,6.776])
v12 = Vector([-5.955,-4.904,-1.874])
v13 = Vector([-4.496,-8.755,7.103])

v14 = Vector([3.183,-7.627])
v15 = Vector([-2.668,5.319])
v16 = Vector([7.35,0.221,5.188])
v17 = Vector([2.751,8.259,3.985])

print v10.dot(v11)
print v12.dot(v13)
print v14.angle(v15)
print v16.angle(v17,in_degrees=True)

#test4
print "test 4 results:"
v18 = Vector([-7.579,-7.88])
v19 = Vector([22.737,23.64])
v20 = Vector([-2.029,9.97,4.172])
v21 = Vector([-9.231,-6.639,-7.245])

v22 = Vector([-2.328,-7.284,-1.214])
v23 = Vector([-1.821,1.072,-2.94])
v24 = Vector([2.118,4.827])
v25 = Vector([0,0])

print v18.isParalleOrOrthogonality(v19)
print v20.isParalleOrOrthogonality(v21)
print v22.isParalleOrOrthogonality(v23)
print v24.isParalleOrOrthogonality(v25)

#test5
v1 = Vector([3.039,1.879])
v2 = Vector([0.825,2.036])
v3 = Vector([-9.88,-3.264,-8.159])
v4 = Vector([-2.155,-9.353,-9.473])
v5 = Vector([3.009,-6.172,3.692,-2.51])
v6 = Vector([6.404,-9.144,2.759,8.718])

print v1.paralle_to(v2)
print v3.orthogonal_to(v4)
print v5.paralle_to(v6)
print v5.orthogonal_to(v6)

#test6
v1 = Vector([8.462,7.893,-8.187])
v2 = Vector([6.984,-5.975,4.778])
v3 = Vector([-8.987,-9.838,5.031])
v4 = Vector([-4.268,-1.861,-8.866])
v5 = Vector([1.5,9.547,3.691])
v6 = Vector([-6.007,0.124,5.772])

print v1.cross_product(v2)       
print v3.cross_product(v4).length()
print v5.cross_product(v6).length()/2