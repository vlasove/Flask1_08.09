//Добавить во вкладку tests внутри /auth

var jsonData = JSON.parse(responseBody);
tests["Test for jwt"] = jsonData.access_token!== undefined;

pm.environment.set("jwt_token", jsonData.access_token);