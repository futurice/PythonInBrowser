# Chilicorn Code Club

Chilicorn Code Club is a [Spice program](http://spiceprogram.org/) project aiming to introduce Finnish school kids to coding and to give schools & teachers tools for facilitating the learning. Exercises are currently developed by [Futurice](http://futurice.com/) employees.

Demo version of Python in Browser can be found [here](https://codeclub.herokuapp.com/).

## Adding exercises

Write your exercise in python and save it in one of the session folders in [examples](https://github.com/futurice/PythonInBrowser/blob/master/examples/). If you are creating a new session please add new folder for it.

After adding the file edit [examples.json](https://github.com/futurice/PythonInBrowser/blob/master/examples/examples.json) and add the details of your exercise.

That's it, next time you open the codeclub page you'll see your excercise in the list of exercises.

## Adding modules

If you want to add a module or hide some of your custom made code so that you can use it in the exercise and import it in the editor you can do that. You have to options for this.

### Python module

With Python modules you work much in the same way as with exercises. Write your module in python and save it this time under [modules](https://github.com/futurice/PythonInBrowser/blob/master/public/modules/).

After adding the file edit [modules.json](https://github.com/futurice/PythonInBrowser/blob/master/examples/modules.json) IF you want to publish your module so that student can also see it. Otherwise no need to do this.

AFter this edit the run-function in [main.js](https://github.com/futurice/PythonInBrowser/blob/master/public/javascripts/main.js) to add your module to Skulpt.

Here is example on how to do it:

```
Sk.externalLibraries = {
        matter: {
          path: '../static/modules/matter/__init__.js',
          dependencies: ['../static/modules/matter/matter-0.8.0.min.js']
        },
        codeclub: {
          path: '../static/modules/codeclub.py'
        },
        coordinates: {
          path: '../static/modules/basic.py'
        },
        winter: {
          path: '../static/modules/winter.py'
        }
      };
```

### JS module

It's also possible to use JS-libraries as modules. How ever you need to write python wrapper for it to use it. For example please see how matter-0.8.0.min.js and __init__.js are added.

## Adding learning material

If you want to add learning material please edit [material.json](https://github.com/futurice/PythonInBrowser/blob/master/examples/material.json).

## Technical details

* [Node.js](https://nodejs.org/) with [Express](http://expressjs.com/)
* [Handlebars](http://handlebarsjs.com/)
* [MongoDB](https://www.mongodb.org/)
* [Skulpt](http://www.skulpt.org/)
* [CodeMirror](https://codemirror.net/)

## Start developing

* Clone this repo or take a fork
* Install MongoDB
* Start MongoDB
* Copy env-local.js to env.js (and possibly edit the Mongo URL in env.js)
* In root of repo ```npm install```
* Start application with ```nodemon bin/www```
* Open a browser at http://localhost:3000/

## License
Plese see our [license](https://github.com/futurice/PythonInBrowser/blob/master/LICENSE).