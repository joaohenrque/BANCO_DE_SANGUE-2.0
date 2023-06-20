document.addEventListener('DOMContentLoaded', function() {
  const perfilForm = document.getElementById('perfilForm');
  const generoFeminino = document.getElementById('generoFeminino');
  const doaLeiteMaterno = document.getElementById('doaLeiteMaterno');

  perfilForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const genero = document.querySelector('input[name="genero"]:checked').value;
    const tipoSanguineo = document.getElementById('tipoSanguineo').value;
    const doacoes = document.querySelectorAll('input[name="doacoes"]:checked');

    if (!nome || !genero || !tipoSanguineo || doacoes.length === 0) {
      alert('Preencha todos os campos obrigatórios!');
      return;
    }

    let doaSangue = false;
    let doaMedula = false;
    let doaLeiteMaternoValue = false;

    for (const doacao of doacoes) {
      if (doacao.value === 'sangue') {
        doaSangue = true;
      } else if (doacao.value === 'medula') {
        doaMedula = true;
      } else if (doacao.value === 'leiteMaterno') {
        doaLeiteMaternoValue = true;
      }
    }

    if (genero === 'Feminino' && !doaLeiteMaternoValue) {
      alert('Selecione a opção "Doa Leite Materno" para o gênero feminino!');
      return;
    }

    // Envie os dados para o servidor ou faça outras ações necessárias
    console.log('Nome:', nome);
    console.log('Gênero:', genero);
    console.log('Tipo Sanguíneo:', tipoSanguineo);
    console.log('Doa Sangue:', doaSangue);
    console.log('Doa Medula:', doaMedula);
    console.log('Doa Leite Materno:', doaLeiteMaternoValue);

    // Aqui você pode fazer uma requisição AJAX para enviar os dados para o servidor

    // Limpar o formulário
    perfilForm.reset();
  });
});
// Script para exibir/esconder o formulário de edição
function toggleEditForm() {
  var editForm = document.getElementById("editForm");
  editForm.style.display = (editForm.style.display === "none") ? "block" : "none";
}

// Evento de clique no link de edição
var editLink = document.getElementById("editLink");
editLink.addEventListener("click", toggleEditForm);
