function checkTest(){
    var inputOfAnswers = document.getElementById('answers');
    var count_of_questions = document.getElementsByClassName('countOfanswerRows').length;
    for(var i = 1; i <= count_of_questions; i++){
        var itemName = 'a'+ i;
        var answers_row = document.getElementsByName(itemName);
        for(var j = 0; j < 4; j++){
            if(answers_row[j].checked){
                inputOfAnswers.value += answers_row[j].value;
            }
        }
    }
    if(inputOfAnswers.value.length != count_of_questions){
        var testAlert = document.getElementById('test_alert');
        document.getElementById("test_alert").innerHTML = '<div class="alert alert-primary alert-dismissible mt-4" role="alert">' 
            + '<span id="missedAnswers"></span><button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';        
        var missedAnswers = document.getElementById('missedAnswers');
        missedAnswers.textContent = 'Siz hali ' + (count_of_questions - inputOfAnswers.value.length) + ' ta javobni belgilamadingiz';
        inputOfAnswers.value = '';
    }
    else{
        document.getElementById("answersForm").submit();
    }
}

