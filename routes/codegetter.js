var express = require('express');
var fs = require('fs');
var path = require('path');
var Promise = require("bluebird");
var router = express.Router();
var defaultCode = "There was a problem loading code, please try again.";
var examplesByLanguage = require('../examples/examples.json').examples;
Promise.promisifyAll(fs);

router.use(function timeLog(req, res, next) {
  next();
});

router.get('/exercise/:language/:session/:id', function(req, res, next) {
  var language = req.params.language;
  var session = req.params.session;
  var exercise = req.params.id;
  var examples = examplesByLanguage[language] || examplesByLanguage['en'];
  getCode(exercise, session, "../examples/")
  .then(function(data) {
    var prevAndNext = nextAndPrevExercises(examples, language, session, exercise);
    var resJson = {
      key: req.params.id,
      nextExercise: prevAndNext.next,
      previousExercise: prevAndNext.prev,
      code: data
    };
    res.set({'Cache-Control': 'public, max-age=3600'});
    res.json(resJson);
  })
  .catch(function(err) {
    res.json({ key: req.params.id, code: defaultCode});
  });
});

router.get('/module/modules/:id', function(req, res, next) {
  getCode(req.params.id, 'modules', "../public/")
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

function nextAndPrevExercises(examples, language, sessionKey, exerciseKey) {
  function sessionByKey(example) {
    return example.key == sessionKey;
  }

  function findExerciseIndex(session, exerciseKey) {
    for (var i=0; i < session.length; i++) {
      if (session[i].key == exerciseKey) {
	return i;
      }
    }
    
    return -1;
  }

  var prevObject, nextObject;
  var session = examples.find(sessionByKey) || {};
  var exercises = session.exercises || [];
  var index = findExerciseIndex(exercises, exerciseKey);

  if (index >= 0) {
    var prev = exercises[index-1] || {};
    var next = exercises[index+1] || {};

    if (prev.key) {
      prevObject = {language: language, session: sessionKey, exercise: prev.key};
    } else {
      prevObject = undefined;
    }

    if (next.key) {
      nextObject = {language: language, session: sessionKey, exercise: next.key};
    } else {
      nextObject = undefined;
    }
    
    return {next: nextObject, prev: prevObject};
  } else {
    return {};
  }
}

module.exports = router;
