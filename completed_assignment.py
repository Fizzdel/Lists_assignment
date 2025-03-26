submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

student=input('enter name here: ',)
completion= student in submitted
attendance= student in attended

print(completion and attendance)
if completion and attendance:
    print('Was here and Submitted the assignment')
elif attendance and not completion:
    print('Was here but work has not yet been submitted')
elif completion and not attendance:
    print('Submitted work but did not attend')
else:
    print('Not on list')