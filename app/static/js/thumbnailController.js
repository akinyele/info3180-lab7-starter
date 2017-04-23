
app.controller('thumbnailCtrl', function($scope, $http) {
  $scope.test = "hello";

  $http.get("http://info3180-lab7-akinyele.c9users.io:8080/api/thumbnail").then(function (response) {
      $scope.thumbnails = response.data.thumbnails;
     
  });
});