from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .models import Test, TestScore
from account.models import CustomUser

def Home(request):
    tests = Test.objects.all().order_by('-created_at')

    context = {
        'tests': tests
    }

    if request.method == 'GET':
        return render(request, 'exam/home.html', context)
    
    search_text = request.POST.get('search_input')
    if len(search_text)==0:
        return render(request, 'exam/home.html', context)
    search_texts = search_text.split()
    search_results = []
    for text in search_texts:
        results = tests.filter(Q(name__icontains=text) | Q(desc__icontains=text))
        for result in results:
            if result not in search_results:
                search_results.append(result)
                
    context['search_texts'] = search_text,
    context['tests'] = search_results
    return render(request, 'exam/home.html', context)
    
def GetTest(request, pk):
    test = Test.objects.get(id=pk)

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
        return redirect('/')
    
def CheckTest(correct_answers: str, options: str, count: int) -> int:
    counter = 0
    for i in range(0, count):
        if correct_answers[i] == options[i]:
            counter += 1
    return counter

def SendFile(request, pk):
    test = Test.objects.get(id=pk)
    try:
        file_data = open(test.file_of_questions.path, 'rb')
        response = HttpResponse(file_data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="test.pdf"'
    except IOError:
        response = HttpResponse('<h1>Fayl topilmadi</h1>')
    return response



