function readURL(input){
    if (input.files && input.files[0]){
      var reader = new FileReader();
      reader.onload = function(e){
        $('#bla').attr('src', e.target.result).width(150).height(200);
      };
      reader.readAsDataURL(input.files[0]);
    }
  }

  // show choosen image before predicting
  document.getElementById('files').addEventListener('change', handleFileSelect, false)
  function handleFileSelect(evt){
      var files = evt.target.files;
      var f = files[0]
      var reader = new FileReader();
      reader.onload = (function(thisFile){
          return function(e){
              document.getElementById('list').innerHTML = ['<img src="', e.target.result, '"title="', thisFile.name, '" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />'].join('')
          };
      })(f);
      reader.readAsDataURL(f)
  }
