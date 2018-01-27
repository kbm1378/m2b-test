var baseApp;

baseApp = angular.module("baseApp", ['ngAnimate']);

baseApp.config(function($interpolateProvider, $sceProvider, $httpProvider) {
  $interpolateProvider.startSymbol("{$");
  return $interpolateProvider.endSymbol("$}");
});

baseApp.config([
  '$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }
]);


QuizQuestion = (function() {
    function QuizQuestion(id, type, title, helper, additional, isHorizontal) {
        this.id = id;
        this.type = type;
        this.title = title;
        this.helper = helper;
        if (type == "radio"){
            this.quizItemList = additional
        }else if(type == "text"){
            this.placeholder = additional
        }else if(type == "select-age"){
            this.selectableAge = []
            for (age = i = 20; i < 100; age = ++i) {
                this.selectableAge.push({
                    name: age + "세",
                    value: age
                });
            }
        }
        if (isHorizontal){
            this.isHorizontal = true
        }else{
            this.isHorizontal = false
        }


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
        this[1] = null;
        this[2] = null;
        this[3] = null;
        this[4] = null;
        this[5] = null;
        this[6] = null;
        this[7] = null;
        this[8] = null;
        this[9] = 1; //향수
        this[10] = ""; //성별
        this[11] = null; //나이
        this[12] = ""; //이름
    }
    return User;
})();



