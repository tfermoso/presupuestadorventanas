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
            alert("calculando..");            
        }
    })

}