
async function requests(){
    const response = await axios.get("http://127.0.0.1:8000/api/usuarios")
    const data = response.data[0]
    console.log(response)

    document.getElementById("nomet").innerHTML = `${data.nome}`
    document.getElementById("emailt").innerHTML = `${data.email}`

}

async function enviar(){
    const nome = document.getElementById("nome") 
    const senha = document.getElementById("senha")
    const email = document.getElementById("email")


    const enviar = await axios.post('http://127.0.0.1:8000/api/usuarios',{
        'nome': nome.value,
        'senha': senha.value,
        'email': email.value
    })
}


function app(){
    requests()
}

app();
