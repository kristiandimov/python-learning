contacts = {
    'number':4,
    'students':[
        {'name':'Kris Dimov','email':'kris4an80@gmail.com'},
        {'name':'Ivan Ivanov','email':'Ivan@gmail.com'},
        {'name':'Megi Dimova','email':'mediD@gmail.com'}
    ]
}

print('Student emails:')
for student in contacts['students']:
   print(student['email']) 