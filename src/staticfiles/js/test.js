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
        alert("Siz hali " + (count_of_questions - inputOfAnswers.value.length) + "ta javobni belgilamadingiz !");
        inputOfAnswers.value = '';
    }
    else{
        document.getElementById("answersForm").submit();
    }
}