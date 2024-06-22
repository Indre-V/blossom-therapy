document.addEventListener("DOMContentLoaded", function() {
    if (document.querySelector(".modal-body .alert")) {
        var myModal = new bootstrap.Modal(document.getElementById('messageModal'));
        myModal.show();
    }
});