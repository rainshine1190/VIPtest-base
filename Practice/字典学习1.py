#coding:utf-8

# def sortedDictValues1(adict):
#     items = adict.items()
#     print("items:", items)
#     list(items).sort()
#     return [value for key, value in items]
#
#
# adict = {"a1": 11, "b1": 2, "c1": 30, "e1": 20, "d1": 4}
# print(sortedDictValues1(adict))
# # items: [('a1', 11), ('c1', 30), ('e1', 20), ('b1', 2), ('d1', 4)]
# # [11, 2, 30, 4, 20]


def sortedDictValues2(adict):
    keys = list(adict.keys())

    print('keys',keys)
    keys.sort()
    return [dict[key] for key in keys]


adict = {"a1": 11, "b1": 2, "c1": 30, "e1": 20, "d1": 4}
print(sortedDictValues2(adict))