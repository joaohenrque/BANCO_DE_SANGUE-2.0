<script>
    document.addEventListener("DOMContentLoaded", function() {
      document.getElementById("fotoCircle").addEventListener("click", function() {
        document.getElementById("fotoInput").click();
      });

      document.getElementById("fotoInput").addEventListener("change", function() {
        var file = this.files[0];
        var reader = new FileReader();

        reader.onload = function(e) {
          document.getElementById("profileImage").src = e.target.result;
        };

        reader.readAsDataURL(file);
      });
    });
  </script>