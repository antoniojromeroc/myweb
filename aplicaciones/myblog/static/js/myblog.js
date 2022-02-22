(function() {
    const btnEliminar = document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn=>{
        btn.addEventListener('click', (e)=>{
            const confirmacion = confirm('Seguro que desea eliminar el Registro?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

    var myAlerts = document.querySelectorAll('.alert');
    const myTimeout = setTimeout(myGreeting, 3000);

    function myGreeting() {
        myAlerts.forEach(myAlert => {            
            myAlert.remove();
        });
    }

})();