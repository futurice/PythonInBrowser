var app = (function() {
  var myFirebaseRef = new Firebase("");
  var editor = document.getElementById("editor");
  var code = localStorage.getItem('myCode');

  var exercises = [];
  exercises["start"] = 'print "Welcome to study with Python"';
  exercises["print"] = 'print "Welcome to study with Python"\n'+
                       'print "Add your comment here and print"';
  exercises["default"] = 'import turtle\n'+
            't = turtle.Turtle()\n'+
            't.forward(100)\n'+
            'print "Hello World"\n'+
            'print ("Hello")\n';
  if(!code) {
    code = exercises["default"];
  }
  var myCodeMirror = CodeMirror(editor, {
    value: code,
    mode:  "python",
    theme: "monokai",
    lineNumbers: true,
    lineWrapping: true
  });

  function outf(text) {
    var mypre = document.getElementById("output");
    mypre.innerHTML = mypre.innerHTML + text;
  }

  function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
      throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
  }

  function readCode() {
    return myCodeMirror.doc.getValue();
  }

  function setCode(code) {
    myCodeMirror.doc.setValue(code);
  }

  function setErrorMessage(message) {
    outf("\n" + message);
  }

  return {
    runit: function() {
       var prog = readCode();
       console.log("prog:" + prog);
       var mypre = document.getElementById("output");
       mypre.innerHTML = '';
       Sk.pre = "output";
       Sk.configure({output:outf, read:builtinRead});
       (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
       var myPromise = Sk.misceval.asyncToPromise(function() {
           return Sk.importMainWithBody("<stdin>", false, prog, true);
       });
       myPromise.then(function(mod) {
           console.log('success');
           setErrorMessage("");
       },
           function(err) {
            console.log(err.toString());
            setErrorMessage(err.toString());
       });
    },

    save: function() {
      var result = window.prompt("What's your name?");
      console.log(result);
      var data = [];
      data[result] = {"code": readCode(), "timestamp": Date.now()};
      myFirebaseRef.set(data);
    },

    load: function() {
      var result = window.prompt("What's your name?");
      myFirebaseRef.child(result).on("value", function(snapshot) {
        var code = snapshot.val().code;
        if(code) {
          setCode(code);
        } else {
          setErrorMessage("Load failed, try again.");
        }
      });
    },
    saveLocally: function() {
      localStorage.setItem('myCode', readCode());
    },
    openExercise: function(id) {
      var code = exercises[id];
      setCode(code);
    }
  };
})();

$(document).ready(function() {
  $('li').click(function(event) {
    var id = $(this).attr('id');
    app.openExercise(id);
  });
});

setInterval(function(){
      app.saveLocally();
    },500);

function runit() {
  return app.runit();
}

function load() {
  return app.load();
}

function save() {
  return app.save();
}