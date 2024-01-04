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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////

var jogador, vencedor = null;
var jogadorSelecionado = document.getElementById('jogador-selecionado');
var vencedorSelecionado = document.getElementById('vencedor-selecionado');

mudarJogador('X');

function escolherQuadrado(id) {
  if (vencedor !== null) {
    return;
  }

  var quadrado = document.getElementById(id);
  if (quadrado.innerHTML !== '-') {
    return;
  }

  quadrado.innerHTML = jogador;
  quadrado.style.color = '#000';

  mudarJogador();
  checaVencedor();
}

function mudarJogador() {
  jogador = jogador === 'X' ? 'O' : 'X';
  jogadorSelecionado.innerHTML = jogador;
}

function checaVencedor() {
  const sequenciasVitoria = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], // Linhas
    [1, 4, 7], [2, 5, 8], [3, 6, 9], // Colunas
    [1, 5, 9], [3, 5, 7]              // Diagonais
  ];

  for (const sequencia of sequenciasVitoria) {
    const [a, b, c] = sequencia;
    const quadradoA = document.getElementById(a);
    const quadradoB = document.getElementById(b);
    const quadradoC = document.getElementById(c);

    if (checaSequencia(quadradoA, quadradoB, quadradoC)) {
      mudaCorQuadrado(quadradoA, quadradoB, quadradoC);
      mudarVencedor(quadradoA);
      return;
    }
  }
}

function mudarVencedor(quadrado) {
  vencedor = quadrado.innerHTML;
  vencedorSelecionado.innerHTML = vencedor;
}

function mudaCorQuadrado(...quadrados) {
  quadrados.forEach(quadrado => quadrado.style.background = '#0f0');
}

function checaSequencia(...quadrados) {
  return quadrados.every((quadrado, index, array) =>
    quadrado.innerHTML !== '-' && quadrado.innerHTML === array[0].innerHTML
  );
}

function reiniciar() {
  vencedor = null;
  vencedorSelecionado.innerHTML = '';

  for (var i = 1; i <= 9; i++) {
    var quadrado = document.getElementById(i);
    quadrado.style.background = '#eee';
    quadrado.style.color = '#eee';
    quadrado.innerHTML = '-';
  }

  mudarJogador('X');
}
