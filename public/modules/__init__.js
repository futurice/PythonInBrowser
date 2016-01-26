var $builtinmodule = function(name) {
  var mod = {};

  var Engine = Matter.Engine,
      World = Matter.World,
      Bodies = Matter.Bodies;

  var engine = Engine.create(getConfiguredTarget(), {
    render: {
      options: {
	width: (Sk.matter && Sk.matter.width) || 600,
	height: (Sk.matter && Sk.matter.height) || 600
      }
    }
  });

  var mouseConstraint = Matter.MouseConstraint.create(engine);
  World.add(engine.world, mouseConstraint);

  function getConfiguredTarget() {
    var selector, target;

    selector = (Sk.matter && Sk.matter.target) || "matter",
    target   = typeof selector === "string" ?
      document.getElementById(selector) :
      selector;
    // ensure that the canvas container is empty
    while (target.firstChild) {
      target.removeChild(target.firstChild);
    }
    return target;
  }

  mod.rectangle = new Sk.builtin.func(function (x, y, width, height, is_static) {
    Sk.builtin.pyCheckArgs("rectangle", arguments, 4, 5);
    Sk.builtin.pyCheckType("x", "number", Sk.builtin.checkNumber(x));
    Sk.builtin.pyCheckType("y", "number", Sk.builtin.checkNumber(y));
    Sk.builtin.pyCheckType("width", "number", Sk.builtin.checkNumber(width));
    Sk.builtin.pyCheckType("height", "number", Sk.builtin.checkNumber(height));
    if (is_static !== undefined) {
      Sk.builtin.pyCheckType("is_static", "bool", Sk.builtin.checkBool(is_static));
    }

    var isstat;
    if (is_static === undefined) {
      isstat = false;
    } else {
      isstat = Sk.misceval.isTrue(is_static);
    }

    var props = { isStatic: isstat };
    var box = Bodies.rectangle(Sk.builtin.asnum$(x), Sk.builtin.asnum$(y),
			       Sk.builtin.asnum$(width), Sk.builtin.asnum$(height),
			       props);
    World.add(engine.world, [box]);

    return undefined;
  });

  mod.circle = new Sk.builtin.func(function (x, y, radius) {
    Sk.builtin.pyCheckArgs("rectangle", arguments, 3, 3);
    Sk.builtin.pyCheckType("x", "number", Sk.builtin.checkNumber(x));
    Sk.builtin.pyCheckType("y", "number", Sk.builtin.checkNumber(y));
    Sk.builtin.pyCheckType("radius", "number", Sk.builtin.checkNumber(radius));

    var circle = Bodies.circle(Sk.builtin.asnum$(x), Sk.builtin.asnum$(y),
			       Sk.builtin.asnum$(radius));
    World.add(engine.world, [circle]);

    return undefined;
  });

  mod.run = new Sk.builtin.func(function () {
    Sk.builtin.pyCheckArgs("run", arguments, 0, 0);
    Engine.run(engine);
    return undefined;
  });

  return mod;
};
