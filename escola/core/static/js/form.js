class Form {
  constructor(id){
    this.form = document.getElementById(id);
    this.$form = $(`#${id}`);
    this.$form.attr("novalidate","novalidate");
  }

  onSuccess(success){
    this.success = success;

    return this;
  }

  onFail(fail){
    this.fail = fail;
    return this;
  }

  addSanitize(key,sanitizeFn){
    if(!this.sanitize){
      this.sanitize = {};
    }
    this.sanitize[key] = sanitizeFn;
    return this;
  }

  init(){
    this.$form.on('submit',(event)=>{
      event.preventDefault();
      this.form.classList.add('was-validated');

      if (this.form.checkValidity() === false) {
        event.stopPropagation();
      }else{
        $.post(this.$form.attr( "action" ), this.getSerializedFormData())
        .done(this.success)
        .fail(this.fail);
      }
    });
  }

  getFormData(){
    var unindexed_array = this.$form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function(n, i){
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
  }

  getSanitizedFormData(){
    const formData = this.getFormData();

    Object.keys(formData).forEach((key)=>{
      const sanitizeFn = this.sanitize[key];
      if(sanitizeFn){
        formData[key] = sanitizeFn(formData[key],formData);
      }
    })

    return formData;
  }

  getSerializedFormData(){
    const formData = this.getSanitizedFormData();
    console.log(formData);
    return $.param(formData);
  }
}