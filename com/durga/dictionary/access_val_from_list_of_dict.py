students = [
    {"name": "John Doe",
     "father name": "Robert Doe",
     "Address": "123 Hall street"
     },
    {
        "name": "Rahul Garg",
        "father name": "Kamal Garg",
        "Address": "3-Upper-Street corner"
    },
    {
        "name": "Angela Steven",
        "father name": "Jabob steven",
        "Address": "Unknown"
    }
]
print(list(map(lambda student: student['Address'], students)))

