var gulp        = require('gulp'); //Importamos gulp
var sass        = require('gulp-sass'); //Importamos sass
var notify      = require('gulp-notify');
var browserSync = require('browser-sync').create();
var concat      = require('gulp-concat');
var browserify  = require('browserify');
var tap         = require('gulp-tap');
var buffer      = require('gulp-buffer');
var sourcemaps  = require('gulp-sourcemaps');
var uglify      = require('gulp-uglify');
var postcss = require('gulp-postcss');
var autoprefixer = require('autoprefixer');
var cssnano = require('cssnano');


var sassConfig = {
    compileSassTaskName: 'compile-sass',
    watchFiles: './assets/sass/*.scss',
    src: './assets/sass/style.scss',
    dest: './ui/static/ui/css',
    sassOpts: {
        includePaths: ['./node_modules/bootstrap/scss',
                        './node_modules/font-awesome/scss']
    }
}

var jsConfig = {
    concatJsTaskName: 'concat-js',
    watchFiles: './assets/js/*js',
    src: './assets/js/main.js',
    dest: './ui/static/ui/js'
}

var uglifyConfig = {
    uglifyTaskName: "uglify",
    src: './dist/main.js',
    dest: './ui/static/ui/js'

}
gulp.task("default",["compile-sass", "concat-js", "fonts"], function(){
    
    notify().write("Iniciando Gulp")
    //Arrancar servidor browser sync
    browserSync.init({
       proxy: "127.0.0.1:8000"
    });
    //Cuando haya cambios compila sass
    gulp.watch(sassConfig.watchFiles, [sassConfig.compileSassTaskName]);

    //Cuando haya cambios en archivos JS, los concateno
    gulp.watch(jsConfig.watchFiles, [jsConfig.concatJsTaskName]);

    // Cuando se cambien html, recargamos navegador
    gulp.watch('./ui/templates/**/*.html', function(){
        browserSync.reload();
        notify().write("Navegador recargado");
    });

});

// compila sass
gulp.task( sassConfig.compileSassTaskName, function(){
    gulp.src(sassConfig.src)
    .pipe(sourcemaps.init()) //Empezamos a capturar los sourcemaps
    .pipe(sass(sassConfig.sassOpts).on('error', function(error){
        return notify().write(error);
    }))
    .pipe(postcss([autoprefixer(), cssnano()]))
    .pipe(sourcemaps.write('./')) //Terminamos de capturar los sourcemaps
    .pipe(gulp.dest(sassConfig.dest))
    .pipe(browserSync.stream())
    .pipe(notify("SASS compilado"))
});

//Concatenando JS

gulp.task(jsConfig.concatJsTaskName, function(){
    gulp.src(jsConfig.src)
    .pipe(tap(function(file){
        file.contents = browserify(file.path).bundle().on('error',function(error){
            notify().write(error);
        });
    }))
    .pipe(buffer())
    //.pipe(concat("main.js"))
    .pipe(sourcemaps.init({ loadMaps: true }))
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest(jsConfig.dest))
    .pipe(notify("JS Concatenado"))
    .pipe(browserSync.stream());
});

//Minifica js
gulp.task(uglifyConfig.uglifyTaskName, function(){
    gulp.src(uglifyConfig.src)
    .pipe(uglify())
    .pipe(gulp.dest(uglifyConfig.dest))
    .pipe(notify("JS Minificado"))
});

gulp.task('fonts', function(){
     gulp.src('./node_modules/font-awesome/fonts/*')
     .pipe(gulp.dest('./ui/static/ui/fonts'))

});