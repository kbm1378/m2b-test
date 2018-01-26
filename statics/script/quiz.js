var baseApp;

baseApp = angular.module("baseApp", ['ui.router']);

baseApp.config(function($interpolateProvider, $sceProvider, $httpProvider) {
  $interpolateProvider.startSymbol("{$");
  return $interpolateProvider.endSymbol("$}");
});

baseApp.controller("BaseCtrl", [
  "$scope", "$rootScope", "$http", function($scope, $rootScope, $http) {
      console.log("hi")

      $scope.test = "테스트"


  }
]);
