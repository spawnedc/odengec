var path = require('path');
var rootPath = path.resolve('./');
var srcPath = path.join(rootPath, 'static-dev');
var paths = {
  src: srcPath,
  scss: path.join(srcPath, 'scss', '**', '*.scss'),
  dist: path.join(srcPath, 'css')
};
module.exports = {
  paths: paths
};
