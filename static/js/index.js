window.onload=()=>{
    document.getElementById("tipoventana").onchange=(e)=>{
        let tipo=e.currentTarget.value;
        document.getElementById("imagenventana").src="/static/img/"+tipo;
    }
}