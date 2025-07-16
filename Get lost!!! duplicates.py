student_data={'id1':
              {'Name':['Sara'],
               'Class':['5th'],
               'subject_integration':['english, math, scince']
               },
               'id1':
              {'Name':['David'],
               'Class':['5th'],
               'subject_integration':['english, math, scince']
               },
               'id1':
              {'Name':['Sara'],
               'Class':['5th'],
               'subject_integration':['english, math, scince']
               },
               'id1':
              {'Name':['Surya'],
               'Class':['5th'],
               'subject_integration':['english, math, scince']
              },
               }

result={}

for key, value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)