function AllClipController($scope, $http) {
    $scope.init = function() {

    var api_url = '/clips/clips/';
    $http.get(api_url)
        .then(function(response) {
            $scope.clips = response.data;
            $scope.urlAmazon = "https://s3-eu-west-1.amazonaws.com/itaplayadviserireland/media/"
            console.log($scope.clips);
        });

          

    $scope.delete = function(object) {

        $http({
            url: '/clips/delete/' + object.pk,
            method: 'DELETE',
            data: {
                pk: object.pk
            },
            headers: {
                "Content-Type": "application/json"
            }
        }).then(function(res) {
            var index = $scope.clips.indexOf(object)
            $scope.clips.splice(index, 1);
            //$scope.data.splice(object,1);
            console.log(res.clips);
        }, function(error) {
            console.log(error);
        });
    };

};
};