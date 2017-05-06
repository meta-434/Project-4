import csv

print ('Welcome to the CS 1064 Grade Report program!')
csv_file = input('Enter the grades file: ')


f = open(csv_file, "r")
r = csv.reader(f)

cont = 'Y'

#get just the first row:
assignments = next(r, [])
assignments = assignments[2:]
#get just second row:
weights = next(r, [])
weights = weights[2:]

#rest of data (students + grades)
class_dictionary = {}
for row in r:
    name = str(', '.join(row[:2]))
    row = row[2:]
    class_dictionary[name] = row

print ('-------------------------------------------')
while cont == "Y":
    report_type = input('Generate a grade report for a \033[1msingle\033[0m student (S)? \nOr summary for \033[1mall\033[0m students (A)?: ' )
    print('-------------------------------------------')
    if report_type == "S":
        single_name = input('Enter student name in the format Last, First: ')
        single_assignments = input('Include only assignments containing (blank for all assignments): ')
        single_output_name = input('Enter file name for report: ')
        print ('Writing report to', single_output_name, '\b...')
        print('-------------------------------------------')

        #changed
        if single_assignments != '':
            assignments_holder = assignments
            weights_holder = weights
            grade_holder = class_dictionary.get(single_name, '')
            selected_assignments = []
            selected_weights = []
            selected_grades = []
            all_selected_grades = 0
            selected_score = 0.0
            total_score = 0.0
            temp2 = 0.0
            tally = 0.0

            for x in range(0, len(assignments_holder)):
                if single_assignments in assignments_holder[x]:
                    selected_assignments.append(assignments_holder[x])
                    selected_weights.append(weights_holder[x])
                    selected_grades.append(grade_holder[x])


            names_list = list(class_dictionary.keys())
            for v in range(0, len(names_list)):
                for t in range(0, len(assignments_holder)):
                    temp = class_dictionary.get(names_list[v], '')
                    if single_assignments in assignments_holder[t]:

                        total_bottom = float(float(selected_weights[t]) * 100 * (len(names_list) * len(selected_assignments))/(len(names_list)))
                        all_selected_grades += (float(float(temp[t]) * float(selected_weights[t])) / float(float(selected_weights[t]) * 100 * (len(names_list) * len(selected_assignments))))
                        total_top = (all_selected_grades) * total_bottom

            output_file = open(single_output_name, 'w')
            output_file.write(single_name + '\n----------------------------------------\n')
            output_file.write('Assignment'.ljust(17) + 'Weight'.ljust(17) + 'Grade'.ljust(12) + '\n')

            for y in range (0, len(selected_assignments)):
                output_file.write(selected_assignments[y].ljust(17) + ((str(float(selected_weights[y]) * 100)) + '%').ljust(17) + str(selected_grades[y]).ljust(12) + '\n')

            output_file.write('----------------------------------------\n')

            for z in range (0, len(selected_assignments)):
                selected_score += float(weights_holder[z]) * float(selected_grades[z])
                total_score += float(weights_holder[z]) * 100

            output_file.write('Overall:'.ljust(17) + (str(selected_score) + '%/' + str(total_score) + '%').ljust(17) + ('{0:.1f}'.format((selected_score / total_score) * 100)).ljust(12) + '\n')
            output_file.write('Class Average:'.ljust(17) + (str(total_top) + '%/' + str(total_bottom) + '%').ljust(17) + str('{0:.1f}'.format((all_selected_grades) * 100)).ljust(12) + '\n')
            output_file.close()

            selected_assignments = []
            selected_weights = []
            selected_grades = []
            selected_score = 0.0
            total_score = 0.0
        #unchanged
        else:
            grade_holder = class_dictionary.get(single_name, '')
            total_all_score = 0.0
            total_class_score = 0.0
            total_score = 0.0
            weighted_grades = []

            names_list = list(class_dictionary.keys())

            for q in range(0, len(names_list)):
                for e in range(0, len(assignments)):
                    grade_list = class_dictionary.get(names_list[q])
                    weighted_grades.append((float(grade_list[e]) * float(weights[e])))

            total_class_score = float(sum(weighted_grades)) / int(len(names_list))

            output_file = open(single_output_name, 'w')

            output_file.write(single_name + '\n----------------------------------------\n')

            output_file.write('Assignment'.ljust(17) + 'Weight'.ljust(17) + 'Grade'.ljust(12) + '\n')

            for y in range (0, len(assignments)):
                output_file.write(assignments[y].ljust(17) + ((str(float(weights[y]) * 100)) + '%').ljust(17) + grade_holder[y].ljust(12) + '\n')

            output_file.write('----------------------------------------\n')

            for z in range (0, len(assignments)):
                total_all_score += float(weights[z]) * 100
                total_score += float(weights[z]) * float(grade_holder[z])
            output_file.write('Overall:'.ljust(17) + (str(total_score) + '%/' + str(total_all_score) + '%').ljust(17) + ('{0:.1f}'.format((total_score / total_all_score) * 100)).ljust(12) + '\n')
            output_file.write('Class Average:'.ljust(17) + (str(total_class_score) + '%/' + str(total_all_score) + '%').ljust(17) + ('{0:.1f}'.format((total_class_score / total_all_score) * 100)).ljust(12))

            output_file.close()

    elif report_type == "A":
        assignments_holder = assignments
        weights_holder = weights
        score_holder = []
        selected_assignments = []
        selected_weights = []
        selected_grades = []
        grand_total_top = 0.0
        grand_total_bottom = 0.0

        class_assignments = input('Include only assignments containing (blank for all assignments): ')
        class_output_name = input('Enter file name for report: ')
        print ('Writing report to', class_output_name, '\b...')
        print('-------------------------------------------')

        output_file = open(class_output_name, 'w')
        output_file.write('Summary Report' + '\n' + '----------------------------------------\n')

        if class_assignments != '':

            for x in range(0, len(assignments_holder)):
                if class_assignments in assignments_holder[x]:
                    selected_assignments.append(assignments_holder[x])
                    selected_weights.append(weights_holder[x])


            names_list = list(class_dictionary.keys())
            for r in range(0, len(names_list)):
                selected_grades = class_dictionary.get(names_list[r], '')
                output_file.write(str(names_list[r]).ljust(17))
                for d in range (0, len(selected_weights)):
                    grand_total_bottom += float(float(selected_weights[d]) * 100)
                    grand_total_top += float(float(selected_weights[d]) * float(selected_grades[d]))

                output_file.write((str(float(grand_total_top)) + '%/' + str(float(grand_total_bottom)) + '%').ljust(17))
                output_file.write(str('{0:.1f}'.format((float(grand_total_top)/float(grand_total_bottom))*100)).ljust(12) + '\n')
                grand_total_top = 0.0
                grand_total_bottom = 0.0

                    #print(selected_grades[d])
                    #print(selected_weights[d] + '%')




            output_file.close()
    cont = str(input('Go again? (Y/N): '))
    print('-------------------------------------------')
