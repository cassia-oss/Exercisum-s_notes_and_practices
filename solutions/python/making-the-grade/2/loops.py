"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    return [round(score) for score in student_scores]
    pass


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed_students = 0
    for score in student_scores:
        if score <= 40:
            failed_students += 1
        else:
            continue
    return failed_students
    pass


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_students = []
    for score in student_scores:
        if score >= threshold:
            best_students.append(score)
        else:
            continue
    return best_students
    pass


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    # 计算最高分与及格线的差值，后续均匀分成4个区间
    score_range = highest - 40
    # 每个区间的分数跨度（均匀划分）
    interval = score_range // 4
    # 计算各等级阈值并转整数，按D、C、B、A顺序返回
    d_threshold = 41 + interval
    c_threshold = d_threshold + interval
    b_threshold = c_threshold + interval
    # 转int是因为题目示例返回整数，与之前的分数四舍五入逻辑一致
    return [41,round(d_threshold), round(c_threshold), round(b_threshold)]
    pass


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    result = []
    for n in range(len(student_scores)):
        result.append(f"{n+1}. {student_names[n]}: {student_scores[n]}")
    return result
    pass    


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect_score = []
    for i in range(len(student_info)):
        name_score = list(student_info[i])
        if name_score[1] != 100:
            continue
        else:
            perfect_score = name_score
            break
    return perfect_score
    pass
