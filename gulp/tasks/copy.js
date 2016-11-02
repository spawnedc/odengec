var gulp = require('gulp');
var copy = require('gulp-copy');
var config = require('../config');

gulp.task('copy', function() {
  gulp.src(config.paths.src.img + '/**/*')
      .pipe(gulp.dest(config.paths.build.img));
});
