from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.db.models import Q, Sum
from .models import Test, TestScore, Subject
from account.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def Home(request):
    tests = Test.objects.all().order_by('-created_at')
    users = CustomUser.objects.all()
    for user in users:
        testScores = TestScore.objects.filter(user=user).values()
        sum_of_testScores = testScores.aggregate(Sum('result'))
        user.result = sum_of_testScores['result__sum']
    users = users[:4]
    context = {
        'tests': tests,
        'top_rating': users,
        'subjects': Subject.objects.all().order_by('name'),
        'levels': Test.objects.values_list()
    }
    if request.method == 'GET':
        return render(request, 'exam/home.html', context)

@login_required(login_url="/account/login/")
def GetTest(request, pk):
    test = get_object_or_404(Test, id=pk)
    if test is not None:
        if request.method == 'GET':
            all_attempts = TestScore.objects.filter(test=test)
            last_scores = all_attempts[:10]
            score_of_user = TestScore.objects.filter(test=test, user=request.user).first()
            attempts = all_attempts.count()
            average_score = 0

            if attempts != 0:
                for a in all_attempts:
                    average_score += a.count_of_correct_answers * test.point
                average_score /= attempts
                average_score = round(average_score, 2)

            context = {
                'test': test,
                'last_scores': last_scores,
                'score_of_user': score_of_user,
                'attempts': attempts,
                'max_score': test.count_of_questions * test.point,
                'average_score': average_score 
            }

            return render(request, 'exam/test.html', context)
        
        return render(request, 'exam/starttest.html', {'test':test})

@login_required(login_url="/account/login/")
def CheckAnswers(request, pk):
    if request.method == 'POST':
        test = Test.objects.get(id=pk)
        answers = request.POST.get('answers')
        checked_correct_answers = CheckTest(test.answers, str(answers), test.count_of_questions)
        test_score = TestScore(test=test, 
                                    count_of_questions=test.count_of_questions,
                                    count_of_correct_answers = checked_correct_answers,
                                    user=request.user,
                                    result=checked_correct_answers * test.point)
        test_score.save(force_insert=True)
        request.method = 'GET'
        return GetTest(request, pk)

def CheckTest(correct_answers: str, options: str, count: int) -> int:
    counter = 0
    for i in range(0, count):
        if correct_answers[i] == options[i]:
            counter += 1
    return counter

@login_required(login_url="/account/login/")
def SendFile(request, pk):
    test = Test.objects.get(id=pk)
    try:
        file_data = open(test.file_of_questions.path, 'rb')
        response = HttpResponse(file_data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="test.pdf"'
    except IOError:
        response = HttpResponse('<h1>Fayl topilmadi</h1>')
    return response



