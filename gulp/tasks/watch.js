var gulp = require('gulp');
var config = require('../config');

gulp.task('dev', function() {
  gulp.run(['scss']);
});

gulp.task('watch', ['dev'], function() {
  gulp.watch(config.paths.src.scss + '**/*.scss', ['scss']);
});
