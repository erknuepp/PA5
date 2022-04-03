# PA5template.py

def increment_attendance(seating, locations):
    for l in locations:
        seating[l[0]][l[1]] += 1


def drop_lowest(scores, drop_number):

    num_to_check = len(drop_number)
    for index in range(num_to_check):
        for _ in range(drop_number[index]):
            scores[index].remove(min(scores[index]))


def organize_grades(grades, assignment_types, max_possible):
    num_to_check = len(grades)
    dict_to_return = {'zy': [], 'lab': [], 'pa': [],
                      'mid1': [], 'mid2': [], 'final': []}
    for index in range(num_to_check):
        dict_to_return[assignment_types[index]].append(grades[index]/max_possible[index])
    return dict_to_return


def gbook_averages(gbook):
    averaged_gbook = gbook
    for k, v in gbook.items():
        if len(v) > 0:
            averaged_gbook[k] = sum(v)/len(v)
        else:
            averaged_gbook[k] = 0.0
    return averaged_gbook


def course_grade(gbook, weights, replace):
    # if replace key should replaces a replace value with a lower grade
    for k, v in replace.items():
        if gbook[k] > gbook[v]:
            gbook[v] = gbook[k]
    grade = 0.0        
    for i in range(len(gbook)):
        grade += list(gbook.values())[i] * list(weights.values())[i]
    return grade
