var path = require('path');
var rootPath = path.resolve('./');
var srcPath = path.join(rootPath, 'static-dev');
var buildPath = path.join(rootPath, 'static');
var paths = {
  src: {
    css: path.join(srcPath, 'css'),
    scss: path.join(srcPath, 'scss'),
    img: path.join(srcPath, 'img')
  },
  build: {
    css: path.join(buildPath, 'css'),
    img: path.join(buildPath, 'img')
  }
};
module.exports = {
  paths: paths
};
