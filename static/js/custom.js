$(document).ready(function () {
  active_link_menu()
  validation()
  tabel_data()
});


function active_link_menu() {
  $('.nav .nav-link a').click(function (e) {
    e.preventDefault();
    $('.nav .nav-link a').removeClass('active');
    $(this).addClass('active');
  });
}

function tabel_data(){
  new DataTable('#tabel_index');
  new DataTable('#tabel_surat_keluar', {
    "searching": false,
    "dom": 'rtip',
    fixedColumns: {
      left: 1,
      right: 1
  },
  });
  new DataTable('#tabel_klasifikasi',{
    "searching": false,
    "dom": 'rtip'
  });
  new DataTable('#tabel_subklasifikasi' , {
    "searching": false,
    "dom": 'rtip'
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

