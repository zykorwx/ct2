var customInterpolationApp = angular.module('angular-django-app', []);
 
customInterpolationApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('#{');
  $interpolateProvider.endSymbol('}');
});
 
 
customInterpolationApp.controller('probandoAngularController', function DemoController() {
    this.msg = "Estoy cambiando la interpolation de {{ a #{  a ver si funciona";
});

function MyCtrl($scope) {
  $scope.action = function() {
    $scope.name1 = 'OK2';
  }
 
  $scope.name1 = 'World';
}