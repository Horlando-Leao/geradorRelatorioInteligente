/* const a = document.getElementById('desejoUsuario').value
console.log(a) */

function buscarRelatorio(desejoUsuario){
    var requestOptions = {
        method: 'GET',
        redirect: 'follow',
        mode: 'no-cors',
        headers: {"Content-Type": "application/json"}
      };
      
      fetch(`http://127.0.0.1:5000/relatorio?desejo=${desejoUsuario}`, requestOptions)
      //fetch(`http://127.0.0.1:5000/relatorio?desejo=${}`, { mode: 'no-cors'})
        .then(response => console.log(response))
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
}


//buscarRelatorio(desejoUsuario="vendas de 2020")
