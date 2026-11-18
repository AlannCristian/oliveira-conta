const formulario = document.querySelector("#formulario-contato");
const resultado = document.querySelector("#resultado-formulario");

formulario.addEventListener("submit", function (evento) {
  evento.preventDefault();

  resultado.textContent =
    "Validação concluída! Esta demonstração não enviou nem salvou dados.";
});
