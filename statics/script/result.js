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
    }
    return User;
})();

baseApp.controller("BaseCtrl", [
    "$scope", "$rootScope", "$http", function($scope, $rootScope, $http) {

        $scope.resultInit = function() {
            $scope.isLoadingSubmit = true;
            name_as_id = window.location.pathname.replace("/result/","");

            $http({
                method: 'GET',
                url: '/user/api/get_result?name_as_id=' + name_as_id,
            }).then((function(response) {
                data = response.data
                $scope.user = new User(data);
                $scope.isLoadingSubmit = false;
            }));
        }


        // 1번만 뜬다.
        // 클릭을 하면 정보를 저장해두고, 2번으로 넘어간다.
        // 뒤로가기를 누르면 다시 1번으로 온다.







  }
]);
