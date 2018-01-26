var baseApp;

baseApp = angular.module("baseApp", []);

baseApp.config(function($interpolateProvider, $sceProvider, $httpProvider) {
  $interpolateProvider.startSymbol("{$");
  return $interpolateProvider.endSymbol("$}");
});


QuizQuestion = (function() {
    function QuizQuestion(id, title, helper, quiz_item_list) {
        this.id = id;
        this.title = title;
        this.helper = helper;
        this.quizItemList = quiz_item_list
    }
    return QuizQuestion;
})();

QuizItem = (function() {
    function QuizItem(id, name, img_url) {
        this.id = id;
        this.name = name;
        this.imgUrl = img_url;
    }
    return QuizItem;
})();

User = (function() {
    function User() {
        this.step = 1;
        this.color = null;
    }
    return User;
})();



baseApp.controller("BaseCtrl", [
    "$scope", "$rootScope", "$http", function($scope, $rootScope, $http) {
        $scope.user = new User()
        $scope.quizQuestionList = [];
        $scope.quizQuestionList.push(new QuizQuestion(
            1,
            '1. 좋아하는 색은?',
            '향의 또 다른 언어는 이미지입니다. 색으로 나를 표현하는 것은 향으로 나를 표현하는 첫 단계입니다.',
            [
                new QuizItem(1, '빨강', 'https://i.imgur.com/Fom4Hox.png'),
                new QuizItem(2, '노랑', 'https://i.imgur.com/5jZG8wl.png'),
                new QuizItem(3, '초록', 'https://i.imgur.com/ulXhQ9Y.png'),
                new QuizItem(4, '파랑', 'https://i.imgur.com/fqTKzX1.png'),
                new QuizItem(5, '검정', 'https://i.imgur.com/I0qZZBF.png'),
                new QuizItem(6, '흰색', 'https://i.imgur.com/I0qZZBF.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            2,
            '2. 다니고 있는 직장은?',
            '수는 개인적인 아이템이 아니라 당신 주변의 사람과 공유하는 아이템입니다.',
            [
                new QuizItem(1, '영업직', 'https://i.imgur.com/Fom4Hox.png'),
                new QuizItem(2, '사무직', 'https://i.imgur.com/5jZG8wl.png'),
                new QuizItem(3, '연구직', 'https://i.imgur.com/ulXhQ9Y.png'),
                new QuizItem(4, '전문직', 'https://i.imgur.com/fqTKzX1.png'),
                new QuizItem(5, '사업가', 'https://i.imgur.com/I0qZZBF.png'),
                new QuizItem(6, '기타', 'https://i.imgur.com/I0qZZBF.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            3,
            '3. 가지고 있는 취미는?',
            '취미의 환경에 적합한 향수를 추천해드립니다.',
            [
                new QuizItem(1, '사람들과 함께 하는 취미', 'https://i.imgur.com/Fom4Hox.png'),
                new QuizItem(2, '혼자서 하는 취미', 'https://i.imgur.com/5jZG8wl.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            4,
            '4. 좋아하는 음식의 분류는?',
            '고지방 음식을 좋아하는 사람은 피부의 유분으로 인해 강하고 오래가는 향이 어울립니다.',
            [
                new QuizItem(1, '채식', 'https://i.imgur.com/Fom4Hox.png'),
                new QuizItem(2, '균형', 'https://i.imgur.com/5jZG8wl.png'),
                new QuizItem(3, '육식', 'https://i.imgur.com/ulXhQ9Y.png'),
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            5,
            '5. 자주 입는 패션 스타일은?',
            '패션 스타일은 향수의 선호도를 파악하는 좋은 지표입니다.',
            [
                new QuizItem(1, '하이패션', 'https://i.imgur.com/Fom4Hox.png'),
                new QuizItem(2, '캐주얼', 'https://i.imgur.com/5jZG8wl.png'),
                new QuizItem(3, '프레피', 'https://i.imgur.com/ulXhQ9Y.png'),
                new QuizItem(4, '슈트', 'https://i.imgur.com/fqTKzX1.png'),
                new QuizItem(5, '스트릿', 'https://i.imgur.com/I0qZZBF.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            6,
            '6. 주로 나타나는 성격은?',
            '연구에 의하면 성격은 환경에 대한 자극을 반영합니다. 내향적인 사람일수록 더욱 따뜻하고, 복잡한 향을 선호합니다.',
            [
                new QuizItem(1, '매우 외향적', 'https://i.imgur.com/Fom4Hox.png'),
                new QuizItem(2, '외향적', 'https://i.imgur.com/5jZG8wl.png'),
                new QuizItem(3, '보통', 'https://i.imgur.com/ulXhQ9Y.png'),
                new QuizItem(4, '내향적', 'https://i.imgur.com/fqTKzX1.png'),
                new QuizItem(5, '매우 내향적', 'https://i.imgur.com/I0qZZBF.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            7,
            '7. 몸에 열이 나는 정도는?',
            '땀에 포함된 화학성분은 향수의 밸런스와 향에 큰 영향을 미칩니다. 높은 체온을 가진 사람일수록 향수가 더욱 빨리 날아갑니다.',
            [
                new QuizItem(1, '차가운 편', 'https://i.imgur.com/Fom4Hox.png'),
                new QuizItem(2, '보통', 'https://i.imgur.com/5jZG8wl.png'),
                new QuizItem(3, '뜨거운 편', 'https://i.imgur.com/ulXhQ9Y.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            8,
            '8. 시간의 여유가 있을때 주로 무엇을?',
            '당신의 라이프를 즐기는 곳은 얼마나 붐빕니까? 향은 당신 앞에 있는 사람과 함께하는 것입니다.',
            [
                new QuizItem(1, '클럽/파티', 'https://i.imgur.com/Fom4Hox.png'),
                new QuizItem(2, '혼자서 보내는 여유', 'https://i.imgur.com/5jZG8wl.png'),
                new QuizItem(3, '친구/연인과의 데이트', 'https://i.imgur.com/ulXhQ9Y.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            9,
            '9. 현재 내가 가지고 있는 향수는?',
            '현재 사용하고 있는 향수는 현재 내가 이런 향에 호감을 갖고 있구나라는 것을 알 수 있습니다. 향수를 아직 사용하고 있지 않으시면 "없음"이라고 적어주셔도 됩니다.',
            []
        ));

        setTimeout(function(){
            $("#question--" + String(1)).css("height", document.documentElement.clientHeight - 131);

        }, 100);

        $scope.onClickBack = function(quizQuestion) {
            $scope.user.step = quizQuestion.id - 1;

        }

        $scope.onClickQuizItem = function(quizQuestion, quizItem) {
            $scope.user.color = quizItem.id;
            $scope.user.step = quizQuestion.id + 1;
            setTimeout(function(){
                $("#question--" + String(quizQuestion.id+1)).css("height", document.documentElement.clientHeight - 131);
            }, 100);

            console.log($scope.user);
        };


        // 1번만 뜬다.
        // 클릭을 하면 정보를 저장해두고, 2번으로 넘어간다.
        // 뒤로가기를 누르면 다시 1번으로 온다.







  }
]);
