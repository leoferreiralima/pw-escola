function go(url){
  location.href = url;
}

var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});


String.prototype.isEmpty = function() {
  return (this.length === 0 || !this.trim());
};