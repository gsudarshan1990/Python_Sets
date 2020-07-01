class student2:
    total_student=0
    def __init__(self, name, age,favorite_subject):
        self.name = name
        self.age = age
        self.favorite_subject = favorite_subject
        student2.total_student+=1

    def __len__(self):
        return student2.total_student

s1=student2("rahul",20,"physics")
s2=student2("sonu",21,"chemistry")
s3=student2("deepu",27,"social")


print("total students",len(s3))

