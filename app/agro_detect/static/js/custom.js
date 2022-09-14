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


  // show boxes
  function abacha_func() {
    var x = document.getElementById("abacha_div");  
      x.style.display = "block";  
  }
  function akara_func() {
    var x = document.getElementById("akara_div");  
      x.style.display = "block";  
  }

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("predi");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}