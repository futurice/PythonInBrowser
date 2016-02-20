var express = require('express');
var fs = require('fs');
var path = require('path');
var Promise = require("bluebird");
var router = express.Router();
var defaultCode = "There was a problem loading code, please try again.";
Promise.promisifyAll(fs);

router.use(function timeLog(req, res, next) {
  next();
});

router.get('/exercise/:session/:id', function(req, res, next) {
  getCode(req.params.id, req.params.session, "../examples/")
  .then(function(data) {
    var resJson = { key: req.params.id, code: data};
    res.set({'Cache-Control': 'public, max-age=3600'});
    res.json(resJson);
  })
  .catch(function(err) {
    res.json({ key: req.params.id, code: defaultCode});
  });
});

function getCode(id, session, pathToCode) {
  var pathName = pathToCode + session + "/" + id + ".py";
  var finalPath = path.resolve(__dirname, pathName);
  console.log("Exercise file: " + finalPath);
  return fs.readFileAsync(path.resolve(__dirname, pathName),"utf-8")
    .then(function(data) {
      return data;
    });
}

module.exports = router;
