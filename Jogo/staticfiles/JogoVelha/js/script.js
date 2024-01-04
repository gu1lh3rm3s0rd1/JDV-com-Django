document.addEventListener('DOMContentLoaded', function () {
    // Pega o elemento que contém o texto e a frase a ser digitada
    const textElement = document.querySelector('.typing-text');
    const textToType = textElement.dataset.text;
  
    // Adiciona a frase automaticamente ao conteúdo da página
    function typeText() {
      textElement.textContent = textToType;
    }
  
    typeText();
  });
  