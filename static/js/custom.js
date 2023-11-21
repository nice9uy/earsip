$(document).ready(function () {
  active_link_menu()
  validation()
});


function active_link_menu() {
  $('.nav .nav-link a').click(function (e) {
    e.preventDefault();
    $('.nav .nav-link a').removeClass('active');
    $(this).addClass('active');
  });
}


function validation() {
  (() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
  })()
}
