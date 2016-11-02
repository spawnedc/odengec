var gulp = require('gulp');
var config = require('../config');

gulp.task('build', function() {
  gulp.run(['scss-build', 'copy']);
});
