var app = (function() {
  var firebaseBaseUrl = "";
  var editor = document.getElementById("editor");
  var defaultText = "# Welcome to learn Python";
  var exercises = [];
  var code = localStorage.getItem("myCode");
  var user = localStorage.getItem("pythonInBrowserUser") ? localStorage.getItem("pythonInBrowserUser") : null;
  var myCodeMirror;

  initApp();

  /*
   * Initializing functions
   */

  function initApp() {
    $.ajax({url: "examples/examples.json",
        dataType: "json",
        async: true,
        success: function(data) {
          if(data && data.examples) {
            initExamples(data.examples);
          } else {
            console.log("reading example.json failed");
          }
        },
        error: function(err) {
          console.log("reading example.json failed");
        }
    });
    initUI();
  }

  function initExamples(examples) {
    var index = examples.length;
    function callbackCheck() {
      if(index === 0) {
        $(".exercise-container").removeClass("not-ready");
        $(".no-content").hide();
      }
    }
    _.each(examples, function(example) {
      var path = "examples/" + example.session + "/" + example.key + ".py";
      $.ajax({url: path,
        async: false,
        success: function(data) {
          if(data) {
            exercises[example.key] = data;
          }
          index--;
          callbackCheck();
        },
        error: function(err) {
          console.log("reading example failed with key:" + example);
          index--;
          callbackCheck();
        }
      });
    });
  }

  function initUI() {
    initCodeMirror();
    initClickHandlers();
    initLocalSave();
  }

  function initCodeMirror() {
    if(user) {
      $(".name-edit").html(user);
    }

    if(!code) {
      code = defaultText;
    }
    myCodeMirror = CodeMirror(editor, {
      value: code,
      mode:  "python",
      theme: "monokai",
      lineNumbers: true,
      lineWrapping: true,
      tabSize: 2,
      autofocus: true
    });
  }

  function initClickHandlers() {
    $(".session-exercises > a > li").on('click', function(event) {
      var id = $(this).attr("id");
      setCode(exercises[id]);
    });

    $(".own-exercises").on("click", "a>li>pre", function(event) {
      getCode($(this).parent("li").attr("id"), $(this).parent("li").data("parent"));
    });

    $(".session-header").on("click", function(event) {
        var id = $(this).data("key");
        $(".session-exercises").hide();
        $("#" + id).show();
    });
  }

  function initLocalSave() {
    setInterval(function(){
      saveLocally();
    },500);
  }

  /*
   * Helper functions
   */

  function initializeFirebase(firebaseUrl) {
    try {
      return new Firebase(firebaseUrl);
    } catch (err) {
      console.error('Failed to initialize Firebase: ' + err);
      return undefined;
    }
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
    $("#mycanvas").empty();
    myCodeMirror.doc.setValue(code);
  }

  function getCode(id, parent) {
    var myFirebaseRef = initializeFirebase(firebaseBaseUrl + parent + "/" + id + "/");
    if (!myFirebaseRef) {
        setErrorMessage('Firebase not configured');
        return;
    }
    return myFirebaseRef.ref().once("value", function(snapshot) {
      if(snapshot && snapshot.val() && snapshot.val().code) {
        setCode(snapshot.val().code);
      }
    });
  }

  function setErrorMessage(message) {
    outf("\n" + message);
  }

  function saveLocally() {
    localStorage.setItem("myCode", readCode());
  }

  function saveNameLocally(name) {
    localStorage.setItem("pythonInBrowserUser", name);
  }

  /*
   * Public functions
   */

  return {
    run: function() {
      $("#mycanvas").empty();
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
        },
        codeclub: {
          path: 'modules/codeclub/codeclub.py'
        },
        coordinates: {
          path: 'modules/basic/basic.py'
        }
      };

       var myPromise = Sk.misceval.asyncToPromise(function() {
           return Sk.importMainWithBody("<stdin>", false, prog, true);
       });
       myPromise.then(function(mod) {
          setErrorMessage("");
       },
          function(err) {
          setErrorMessage(err.toString());
       });
    },

    save: function() {
      var result = $(".name-edit").html();
      var myFirebaseRef = initializeFirebase(firebaseBaseUrl + result + "/");
      if (!myFirebaseRef) {
        setErrorMessage('Firebase not configured');
        return;
      }
      var data = {"code": readCode(), "timestamp": Date.now()};
      var newRef = myFirebaseRef.push(data, function(response) {
        if(!response) {
          $(".saved").show().fadeOut(800);
        }
      });
    },

    load: function() {
      var result = $(".name-edit").html();
      saveNameLocally(result);
      if(result && result.length > 1) {
        var myFirebaseRef = initializeFirebase(firebaseBaseUrl + result + "/");
        if (!myFirebaseRef) {
          setErrorMessage('Firebase not configured');
          return;
        }
        myFirebaseRef.ref().once("value", function(snapshot) {
          if(snapshot.val()) {
            $(".own-exercises").empty();
            _.each(snapshot.val(), function(snippet, key) {
              var date = moment(snippet.timestamp).format("DD.MM.YYYY HH:mm:ss");
              $(".own-exercises").append("<a href='#close'><li id=" +  key + " data-parent=" + result + "><div class='date'>" + date + "</div><pre>" + snippet.code + "</pre></li></a>");
            });
          } else {
            $(".empty-exercises").show().fadeOut(1000);
          }
        });
      }
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
