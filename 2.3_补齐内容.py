
department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

line1 = "department1 name: %s  Manager:%s  COURSE FEES:%.2f THE END" % (department1, depart1_m, COURSE_FEES_SEC)
line2 = "department2 name: {:<8s}  Manager:{:<7s}  COURSE FEES:{:<9s} THE END".format(
    department2, depart2_m, str(round(COURSE_FEES_Python,2)))

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
