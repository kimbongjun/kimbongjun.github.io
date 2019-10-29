$(document).ready(function() {

  'use strict';

  // =================
  // Responsive videos
  // =================

  $('.o-wrapper').fitVids({
    'customSelector': ['iframe[src*="ted.com"]']
  });

  // =================
  // Off Canvas menu
  // =================

  $('.js-off-canvas-toggle').click(function(e) {
    e.preventDefault();
    $('.js-off-canvas-toggle').toggleClass('is-active');
    $('.js-off-canvas-container').toggleClass('is-active');
  });
  // Add some classes to body for CSS hooks

  var ua = window.navigator.userAgent;
    var b = "";
    var msie = ua.indexOf('MSIE ');
    if (msie > 0) {
        // IE 10 or older => return version number
        b = "msie ie" + parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
    }
 
    var trident = ua.indexOf('Trident/');
    if (trident > 0) {
        // IE 11 => return version number
        var rv = ua.indexOf('rv:');
        b = "trident ie"+parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
    }
 
    var edge = ua.indexOf('Edge/');
    if (edge > 0) {
        // Edge (IE 12+) => return version number
        b = "edge ie"+parseInt(ua.substring(edge + 5, ua.indexOf('.', edge)), 10);
 
    }
 
    // other browser
    if(b!="") {
        $('body').addClass(b);
    }

});