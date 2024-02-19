const agendamento = document.querySelector(".agendamento")
const diaAgendamento = agendamento.querySelector(".day")
const horaAgendamento = agendamento.querySelector(".hora")
const infoAgendamento = agendamento.querySelector(".info")

const calendarioConsultas = document.querySelector("#calendario-consultas")

const diasCalendario = calendarioConsultas.querySelectorAll("button")

diasCalendario.forEach(dia => {
    dia.addEventListener("click", e => {
        e.preventDefault()
        const dataCompleta = dia.children[0].getAttribute("datetime")
        const data = dataCompleta.split("-");
        diaAgendamento.innerHTML = `<p>${data[2]}/${data[1]}</p>`
    })
})