
array_index = [[],[]]

print("Dimensions = " + str(len(array_index)))
print("Dimensions = " + str(len(array_index[0])))
print("Dimensions = " + str(len(array_index[1])))
print("")
array_index[0].append("Allo 1")
array_index[0].append("Allo 2")

array_index[1].append("Allo 3")
array_index[1].append("Allo 4")
print("Dimensions = " + str(len(array_index)))
print("Dimensions = " + str(len(array_index[0])))
print("Dimensions = " + str(len(array_index[1])))
print("")

array_index.append([])
array_index.append([])
array_index[2].append("Allo 5")
array_index[3].append("Allo 6")
print("Dimensions = " + str(len(array_index)))
print("Dimensions = " + str(len(array_index[0])))
print("Dimensions = " + str(len(array_index[1])))

myIndex = array_index[1].index("Allo 3")
print("Dimensions last = " + str(len(array_index)))

print("Index of Allo 1 = " + str(myIndex))









