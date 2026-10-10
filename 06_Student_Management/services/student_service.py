

def save_student(student):
    with open("data/students.txt", "a") as file:
        file.write(
            f"{student.student_id},{student.name},{student.age},{student.email}\n"
        )



def get_all_students():
        with open("data/students.txt","r") as file:
            students = file.readlines()
            return students



def search_studentid(student_id):
     with open("data/students.txt","r") as file:
        students=file.readlines()
          
        for student in students:
               data = student.strip().split(",")

               if data[0]== str(student_id):
                    return student.strip()
               



        return "student not found"


def delete_student(student_id):
     with open("data/students.txt","r") as file:
          students = file.readlines()   

     with open("data/students.txt","w") as file:
          found = False


          for student in students:
               data = student.strip().split(",")


               if data[0] != str(student_id):
                    file.write(student)
               else:
                    found = True


     return found       


def update_student(student_id,name,age,email):
     with open("data/students.txt","r") as file:
          students = file.readlines()

     found = False

     with open("data/students.txt","w") as file:
          



          for student in students:
           data = student.strip().split(",")

           if data[0] == str(student_id):
               file.write(f"{student_id},{name},{age},{email}\n")
               found = True
           else:
               file.write(student)




     return found



      