baseApp.controller("BaseCtrl", [
    "$scope", "$rootScope", "$http", function($scope, $rootScope, $http) {
        $scope.user = new User();
        console.log($scope.user);
        $scope.quizQuestionList = [];
        $scope.state = {
            'isLoading': false
        };
        $scope.quizQuestionList.push(new QuizQuestion(
            1,
            "radio",
            '1. 좋아하는 색은?',
            '향의 또 다른 언어는 이미지입니다. 색으로 나를 표현하는 것은 향으로 나를 표현하는 첫 단계입니다.',
            [
                new QuizItem(1, '빨강', 'https://i.imgur.com/gbMEtRN.jpg'),
                new QuizItem(2, '노랑', 'https://i.imgur.com/N8l6Rbw.jpg'),
                new QuizItem(3, '초록', 'https://i.imgur.com/uWMBWys.jpg'),
                new QuizItem(4, '파랑', 'https://i.imgur.com/k7JBfoV.jpg'),
                new QuizItem(5, '검정', 'https://i.imgur.com/G9CnmVB.jpg'),
                new QuizItem(6, '흰색', '')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            2,
            "radio",
            '2. 다니고 있는 직장은?',
            '향수는 개인적인 아이템이 아니라 당신 주변의 사람과 공유하는 아이템입니다.',
            [
                new QuizItem(1, '영업직', 'https://i.imgur.com/gbMEtRN.jpg'),
                new QuizItem(2, '사무직', 'https://i.imgur.com/N8l6Rbw.jpg'),
                new QuizItem(3, '연구직', 'https://i.imgur.com/uWMBWys.jpg'),
                new QuizItem(4, '전문직', 'https://i.imgur.com/k7JBfoV.jpg'),
                new QuizItem(5, '사업가', 'https://i.imgur.com/G9CnmVB.jpg'),
                new QuizItem(6, '기타', '')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            3,
            "radio",
            '3. 가지고 있는 취미는?',
            '취미의 환경에 적합한 향수를 추천해드립니다.',
            [
                new QuizItem(1, '사람들과 함께 하는 취미', 'https://i.imgur.com/nx7ZUxC.jpg'),
                new QuizItem(2, '혼자서 하는 취미', 'https://i.imgur.com/MHjEJWh.jpg')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            4,
            "radio",
            '4. 좋아하는 음식의 분류는?',
            '고지방 음식을 좋아하는 사람은 피부의 유분으로 인해 강하고 오래가는 향이 어울립니다.',
            [
                new QuizItem(1, '채식', 'https://i.imgur.com/Q13kQaY.jpg'),
                new QuizItem(2, '균형', 'https://i.imgur.com/Kt6PSGW.jpg'),
                new QuizItem(3, '육식', 'https://i.imgur.com/XJSwvbl.jpg'),
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            5,
            "radio",
            '5. 자주 입는 패션 스타일은?',
            '패션 스타일은 향수의 선호도를 파악하는 좋은 지표입니다.',
            [
                new QuizItem(1, '하이패션', 'https://i.imgur.com/HCDqDah.jpg'),
                new QuizItem(2, '캐주얼', 'https://i.imgur.com/nhW9pp2.jpg'),
                new QuizItem(3, '프레피', 'https://i.imgur.com/IPnXqdG.jpg'),
                new QuizItem(4, '슈트', 'https://i.imgur.com/3eEXmYR.jpg'),
                new QuizItem(5, '스트릿', 'https://i.imgur.com/JxX2UNr.jpg'),
                new QuizItem(0, '', 'https://i.imgur.com/pQZnwar.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            6,
            "radio",
            '6. 주로 나타나는 성격은?',
            '연구에 의하면 성격은 환경에 대한 자극을 반영합니다. 내향적인 사람일수록 따뜻하고, 복잡한 향을 선호합니다.',
            [
                new QuizItem(1, '매우 외향적', 'https://i.imgur.com/HCDqDah.jpg'),
                new QuizItem(2, '외향적', 'https://i.imgur.com/nhW9pp2.jpg'),
                new QuizItem(3, '보통', 'https://i.imgur.com/IPnXqdG.jpg'),
                new QuizItem(4, '내향적', 'https://i.imgur.com/3eEXmYR.jpg'),
                new QuizItem(5, '매우 내향적', 'https://i.imgur.com/JxX2UNr.jpg'),
                new QuizItem(0, '', 'https://i.imgur.com/pQZnwar.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            7,
            "radio",
            '7. 몸에 열이 나는 정도는?',
            '땀에 포함된 화학성분은 향에 큰 영향을 미칩니다. 높은 체온을 가진 사람일수록 향수가 더욱 빨리 날아갑니다.',
            [
                new QuizItem(1, '차가운 편', 'https://i.imgur.com/TBhy68F.png'),
                new QuizItem(2, '보통', 'https://i.imgur.com/B9Mu37U.png'),
                new QuizItem(3, '뜨거운 편', 'https://i.imgur.com/ulXhQ9Y.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            8,
            "radio",
            '8. 여유가 있을때 주로 무엇을?',
            '당신의 라이프를 즐기는 곳은 얼마나 붐빕니까? 향은 당신 앞에 있는 사람과 함께하는 것입니다.',
            [
                new QuizItem(1, '클럽/파티', 'https://i.imgur.com/Fom4Hox.png'),
                new QuizItem(2, '혼자서 보내는 여유', 'https://i.imgur.com/5jZG8wl.png'),
                new QuizItem(3, '친구/연인과의 데이트', 'https://i.imgur.com/ulXhQ9Y.png')
            ]
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            9,
            "radio",
            '9. 성별',
            '성별에 따라 당신을 표현하는 방법이 달라집니다.',
            [
                new QuizItem(1, '남성', 'https://i.imgur.com/XuHH2zL.jpg'),
                new QuizItem(2, '여성', 'https://i.imgur.com/9Bz0oRn.jpg')
            ],
            true
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            10,
            "text",
            '10. 현재 내가 가지고 있는 향수는?',
            '사용하고 있는 향수는 내가 이런 향에 호감을 갖고 있구나라는 것을 알 수 있습니다.',
            'ex) CK ONE, 존 바바토스, 앤디미온'
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            11,
            "select-age",
            '11. 나이',
            '거의 다왔습니다! 연령별로 어울리는 향이 다릅니다.',
            []
        ));
        $scope.quizQuestionList.push(new QuizQuestion(
            12,
            "text",
            '12. 이름',
            '마지막으로, 어떤 분의 향을 찾아야할지 알려주세요. 입력하신 이름은 향수 병에 넣을 수 있습니다.',
            'ex) 김투비'
        ));


        setTimeout(function(){
            $("#question--1").css("height", document.documentElement.clientHeight - 146);
        }, 100);

        $scope.onClickBack = function(quizQuestion) {
             beforeStep = quizQuestion.id - 1;
             if ($scope.quizQuestionList[beforeStep-1].type == "radio"){
                 setTimeout(function(){
                     $("#question--" + String(quizQuestion.id+1)).css("height", document.documentElement.clientHeight - 146);
                 }, 50);
             }
             $scope.user.step = beforeStep
        }

        $scope.onClickQuizItem = function(quizQuestion, quizItem) {
            nextStep = quizQuestion.id + 1;
            if (quizItem!=null){
                if (quizItem.id == 0){
                    return;
                }
                $scope.user[quizQuestion.id] = quizItem.id;
            }
            if ($scope.quizQuestionList[nextStep-1].type == "radio"){
                setTimeout(function(){
                    $("#question--" + String(quizQuestion.id+1)).css("height", document.documentElement.clientHeight - 146);
                }, 50);
            }

            $scope.user.step = nextStep;
        };

        $scope.submit = function() {
            $scope.isLoadingSubmit = true;

            payload = {
                'color': $scope.user[1],
                'job': $scope.user[2],
                'hobby': $scope.user[3],
                'food': $scope.user[4],
                'fashion': $scope.user[5],
                'introversion': $scope.user[6],
                'heat': $scope.user[7],
                'holiday': $scope.user[8],
                'my_perfume':$scope.user[9],
                'gender':$scope.user[10],
                'age':$scope.user[11],
                'name':$scope.user[12]
            };

            $http({
                method: 'POST',
                url: '/user/submit',
                data:  JSON.stringify(payload),
                headers: {
                    'Content-Type': 'application/json; charset=utf-8'
                }
            }).then((function(response) {
                reloadUrl = "/result/" + response.data.page_id;
                window.location.href=reloadUrl
                console.log(reloadUrl);
                //location.reload(reloadUrl);
            }));
        }


        // 1번만 뜬다.
        // 클릭을 하면 정보를 저장해두고, 2번으로 넘어간다.
        // 뒤로가기를 누르면 다시 1번으로 온다.







  }
]);
