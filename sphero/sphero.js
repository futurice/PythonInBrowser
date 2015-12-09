var Cylon = require('cylon');
var _ = require('lodash');

Cylon.robot({
  connections: {
    sphero: { adaptor: 'sphero', port: '/dev/tty.Sphero-YOW-AMP-SPP' }
  },

  devices: {
    sphero: { driver: 'sphero' }
  },

  work: function(my) {
    var defaultSteps = [
      {speed: 50, angle: 0, duration: 2},
      {speed: 50, angle: 90, duration: 2},
      {speed: 50, angle: 180, duration: 2},
      {speed: 50, angle: 270, duration: 2}
    ];

    function doMove(steps) {
      console.log("do move called " + steps.length);
      if(steps.length > 0) {
        my.sphero.stop(function() {
          _.delay(function() {
            my.sphero.roll(steps[0].speed, steps[0].angle);
            _.delay(doMove, steps[0].duration * 1000, _.drop(steps));
          }, 300);
        });
      } else {
        my.sphero.stop(function() {
          console.log("Round done, wait and start again!")
          my.sphero.randomColor(function(err, data) {
            console.log("change color first")
            _.delay(doMove, 5000 , defaultSteps);
           })
        })
      }
    }
    doMove(defaultSteps);
  }
}).start();
