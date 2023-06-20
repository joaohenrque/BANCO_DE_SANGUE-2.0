
  <script>
    document.getElementById("fotoCircle").addEventListener("click", function() {
      document.getElementById("fotoInput").click();
    });

    document.getElementById("fotoInput").addEventListener("change", function() {
      var file = this.files[0];
      var reader = new FileReader();

      reader.onload = function(e) {
        document.getElementById("fotoCircle").style.backgroundImage = "url(" + e.target.result + ")";
        document.getElementById("fotoCircle").innerHTML = "";
      };

      reader.readAsDataURL(file);
    });
  </script>