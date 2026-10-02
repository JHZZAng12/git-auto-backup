students= [
    {"name":"insung","korean":87,"math":98,"english":88,"science":95},
    {"name":"hajin","korean":92,"math":98,"english":96,"science":98},
    {"name":"jiyeoun","korean":76,"math":96,"english":94,"science":90},
    {"name":"sunju","korean":98,"math":92,"english":96,"science":92},
    {"name":"arin","korean":95,"math":98,"english":98,"science":98},
    {"name":"myoungwall","korean":64,"math":88,"english":92,"science":92}
]

print("name","total score","average",sep="\t")

for student in students:

    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep="\t")
