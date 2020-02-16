(function(d, m){
    var kommunicateSettings = {
        "appId":"1deae80a9100184b299693deb316914c",
        "popupWidget":true,
        "automaticChatOpenOnNavigation":true,
        "sessionTimeout": 0
      };
    var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
    s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
    var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
    window.kommunicate = m; m._globals = kommunicateSettings;
  })(document, window.kommunicate || {});