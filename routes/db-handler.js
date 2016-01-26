var express = require('express');
var path = require('path');
var router = express.Router();
var ENV = require('../env');
var Promise = require('bluebird');
var mongodb = require('mongodb');
var _ = require('lodash');
var collection = 'codes';

/* Get codes for name */
router.get('/getSaved/:name', function(req, res, next) {
  var name = req.params.name;
  var db = req.db;
  db.collection('codes').findOne({ key: name })
  .then(function(item) {
    res.json({ data: item.codes });
  })
  .catch(function(err) {
    res.json({});
  });
});

router.get('/getSavedForName/:name/:key', function(req, res, next) {
  var name = req.params.name;
  var key = req.params.key;
  var db = req.db;
  db.collection('codes').findOne({ key: name })
  .then(function(item) {
    res.json({ data: _.filter(item.codes, {timestamp: key})[0] });
  })
  .catch(function(err) {
    res.json({});
  });
});

/* Save to db */
router.post('/save', function(req, res, next) {
  var data = req.body;
  var db = req.db;
  var codes = {timestamp: data.timestamp, code: data.code, name: data.name};
  db.collection(collection).update({key: data.name}, { $push: { codes: codes }}, {upsert: true})
  .then(function() {
    res.sendStatus(200);
  })
  .catch(function(err) {
    console.log("Ups, error occurred " + err);
    res.sendStatus(500);
  });
});

module.exports = router;
