students = [
    {"id": 1,"name": "Lam", "toan": 6, "van": 7, "hoa": 10},
    {"id": 2,"name": "Hieu", "toan": 7, "van": 9, "hoa": 9},
    {"id": 3,"name": "Hung", "toan": 8, "van": 5, "hoa": 1},
    {"id": 4,"name": "Truc", "toan": 9, "van": 7, "hoa": 4},
    {"id": 5,"name": "Duong", "toan": 10, "van": 10, "hoa": 10},
]
for student in students:
    student["average"] = (student["toan"] + student["van"] + student["hoa"]) / 3
    
print("Sinh vien co diem trung binh 5:")
for student in students:
    if student["average"] > 5: print(student["name"], student["average"])
    
print("")

print("Sinh vien co diem hoa duoi 5:")
for student in students:
    if student["hoa"] < 5: print(student["name"], student["hoa"])