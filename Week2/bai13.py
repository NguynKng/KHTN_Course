or_lst = [1,5,8,-1,2,6,0,-8,-6,11,19,21,3]
new_list1 = [x+2 for x in or_lst]
new_list2 = [x for x in or_lst if x < 0]
new_list3 = [x if x>0 else 0 for x in or_lst]
print("List mới sau khi mỗi phần tử tăng thêm 2:",new_list1)
print("List sau khi lọc phan tu am:",new_list2)
print("List thay thế các phần tử âm thành số 0:",new_list3)
