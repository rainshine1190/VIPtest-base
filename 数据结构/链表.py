"""
功能描述：
编写人：liangchao
编写日期：
实现逻辑：
创建链表
插入链表（头插法，尾插法）


"""


class Node():

    def __init__(self,item):
        self.item = item
        self.next = None

def create_linklist(li):
    """
    头插法创建链表
    :param li:
    :return:
    """
    #创建一个头节点
    head = Node(li[0])
    # 遍历剩余元素
    for i in li[1:]:
        # 创建一个新节点
        node = Node(i)
        # 新节点的next指向原来的head
        node.next = head
        # 新节点赋给head
        head = node
    return head

def print_linklist(lk):
    """
    遍历链表
    :param lk:
    :return:
    """
    while lk:
        # 打印链表的内容
        print(lk.item,end='\t')
        # 指向下一个链表
        lk = lk.next

lk = create_linklist([1, 2, 3, 4])
print(lk.next.item)
print_linklist(lk)