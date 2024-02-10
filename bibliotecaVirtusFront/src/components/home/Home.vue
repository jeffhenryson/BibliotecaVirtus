<template>
  <div class="home">
    <h1 v-if="username">Seja Bem-vindo, {{ username }} ao Nosso Mundo Digital!</h1>
    <h1 v-else>Seja Bem-vindo(a) ao Nosso Mundo Digital!</h1>
    <p>Explorar, aprender e se conectar nunca foi tão fácil. Aqui, no <strong>Meu Projeto Vue</strong>, nós trabalhamos
      incansavelmente para trazer a você uma experiência digital única e enriquecedora. Navegue pelo nosso site para
      descobrir ferramentas inovadoras, conteúdos exclusivos e uma comunidade vibrante pronta para te receber de braços
      abertos.</p>
    <p>Seja buscando novos conhecimentos, compartilhando suas experiências ou apenas explorando o que temos a oferecer,
      você está no lugar certo. Bem-vindo à jornada que começa agora. Estamos ansiosos para caminhar ao seu lado.</p>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  computed: {
    username() {
      return localStorage.getItem('username');
    }
  }
};
</script>
  
<style>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f5f5f5;
  color: #333;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 20px;
  text-align: center;
}

h1 {
  color: #2c3e50;
  font-size: 2.5em;
  margin-bottom: 0.5em;
}

p {
  color: #34495e;
  font-size: 1.2em;
  line-height: 1.6;
  max-width: 600px;
  margin-bottom: 1em;
}

strong {
  color: #2980b9;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2em;
  }

  p {
    font-size: 1em;
  }
}
</style>
  