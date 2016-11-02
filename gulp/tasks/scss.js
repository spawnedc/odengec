var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var config = require('../config');

gulp.task('scss', function() {
  gulp.src(config.paths.src.scss + '/**/*.scss')
      .pipe(sass())
      .pipe(autoprefixer('last 2 version'))
      .pipe(gulp.dest(config.paths.src.css));
});

gulp.task('scss-build', function() {
  gulp.src(config.paths.src.scss + '/**/*.scss')
      .pipe(sass())
      .pipe(autoprefixer('last 2 version'))
      .pipe(gulp.dest(config.paths.build.css));
});
