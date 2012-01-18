(function() {
  var googlePlusOneButton;

  $(function() {
    return googlePlusOneButton();
  });

  googlePlusOneButton = function() {
    var po, s;
    po = document.createElement("script");
    po.type = "text/javascript";
    po.async = true;
    po.src = "https://apis.google.com/js/plusone.js";
    s = document.getElementsByTagName("script")[0];
    return s.parentNode.insertBefore(po, s);
  };

}).call(this);
