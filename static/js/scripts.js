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

// // function to unselect the option "Not specified" if one or more allegerns are selected

// $("#na").click(function() {
//   $(".select_allergen").attr("selected", false);
// });

// $(".select_allergen").click(function() {
//   $("#na").removeAttr("selected");
// });
