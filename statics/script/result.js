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

User = (function() {
    function User(data) {
        this.name = data.name;
        this.perfumeCommon = data.perfume_common;
        this.perfumeSpecial = data.perfume_special;
        this.perfumeCommonReasonText = data.perfume_common_reason_text;
        this.perfumeSpecialReasonText = data.perfume_special_reason_text;
    }
    return User;
})();

baseApp.controller("BaseCtrl", [
    "$scope", "$rootScope", "$http", function($scope, $rootScope, $http) {

        $scope.resultInit = function() {
            $scope.isLoadingResult = true;
            name_as_id = window.location.pathname.replace("/","");

            $http({
                method: 'GET',
                url: '/user/api/get_result?name_as_id=' + name_as_id,
            }).then((function(response) {
                data = response.data
                $scope.user = new User(data);
                $scope.isLoadingResult = false;

                setTimeout(function(){
                    var typed = new Typed('#typed', {
                        stringsElement: '#typed-strings',
                        typeSpeed: 40
                    });
                }, 100);
            }));
        }

        $scope.onScrollToCommon = function(){
            $("html, body").animate({ scrollTop: $("#detail_common").position().top });
        }

        $scope.onScrollToSpecial = function(){
            $("html, body").animate({ scrollTop: $("#detail_special").position().top });
        }

        $scope.onScrollToOpenevent = function(){
            $("html, body").animate({ scrollTop: $("#detail_openevent").position().top });
        }

        $scope.onReload = function(url){
            window.location.href=url;
        }





        // 1번만 뜬다.
        // 클릭을 하면 정보를 저장해두고, 2번으로 넘어간다.
        // 뒤로가기를 누르면 다시 1번으로 온다.







  }
]);
