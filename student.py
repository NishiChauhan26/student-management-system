class Student:
    def __init__(self, roll_no, name, age, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
    
    def display(self):
        print(f"Roll No: {self.roll_no} | Name: {self.name} | Age: {self.age} | Course: {self.course} | Marks: {self.marks}")

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }
    @staticmethod
    def from_dict(data):
        return Student(data["roll_no"], data["name"], data["age"], data["course"], data["marks"])


if __name__ == "__main__":  
    s1 = Student(101, "Harry", 20, "Python Development", 88)
    s1.display()