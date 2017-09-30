angular.module('familyNameDraw', [])
  .controller('MainController', MainController);

function MainController($scope, $http) {

  $scope.showResults = false;
  $scope.resultsLoading = false;
  $scope.disableButton = false;
  $scope.showEverythingsTerrible = false;
  $scope.state = {
    familyMembers: [],
    selectedMember: undefined,
    result: undefined
  };

  $scope.showLoading = true;
  $scope.familyMembers = [];

  $http.get('/api/v1/member')
    .then(function (response) {
      $scope.state.familyMembers = response.data.data;
      $scope.showLoading = false;
    });

  $scope.updateSelect = function () {
    $scope.resultsLoading = false;
    $scope.showResults = false;
    $scope.state.result = undefined;
    $scope.disableButton = false;
  };

  $scope.drawName = function () {
    $scope.disableButton = true;
    $scope.resultsLoading = true;
    $scope.showResults = true;

    $http.post('/api/v1/member/' + $scope.state.selectedMember.name)
      .then(function (response) {
        var result = response.data.data;
        if (result.length === 0) {
          $scope.showEverythingsTerrible = true;
        } else {
          $scope.state.result = response.data.data[0];
        }
        $scope.resultsLoading = false;
      });
  };
}
