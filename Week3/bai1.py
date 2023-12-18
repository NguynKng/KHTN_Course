def BMI(weight,height):
    bmi = weight/(height**2)
    return bmi

def advise(bmi):
    if bmi < 18:
        print("Gầy, cần bổ sung dinh dưỡng.")
    elif 18 < bmi < 25:
        print("Cân đối, cần duy trì.")
    else:
        print("Béo, cần tập luyện thêm.")

def doi_chieucao(chieu_cao):
    chieu_cao = chieu_cao/100
    return chieu_cao

while True:
    weight = float(input("Nhập cân nặng: "))
    height = float(input("Nhập chiều cao: "))
    if weight > 0 and height > 0:
        break
if height > 3:
    height = doi_chieucao(height)
print("Chỉ số BMI là",BMI(weight,height))
advise(BMI(weight,height))