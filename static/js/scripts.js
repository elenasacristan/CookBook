// https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL

function previewFile() {
  var preview = document.querySelector(".img-details img");
  var file = document.querySelector("input[type=file]").files[0];
  var reader = new FileReader();

  reader.addEventListener(
    "load",
    function() {
      preview.src = reader.result;
    },
    false
  );

  if (file) {
    reader.readAsDataURL(file);
  }
}

// this code is used to go back to the standard image in case the user press cancel in the upload file modal window

$(".cancel").click(function() {
  // Change src attribute of image
  $(".img-details img").attr("src", "/static/img/default.jpg");
  $(".upload-file input[type=file]").val(null);
  $(".file-path-wrapper > input").val("");
});
