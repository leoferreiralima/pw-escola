function show(url,data){
  $('#professor-modal').modal({
    backdrop: true
  });

  $.get(url,data)
  .done(function(response) {
    $('#professor-modal').find(".modal-dialog").html(response);
  })
  .fail(function() {
    
    hide();
  })
}

function hide(){
  const professorModal = $('#professor-modal').modal({
    backdrop: true
  });
  professorModal.modal('hide');
}

