students = {
    "Alice": ["ID001", 26, "A"],
    "Bob":["ID002", 27, "B"], 
    "Claire": ["ID003", 17, "C"], 
    "Dan": ["ID004", 21, "D"], 
    "Emma": ["ID005", 22, "F"]
    }

print(students["Claire"][0])
print(students["Dan"][1:])

students_new = {
    "Alice": {"id": "ID001", "age": 26, "grade": "A"},
    "Bob": {"id": "ID002", "age": 27, "grade": "B"},
    "Claire": {"id": "ID003", "age": 17, "grade": "C"},
    "Dan": {"id": "ID004", "age": 21, "grade": "D"},
    "Emma": {"id": "ID005", "age": 22, "grade": "F"},
}

print(students_new["Dan"]["age"])

print(students_new["Emma"]["id"], students_new["Emma"]["grade"])