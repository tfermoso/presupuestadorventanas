window.onload=()=>{
    document.getElementById("tipoventana").onchange=(e)=>{
        let tipo=e.currentTarget.value;
        document.getElementById("imagenventana").src="/static/img/"+tipo;
    }

    $(".datos").change(()=>{
        let ancho=$("#ancho").val();
        let alto=$("#alto").val();
        let tipo=$("#tipoventana").val();
        if(ancho!="" && alto!=""){
            url="/calcular"
            fetch(url, {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                  ancho,
                  alto,
                  tipo
                })
              })
              .then(response => response.json())
              .then(data => {
                console.log(data);
                $("#precio").html(data.precio)
              })
              .catch(error => {
                console.error('Error:', error);
              });
                        
        }
    })

}