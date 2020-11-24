function mensaje_alerta(){
    Swal.fire({
        //error
        icon:'error',
        title: 'Error',
        allowOutsideClick :false,
        allowEscapeKey:false,
        text: '¡No tienes los permisos necesarios!',
        background: '#fff url(https://sweetalert2.github.io/images/trees.png)',
        backdrop: `
        rgba(0,0,123,0.4)
        url("https://sweetalert2.github.io/images/nyan-cat.gif")
        left top
        no-repeat
      `
    }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            window.location = 'http://127.0.0.1:8000/';
        } 
      })
}
