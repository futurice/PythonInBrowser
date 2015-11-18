var app = (function() {
  var myFirebaseRef = initializeFirebase("");
  var editor = document.getElementById("editor");
  var examples = ["default", "start", "print"];
  var exercises = [];
  var code = localStorage.getItem("myCode");
  setExamples();

  if(!code) {
    code = exercises["default"] ? exercises["default"] : "#empty editor";
  }

  var myCodeMirror = CodeMirror(editor, {
    value: code,
    mode:  "python",
    theme: "monokai",
    lineNumbers: true,
    lineWrapping: true
  });

  $(document).ready(function() {
    $("li").click(function(event) {
      var id = $(this).attr("id");
      setCode(exercises[id]);
    });
  });

  setInterval(function(){
    saveLocally();
  },500);

  function initializeFirebase(firebaseUrl) {
    try {
      return new Firebase(firebaseUrl);
    } catch (err) {
      console.error('Failed to initialize Firebase: ' + err);
      return undefined;
    }
  };

  function setExamples() {
    _.each(examples, function(example) {
      var path = "examples/" + example + ".py";
      $.get(path, function(data) {
        if(data) {
          exercises[example] = data;
        }
      });
    });
  }

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

  function saveLocally() {
    localStorage.setItem("myCode", readCode());
  }

  return {
    run: function() {
       var prog = readCode();
       var mypre = document.getElementById("output");
       var width = document.getElementById("mycanvas").offsetWidth;
       var height = document.getElementById("mycanvas").offsetHeight;
       mypre.innerHTML = "";
       Sk.pre = "output";
       Sk.configure({output:outf, read:builtinRead});
       (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = "mycanvas";
       (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).width = width;
       (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).height = height;
       Sk.TurtleGraphics.defaults = {
                canvasID: "mycanvas",
                animate: false,
                degrees: true,
                width: 600,
                height: 600
            };
       Sk.matter = {
         target: "mycanvas",
         width: 600,
         height: 600
       };
       Sk.externalLibraries = {
         matter: {
           path: 'modules/matter/__init__.js',
           dependencies: ['modules/matter/matter-0.8.0.min.js']
         }
       };
       var myPromise = Sk.misceval.asyncToPromise(function() {
           return Sk.importMainWithBody("<stdin>", false, prog, true);
       });
       myPromise.then(function(mod) {
           console.log("success");
           setErrorMessage("");
       },
           function(err) {
            console.log(err.toString());
            setErrorMessage(err.toString());
       });
    },

    save: function() {
      if (!myFirebaseRef) {
        setErrorMessage('Firebase not configured');
        return;
      }

      var result = window.prompt("What's your name?");
      var data = {"code": readCode(), "timestamp": Date.now()};
      myFirebaseRef.once("value", function(dataSnapshot) {
        if(dataSnapshot && dataSnapshot.hasChild(result)) {
          myFirebaseRef.child(result).update(data);
        } else {
          myFirebaseRef.child(result).set(data);
        }
      });
    },

    load: function() {
      if (!myFirebaseRef) {
        setErrorMessage('Firebase not configured');
        return;
      }

      var result = window.prompt("What's your name?");
      myFirebaseRef.child(result).once("value", function(dataSnapshot) {
        if(dataSnapshot.val() && dataSnapshot.val().code) {
            setCode(dataSnapshot.val().code);
          } else {
            setErrorMessage("Load failed, try again.");
          }
      });
    }
  };
})();

function run() {
  return app.run();
}

function load() {
  return app.load();
}

function save() {
  return app.save();
}
